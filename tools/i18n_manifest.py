# -*- coding: utf-8 -*-
"""Single source of truth for the EN -> bilingual string patches.

Used by localize_jar.py (build) and verify_jar.py (self-check).
Referenced keys/values must match upstream master sources at
MobileTribe/commit-template-idea-plugin@e07bcba.
"""

FILE_COMMIT_DIALOG = 'com/leroymerlin/commit/CommitDialog.class'
FILE_COMMIT_PANEL = 'com/leroymerlin/commit/CommitPanel.class'

CLASS_PATCHES = {
    FILE_COMMIT_DIALOG: {
        'Commit': 'Commit (提交)',
        'OK': 'OK (确定)',
    },
    FILE_COMMIT_PANEL: {
        'Type of change': 'Type of change (变更类型)',
        'Scope of this change': 'Scope of this change (变更范围)',
        'Short description': 'Short description (简短描述)',
        'Long description': 'Long description (详细描述)',
        'Closed issues': 'Closed issues (关闭的议题)',
        'Comma-separated list of issues which are closed by this commit':
            'Comma-separated list of issues which are closed by this commit (以逗号分隔的、将被本次提交关闭的议题列表)',
        'Breaking changes': 'Breaking changes (破坏性变更)',
        'Wrap text at 72 characters?': 'Wrap text at 72 characters? (每 72 个字符自动换行)',
        'Wrap at 72 characters?': 'Wrap at 72 characters? (每 72 个字符自动换行)',
        'Skip CI?': 'Skip CI? (跳过 CI)',
        'feat - A new feature': 'feat - A new feature (新功能)',
        'fix - A bug fix': 'fix - A bug fix (修复 Bug)',
        'docs - Documentation only changes': 'docs - Documentation only changes (仅文档变更)',
        'style - Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)':
            'style - Changes that do not affect the meaning of the code (空白、格式化、缺少分号等不影响代码含义的变更)',
        'refactor - A code change that neither fixes a bug nor adds a feature':
            'refactor - A code change that neither fixes a bug nor adds a feature (既非修复 Bug 也非新增功能的代码重构)',
        'perf - A code change that improves performance': 'perf - A code change that improves performance (提升性能的代码变更)',
        'test - Adding missing tests or correcting existing tests':
            'test - Adding missing tests or correcting existing tests (补充缺失的测试或修正既有测试)',
        'build - Changes that affect the build system or external dependencies (example scopes: gulp, broccoli, npm)':
            'build - Changes that affect the build system or external dependencies (影响构建系统或外部依赖的变更，示例范围：gulp、broccoli、npm)',
        'ci - Changes to our CI configuration files and scripts (example scopes: Travis, Circle, BrowserStack, SauceLabs)':
            'ci - Changes to our CI configuration files and scripts (修改 CI 配置文件与脚本的变更，示例范围：Travis、Circle、BrowserStack、SauceLabs)',
        "chore - Other changes that don't modify src or test files":
            "chore - Other changes that don't modify src or test files (不修改 src 或测试文件的其他变更)",
        'revert - Reverts a previous commit': 'revert - Reverts a previous commit (回滚之前的一次提交)',
    },
}

PLUGIN_XML_ENTRY = 'META-INF/plugin.xml'
PLUGIN_CANONICAL = 'resources/META-INF/plugin.xml'
PLUGIN_ACTION_TOKEN = '(创建提交信息)'
PLUGIN_NOTE_TOKEN = '中英双语版'

ANNEX_ENTRIES = [
    'src',
    'tests',
    'resources/META-INF/plugin.xml',
    'LICENSE',
    'README.zh-CN.md',
]
