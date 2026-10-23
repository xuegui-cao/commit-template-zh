# -*- coding: utf-8 -*-
"""Rebuild the bilingual plugin JAR from the base JAR + i18n manifest.

Usage (from the repository root):
    python tools/localize_jar.py --base tools/upstream/commit-template-idea-plugin-base-1.2.1.jar \
                                 --out dist/commit-template-zh-1.2.1.jar

Pipeline: extract base -> patch class constant pools -> swap in the canonical
plugin.xml -> annex source/tests/docs -> repack. Runs its own verification
afterwards.
"""
import argparse
import os
import struct
import sys
import zipfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(1, os.getcwd())

from i18n_manifest import CLASS_PATCHES, PLUGIN_CANONICAL, PLUGIN_XML_ENTRY, ANNEX_ENTRIES
from verify_jar import verify_built_jar


def patch_class_bytes(data, mapping):
    """Rewrite CONSTANT_Utf8 entries. Entries are index-referenced, so only
    the entry's own u2 length prefix needs updating (content may change size).
    Java modified UTF-8 == UTF-8 for BMP-only strings."""
    magic, = struct.unpack_from('>I', data, 0)
    assert magic == 0xCAFEBABE
    off = 8
    count, = struct.unpack_from('>H', data, off)
    off += 2

    slots = []
    i = 1
    while i < count:
        tag = data[off]
        if tag == 1:
            ln, = struct.unpack_from('>H', data, off + 1)
            slots.append((off, off + 3, ln, data[off + 3: off + 3 + ln]))
            off += 3 + ln
        elif tag in (7, 8, 16, 19, 20):
            off += 3
        elif tag == 15:
            off += 4
        elif tag in (3, 4, 9, 10, 11, 12, 17, 18):
            off += 5
        elif tag in (5, 6):
            off += 9
        else:
            raise ValueError(f'bad cp tag {tag} at offset {off}')
        i += 2 if tag in (5, 6) else 1

    out = bytearray()
    prev = 0
    replaced = []
    for entry_start, len_start, ln, raw in slots:
        s = raw.decode('utf-8')
        if s in mapping:
            nb = mapping[s].encode('utf-8')
            out += data[prev:len_start - 2]
            out += struct.pack('>H', len(nb))
            out += nb
            replaced.append(mapping[s])
            prev = len_start + ln
    out += data[prev:]
    return bytes(out), replaced


def collect_annex(repo_root):
    entries = []
    for rel in ANNEX_ENTRIES:
        full = os.path.join(repo_root, rel)
        if not os.path.exists(full):
            raise FileNotFoundError(f'annex missing in repo: {rel}')
        if os.path.isdir(full):
            for root, dirs, files in os.walk(full):
                # skip build junk
                dirs[:] = [d for d in dirs if d not in ('__pycache__',) and not d.endswith('.iml')]
                for f in files:
                    p = os.path.join(root, f)
                    entries.append((os.path.relpath(p, repo_root).replace(os.sep, '/'), p))
        else:
            entries.append((rel, full))
    return entries


def build(base_jar, out_jar, repo_root):
    with zipfile.ZipFile(base_jar) as zin:
        base_entries = {n: zin.read(n) for n in zin.namelist()}

    for name, mapping in CLASS_PATCHES.items():
        if name not in base_entries:
            raise KeyError(f'base jar lacks {name}')
        for k in mapping:
            raw = base_entries[name]
            if k.encode('utf-8') not in raw:
                raise AssertionError(f'base {name} does not contain key {k!r} - base jar mismatch')
        base_entries[name], _ = patch_class_bytes(base_entries[name], mapping)

    with open(os.path.join(repo_root, PLUGIN_CANONICAL), 'rb') as f:
        base_entries[PLUGIN_XML_ENTRY] = f.read()

    entries = [(n, base_entries[n]) for n in base_entries]
    entries += [(rel, open(os.path.join(repo_root, rel), 'rb').read()) for rel, _ in collect_annex(repo_root)]
    entries.sort(key=lambda t: (0 if t[0] == 'META-INF/MANIFEST.MF' else 1, t[0]))

    os.makedirs(os.path.dirname(os.path.abspath(out_jar)), exist_ok=True)
    with zipfile.ZipFile(out_jar, 'w', zipfile.ZIP_DEFLATED) as z:
        for rel, data in entries:
            z.writestr(rel, data)
    print(f'built {out_jar} ({os.path.getsize(out_jar)} bytes, {len(entries)} entries)')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--base', required=True)
    ap.add_argument('--out', required=True)
    ap.add_argument('--repo-root', default='.')
    args = ap.parse_args()
    out = os.path.abspath(args.out)
    build(args.base, out, os.path.abspath(args.repo_root))
    problems = verify_built_jar(out, os.path.abspath(args.repo_root))
    if problems:
        print('SELF-CHECK FAILED:', *problems, sep='\n  ')
        raise SystemExit(1)
    print('build PASS')


if __name__ == '__main__':
    main()
