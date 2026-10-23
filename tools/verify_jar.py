# -*- coding: utf-8 -*-
"""Self-check for the base jar and the built bilingual jar.

    python tools/verify_jar.py --base tools/upstream/...base.jar   (before build)
    python tools/verify_jar.py --jar  dist/...jar                  (after build)
"""
import argparse
import sys
import os
import zipfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from i18n_manifest import CLASS_PATCHES, PLUGIN_XML_ENTRY, PLUGIN_CANONICAL, PLUGIN_ACTION_TOKEN, PLUGIN_NOTE_TOKEN, ANNEX_ENTRIES


def _fail(msgs, text):
    msgs.append(text)


def verify_base_jar(path):
    problems = []
    with zipfile.ZipFile(path) as z:
        with z.open(PLUGIN_XML_ENTRY) as f:
            pxml = f.read().decode('utf-8')
        if 'Create commit message' not in pxml:
            _fail(problems, 'base plugin.xml lacks upstream action text')
        for name, mapping in CLASS_PATCHES.items():
            raw = z.read(name)
            for k in mapping:
                if k.encode('utf-8') not in raw:
                    _fail(problems, f'{name}: base key missing: {k!r}')
    return problems


def verify_built_jar(path, repo_root='.'):
    problems = []
    z = zipfile.ZipFile(path)
    try:
        bad = z.testzip()
        if bad is not None:
            _fail(problems, f'zip corruption at {bad}')
        names = set(z.namelist())
        raw = z.read(PLUGIN_XML_ENTRY)
        pxml = raw.decode('utf-8')
        with open(os.path.join(repo_root, PLUGIN_CANONICAL), 'rb') as f:
            canonical = f.read()
        if pxml.encode('utf-8') != canonical:
            _fail(problems, 'shipped plugin.xml != resources/%s' % PLUGIN_CANONICAL)
        if pxml.count(PLUGIN_ACTION_TOKEN) != 2:
            _fail(problems, f'plugin.xml: expected 2x {PLUGIN_ACTION_TOKEN!r}')
        if PLUGIN_NOTE_TOKEN not in pxml and 'Bilingual' not in pxml:
            _fail(problems, 'plugin.xml lacks bilingual note')
        for name, mapping in CLASS_PATCHES.items():
            if name not in names:
                _fail(problems, f'built jar lacks {name}')
                continue
            data = z.read(name)
            for v in mapping.values():
                if v.encode('utf-8') not in data:
                    _fail(problems, f'{name}: localized value missing: {v!r}')
        for rel in ANNEX_ENTRIES:
            if rel not in names and not any(n.startswith(rel + '/') for n in names):
                _fail(problems, f'built jar missing annex entry {rel}')
    finally:
        z.close()
    return problems


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--base')
    ap.add_argument('--jar')
    ap.add_argument('--repo-root', default='.')
    args = ap.parse_args()
    problems = []
    if args.base:
        problems += verify_base_jar(args.base)
    if args.jar:
        problems += verify_built_jar(args.jar, os.path.abspath(args.repo_root))
    if problems:
        print('FAIL:', *problems, sep='\n  ')
        raise SystemExit(1)
    print('verify PASS')


if __name__ == '__main__':
    main()
