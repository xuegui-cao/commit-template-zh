# Git Commit Template 中英双语版

IntelliJ 插件 **Git Commit Template**（id: `commit-template-idea-plugin`）的**中英双语界面版**：
所有界面提示保留英文原文并以 `English (中文翻译)` 格式追加中文，共 25 处。
未做任何功能改动，插件逻辑与上游完全一致。

## 为什么做这个项目

原插件已经很成熟，但它默认面向熟悉 Conventional Commits 的开发者。实际工作中，
**很多新入行的程序员对各提交类型（feat / fix / docs / style / refactor / perf / test /
build / ci / chore / revert）的具体含义并不熟悉**，界面上那些长串的英文类型说明经常
看不懂、错选类型，导致提交信息不规范、code review 时返工。

本项目正是为此而来：**在保留英文原文的前提下，为每条类型说明追加中文翻译**，
让对 Conventional Commits 陌生的同事（尤其是英语不熟悉的同学）也能一眼读懂
"这个类型适合哪种改动"，从源头减少错选类型、乱写提交信息的情况。

## 安装

1. 从 [Releases](../../releases) 下载 `commit-template-zh-1.2.1.jar`
2. IDE 中：**File → Settings → Plugins → ⚙️ → Install Plugin from Disk**，选择该 JAR
3. 重启 IDE

## 包里有什么

- 可执行插件 class（与上游 1.2.1 相同，仅常量池字符串双语化）
- 参考源码 `src/`、`tests/`（`src/` 与 class 逐字对应的本地化版本）
- `LICENSE`（Apache-2.0，不得移除）、`README.zh-CN.md`（即本文件）

## 从源码复现 JAR

不需要 IntelliJ SDK，只要 Python 3.8+：

```bash
python tools/localize_jar.py --base tools/upstream/commit-template-idea-plugin-base-1.2.1.jar \
                             --out dist/commit-template-zh-1.2.1.jar
```

构建完会自动自检（全部双语字符串逐项断言）。提交式版本 `"Create commit message (创建提交信息)"`
等所有改动集中在 [`tools/i18n_manifest.py`](tools/i18n_manifest.py) —— 想调整译文只改这个文件。

- 基线 JAR：`tools/upstream/` 内，SHA-256 `b2f9965c50b01a79987db65fa556b091a052424bf1948eac69a3cabf443f41a7`
- 参考：上游源码 https://github.com/MobileTribe/commit-template-idea-plugin （master @ `e07bcba`，
  包内 class 字符串与该源码逐字对应，已逐项校验）

## 目录结构

```
src/       com/leroymerlin/commit/ 本地化 Java 源码 + CommitPanel.form
tests/     CommitMessageTest / GitLogQueryTest（需 junit4 + commons-lang）
resources/ plugin.xml（双语版）+ icons/
tools/     提交流水线：i18n_manifest.py / localize_jar.py / verify_jar.py + 基线 JAR
docs?      见根目录 NOTICE / CHANGELOG
```

## 执行单元测试（可选）

```bash
javac -cp "junit.jar;commons-lang.jar;<IntelliJ>\lib\*;<IntelliJ>\plugins\vcs\*" -d out tests/com/leroymerlin/commit/*.java
```

单元测试覆盖提交模板解析逻辑，界面字符串改动不影响其断言。

## 上游与许可证

- 上游项目（Apache-2.0）：https://github.com/MobileTribe/commit-template-idea-plugin
- 本仓库修改声明见 [NOTICE](NOTICE)，变更历史见 [CHANGELOG](CHANGELOG.md)，许可证未变更。

## 未翻译项（刻意保留）

- 类型小写名 `feat` / `fix` / … —— 提交模板语法 `type(scope): subject` 及解析回填依赖它
- 模板标记 `BREAKING CHANGE:`、`Closes`
- `ChangeType` 枚举字段（界面不显示）

## 发布到 Marketplace 前需要做

1. 改 `<id>`：如 `commit-template-zh.<你的名>`（与官方插件并存）
2. 在 JetBrains 注册插件签名证书（2021.2+ 强制）
3. README 补充 Marketplace 安装入口

也欢迎把双语化以 i18n message bundle 的形式 PR 回上游，合并后此 fork 即可退役。
