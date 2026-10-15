# AI Career Copilot Skill

面向 AI 工程方向的技术成长与求职技能。支持 Agent、模型评测、RAG、NLP 等背景，基于使用者提供的材料工作，不预设学历、任职经历或技术水平。

这个公开版本从个人使用流程中提炼而来，**不包含作者或其他人的真实简历、联系方式、照片、公司项目原文和实验数据**。个人资料与通用技能分开保存。

## 可以做什么

| 任务 | 产出 |
| --- | --- |
| 分析JD | 已有证据、技能自述与关键缺口的对照 |
| 改写简历 | 受事实约束的项目叙述，按用户要求制作文档 |
| 模拟面试 | 基于真实项目的追问、复盘与备答提示 |
| 技术提升 | 可执行项目、实现路径与验证条件 |

技能区分个人贡献和项目结果，不把招聘关键词补成经历，不给无依据的录用概率。当前岗位查询需要运行环境具备联网能力；文件生成需要相应的文档工具。技能本身不安装这些工具，也不执行自动投递。

## 安装到 Codex

1. 下载或克隆这个仓库。
2. 将 `skills/ai-career-copilot` **整个文件夹**复制到个人技能目录。未设置 `CODEX_HOME` 时为 `~/.codex/skills/`；设置了则使用该目录下的 `skills/`。
3. 在能够发现该技能的新聊天中调用 `$ai-career-copilot`。

Windows PowerShell 示例（在选定的工作目录运行，目标目录已存在时先检查内容，不覆盖）：

```powershell
git clone https://github.com/coolwkx/ai-career-copilot-skill.git
$skillBase = if ($env:CODEX_HOME) { Join-Path $env:CODEX_HOME 'skills' } else { Join-Path $env:USERPROFILE '.codex/skills' }
$skillTarget = Join-Path $skillBase 'ai-career-copilot'
if (Test-Path -LiteralPath $skillTarget) { throw '目标已存在，请先检查已有技能。' }
New-Item -ItemType Directory -Path $skillBase -Force | Out-Null
Copy-Item -LiteralPath './ai-career-copilot-skill/skills/ai-career-copilot' -Destination $skillTarget -Recurse
```

技能可自动匹配相关任务，也可以显式调用。无需修改全局模型设置或连接外部账号。

## 快速开始

直接提供简历、项目描述或JD，不必先建立档案：

```text
使用 $ai-career-copilot，对照这份JD分析我的匹配度。
区分已有经历支持、只有技能自述、尚未具备的条件。
```

```text
使用 $ai-career-copilot，根据我提供的项目描述模拟面试。
一次问一道，等我回答后再点评，不替我编造实验数据。
```

```text
使用 $ai-career-copilot，基于我的RAG经验设计一个小型评测项目。
优先使用现有仓库，给出可运行实现与验收方法。
```

## 可选的私有背景档案

将技能中的 `templates/profile.example.json` 复制到**仓库以外**的私有位置，再填写实际背景。它是空结构示例，不包含需要继承的经历。调用时指定该文件路径即可。

项目条目可以记录：项目名、日期、本人职责、工作动作、结果、指标定义、来源、待核实点。只保存完成当前任务需要的信息。更新时间用于判断资料新旧，不代替当前日期。

不要将填好的档案、真实简历、照片、密钥或公司内部材料提交到公开仓库。`.gitignore` 提供常见排除项，但不能替代提交前检查。没有档案仍可在当前聊天中提供必要信息。

## 文件结构

```text
skills/ai-career-copilot/
  SKILL.md
  agents/openai.yaml
  references/evidence.md
  references/workflows.md
  templates/profile.example.json
scripts/validate_skill.py
tests/scenarios.md
```

## 验证与贡献

运行 `python scripts/validate_skill.py`，使用 Python 3 标准库，无第三方依赖。检查包结构、引用路径、基础元数据及空模板；行为检查用例见 `tests/scenarios.md`。这些检查不能证明所有模型和环境下的实际表现。

欢迎提出改进。提交问题或示例时请使用虚构或已获授权的材料，不上传真实个人档案和雇主保密资料。修改时保持“事实、证据、未知项、建议”之间的区别。

## 许可证

[MIT](LICENSE)。技能指令与空模板可复用、修改和分享。使用者另外提供的资料不因此获得公开授权。
