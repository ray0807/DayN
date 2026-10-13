# Day N：从零开始做 B2B 外贸

一套可复用的 AI 外贸实践 skills：准备两天（Day1定卖什么，Day2定怎么卖），随后利用AI、自动化和已有能力持续开展真实业务，遇到问题解决问题，没有固定终点。

**需要调研的由 AI 主动完成，需要决策的交给用户。**

AI 查资料、比较方案、提出推荐并整理材料；用户提供真实个人条件，决定方向、投入与关键取舍。AI 给出推荐不等于用户已经选择。已明确的选择继续有效，不反复确认。

## 从哪里开始

第一次使用，先用 [通用外贸起步访谈](skills/trade-startup-interview/SKILL.md)。它逐步收集每个人的目标、经验、时间、预算、能力与资源，根据答案分析和答疑，不预设业务方向或技术能力。B2B专项路线只适用于用户明确想探索B2B后。

通用启动提示词：

> 请读取 skills/trade-startup-interview/SKILL.md，通过提问了解我的实际情况，再根据回答分析和回答我的问题。每轮最多三个问题，已说过的不要重问，没说过的不要假设。我不知道的专业知识由你解释或调查，关键取舍由我决定。信息足够时整理起步表，未知项保留待确认。

确认要探索B2B后，读取 [Day 1 Agent技能](days/Day01-快速起步/dayn-quick-start/SKILL.md)：询问真实条件后，AI主动联网研究至少10个具体商品并通过多轮询问和补充调研筛到一个优先产品，完整比较后由用户选择；供应商开发不属于Day1。其他Day的技能入口见 [实践路线](docs/dayn-roadmap.md)。各Day技能保存在对应目录，可直接要求Agent读取；现有安装脚本只安装skills目录内的专项模块，未自动安装这些Day技能。

完整顺序见 [Day 1—Day N 大纲](docs/dayn-roadmap.md)。Day 1定卖什么：交付至少10个具体产品的选品报告并通过多轮询问和补充调研筛到一个优先产品；Day 2定怎么卖：报价、客户与渠道、话术、交付与收款，并交付实践启动包；Day 3起持续实践。准备共两天，只能靠实践获得的信息列入验证清单随业务验证，不强制每天一集，没有固定结束日期。

## 目录

```text
days/       每个Day的可执行Agent技能，以及任务概览
skills/     可复用的专项 skills 与总导师
docs/       完整路线和决策记录模板
scripts/    安装与格式检查
```

## Skills 分类

| 类别 | Skill | 对应阶段 |
|---|---|---|
| 通用访谈 | [trade-startup-interview](skills/trade-startup-interview/SKILL.md) | 收集个人条件、分析与答疑，不预设方向 |
| 总体辅导 | [b2b-trade-mentor](skills/b2b-trade-mentor/SKILL.md) | 确定B2B后的系列，保持条件与选择连续 |
| 起步条件 | [b2b-startup-planner](skills/b2b-startup-planner/SKILL.md) | Day 1及后续投入调整 |
| 方向选择 | [b2b-direction-research](skills/b2b-direction-research/SKILL.md) | Day 1及后续方向调整 |
| 产品与市场 | [b2b-product-market-research](skills/b2b-product-market-research/SKILL.md) | Day 1—2及实际需求出现时 |
| 流程与准入 | [b2b-trade-readiness](skills/b2b-trade-readiness/SKILL.md) | Day 2及具体交易准备 |
| 供应与样品 | [b2b-supplier-research](skills/b2b-supplier-research/SKILL.md) | 供应与样品需要时 |
| 成本与报价 | [b2b-cost-quotation](skills/b2b-cost-quotation/SKILL.md) | 具体报价需求出现时 |
| 产品展示 | [b2b-product-assets](skills/b2b-product-assets/SKILL.md) | Day 2及后续资料更新 |
| 客户积累 | [b2b-customer-development](skills/b2b-customer-development/SKILL.md) | 首轮实施及持续客户开发 |
| 工具与自动化 | [b2b-lean-automation](skills/b2b-lean-automation/SKILL.md) | 启动工具及随时加入的自动化 |
| 阶段复盘 | [b2b-progress-review](skills/b2b-progress-review/SKILL.md) | 持续实践中的定期复盘 |
| 真实内容 | [b2b-real-content-log](skills/b2b-real-content-log/SKILL.md) | 每期实际工作完成后，按需使用 |

一个 Day 可以调用多个相关 skill，同一个 skill 可以服务多个 Day。准备事项合并推进，不为了增加天数拆任务。原30项保留为按需参考。

## 安装前先看这里

本项目的 skills 是给 AI 阅读的工作指导，不是一个需要运行 Python 的外贸软件。安装后仍需要你提供真实条件、作出关键选择并开展实际业务。

下载或解压项目，进入包含 `README.md`、`skills/`、`days/` 的目录。以下命令均从这个目录运行；仓库还未上传时，直接使用本地文件即可。

每个 skill 是一个完整文件夹，复制时保留 `SKILL.md`、`agents/` 和可能存在的 `references/`。不要把十二个 `SKILL.md` 合并成一个文件，也不要把整个项目压缩包当作单个 skill 导入。

| 工具 | 推荐安装方式 | 调用方式 |
|---|---|---|
| Codex | 项目 `.agents/skills/`，或按本机已识别的个人技能目录安装 | 选择技能或在提示词中指定名称 |
| TraeCode / TRAE IDE | 项目 `.trae/skills/`，或从技能设置导入 | 自然语言指定技能名称 |
| TraeWork | 将单个 skill 打包后，通过技能上传入口安装 | 从技能列表选取，或自然语言指定名称 |
| ChatGPT Work | 有技能入口时创建或上传；没有时使用附件指导 | 选择已安装技能，或明确要求读取附件 |
| 其他能读取文件的 AI 工具 | 读取当前 Day 和对应 `SKILL.md` | 用文末通用提示词启动 |

以下说明依据 2026-10-09 查阅的官方文档。产品界面与支持范围可能变化，实际入口以你的版本为准；这些步骤未逐个平台实机验证。

## 在 Codex 中安装

### 推荐：仅在当前项目使用

当前官方文档列出的项目发现目录是 `.agents/skills/`，个人目录是 `~/.agents/skills/`。安装目录与具体版本有关，不把旧版 `.codex/skills/` 当作所有版本的唯一位置。[Codex 官方技能文档](https://developers.openai.com/codex/skills/)

Windows 在项目根目录打开 PowerShell，运行：

```powershell
& .\scripts\install-skills.ps1 -Destination (Join-Path (Get-Location).Path '.agents/skills')
```

安装后的结构应为：

```text
项目目录/
├── days/
├── skills/                    原始 skill 集合
└── .agents/
    └── skills/                Codex 发现目录
        ├── b2b-startup-planner/
        │   ├── SKILL.md
        │   └── agents/openai.yaml
        └── b2b-trade-mentor/
            ├── SKILL.md
            ├── agents/openai.yaml
            └── references/dayn-routing.md
```

用 Codex 打开这个项目。若技能没有出现，重新打开会话或重启工具，再检查文件路径。CLI / IDE 可通过 `/skills` 或输入 `$` 选择技能；其他界面可从技能选择入口或直接指定名称。[调用与发现说明](https://developers.openai.com/codex/skills/)

Day 1 启动示例：

```text
使用 $b2b-startup-planner，帮我完成 Day 1 起步盘点。
先读取 days/Day01-快速起步/TASK.md 和会话已有信息。
AI 主动整理时间、预算、能力和资源，只向我询问真实个人条件与关键取舍。
同一次工作完成行业、产品与企业客户初筛，推荐暂定组合；未知项保留待验证，不加入盈利目标。
```

### 在多个项目中使用

按当前官方个人目录安装：

```powershell
$personalSkills = Join-Path ([Environment]::GetFolderPath('UserProfile')) '.agents/skills'
& .\scripts\install-skills.ps1 -Destination $personalSkills
```

如果你的本机版本已经识别 `.codex/skills`，也可指定该目录。此前本项目的安装脚本默认使用 `CODEX_HOME/skills`，未设置时使用 `~/.codex/skills`；这是脚本的兼容默认行为，不是最新官方目录的替代说明。

macOS / Linux 无需运行 PowerShell，可手动将 `skills/` 下的完整技能文件夹复制到项目 `.agents/skills/` 或个人 `~/.agents/skills/`。

建议选择项目或个人安装之一，避免同名技能重复出现。只想试用 Day 1 时，可以仅安装两个模块：

```powershell
& .\scripts\install-skills.ps1 `
  -Destination (Join-Path (Get-Location).Path '.agents/skills') `
  -Names 'b2b-startup-planner', 'b2b-real-content-log'
```

## 在 TraeCode / TRAE IDE 中安装

### 方式一：复制到项目技能目录

Windows 在本项目目录运行：

```powershell
& .\scripts\install-skills.ps1 -Destination (Join-Path (Get-Location).Path '.trae/skills')
```

然后用 TRAE 打开项目，在“设置 → 技能与命令”中检查技能。也可以从该入口创建技能并导入单个 `SKILL.md` 或单技能 ZIP；带参考文件的总导师建议保留完整文件夹。[TraeCode 官方说明](https://docs.trae.cn/ide_skills)

调用示例：

```text
用 b2b-startup-planner 技能帮我完成 Day 1。
读取 days/Day01-快速起步/TASK.md，根据已有信息主动整理，
只问我个人条件和关键取舍，最终生成起步盘点表。
```

### 方式二：使用共享的 .agents 目录

已经为 Codex 安装到项目 `.agents/skills/` 时，可在 TRAE 的“设置 → 技能与命令 → 导入设置”打开“启用 .agents 技能目录”。避免再复制另一套同名技能；TRAE 对同名 `.trae` 技能的优先级见其官方文档。[共享目录说明](https://docs.trae.cn/ide_skills)

### 个人全局安装

TraeCode 国内版官方个人目录为 `~/.trae-cn/skills`，Windows 对应用户目录下 `.trae-cn/skills`：

```powershell
$traeSkills = Join-Path ([Environment]::GetFolderPath('UserProfile')) '.trae-cn/skills'
& .\scripts\install-skills.ps1 -Destination $traeSkills
```

此处按国内版文档说明。国际版优先使用项目 `.trae/skills/` 或界面导入，并核对当前版本文档，避免套用未经核实的个人目录。

## 在 TraeWork 中安装

TraeWork 支持在“插件市场 → 技能 → 上传技能”导入本地包。官方要求 ZIP 或 `.skill` 文件的根目录包含 `SKILL.md`。[TraeWork 官方说明](https://docs.trae.cn/work_skills?lang=zh)

### 第一步：单独打包一个 skill

先试用起步规划模块。Windows 在项目根目录运行：

```powershell
Compress-Archive `
  -Path '.\skills\b2b-startup-planner\*' `
  -DestinationPath '.\b2b-startup-planner.zip'
```

ZIP 打开后的第一层应是：

```text
SKILL.md
agents/
```

打包总导师时，把它的文件夹内容完整压缩，保留 `references/`。不要额外套一层 `skills/` 或项目文件夹。已有同名 ZIP 时先换一个输出文件名。

### 第二步：上传并使用

1. 打开“插件市场 → 技能 → 上传技能”。
2. 上传刚生成的单技能 ZIP，完成安装。
3. 在已安装列表检查技能与当前运行环境；本地与云端任务的技能适用环境不同。
4. 从技能列表选择，或说“用 b2b-startup-planner 帮我完成 Day 1”。

需要其他阶段时，再导入对应模块。不要假定本地复制的技能已同步到云端。若当前界面布局变化，以“技能”管理入口为准。[安装、调用与运行环境](https://docs.trae.cn/work_skills?lang=zh)

把 `days/` 和 `docs/` 作为项目资料保留，或附上当天的 `TASK.md`。仅导入 skill 不会自动附带整套 Day 大纲。

## 在 ChatGPT Work 中使用

这里指 OpenAI 的 ChatGPT Work，和上面的 TraeWork 是两个产品。

### 有技能管理入口

根据账户与工作区开放情况，在“Plugins → Skills → Create”中选择从电脑上传、聊天创建或编辑器创建。调用时可用 `@` 选择技能。具体安装、权限和同步可能因产品界面而异。[ChatGPT 技能帮助](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)、[官方调用说明](https://developers.openai.com/codex/skills/)

先导入 `b2b-startup-planner`，附上 Day 1 的 `TASK.md`。上传文件格式按界面要求；不要默认它支持整套多技能项目 ZIP。总导师需要保留其参考文件，若当前导入方式不支持，则先使用独立模块。

启动提示词：

```text
使用已安装的 B2B 起步规划技能，按我附上的 Day 1 任务推进。
已确定的条件不要重问；AI负责研究、解释与整理，
我负责真实投入条件与关键选择。最后给出起步盘点表。
```

### 没有技能入口：通过文件指导当前对话

上传 `skills/b2b-startup-planner/SKILL.md` 和 `days/Day01-快速起步/TASK.md`，要求助手先读取再执行。这是当前会话使用文件指导，不等同于持久安装。不能上传 Markdown 时，将这两个文件的内容粘贴到对话。

普通附件模式不会自动赋予联网、文件写入或外部应用权限；缺少能力时应明确哪些内容还未验证。

## 其他 AI 工具的通用方式

工具能读取项目文件时，直接使用以下提示词：

```text
先读取 skills/b2b-startup-planner/SKILL.md，
再读取 days/Day01-快速起步/TASK.md，按它们推进当前任务。
需要调研的由你主动完成，需要关键取舍的由我决定。
只问我你无法自行获得的个人信息；给出推荐、依据和未知项。
不能联网时说明当前未核实，不虚构事实。
```

之后换成对应 Day 的任务文件与 skill。没有原生技能发现机制时，不依赖 `$`、`@` 或 `/` 自动加载文件。

## 如何确认真的在使用 skill

请助手简短说明本次使用的 skill 名称、可读取的文件和第一项行动，然后检查行为：

- 是否保留已确定的 B2B 方向和已有答案？
- 是否自行分析专业问题，而非让你回答整套行业问卷？
- 是否将事实、AI推荐、用户决定和待验证项分开？
- 是否对当前信息提供来源，不能查证时说明限制？

文件被识别不等于模型每次都可靠执行。发现偏差时指出具体问题，让助手重新对照当前 skill 修正。

## 更新、脚本与常见问题

已有同名且内容不同的文件，安装脚本默认拒绝覆盖。确实要更新时，在原命令后加 `-Overwrite`；它会覆盖本集合对应文件，不删除其他文件。

Python 不是使用 skills 的前提。`scripts/validate_skills.py` 只做可选的结构检查；PowerShell 脚本只负责复制文件。遇到脚本执行限制可以手动复制完整 skill 文件夹，不必为了安装改变系统策略。

技能不可见时，检查是否多套一层目录、`SKILL.md` 名称和 YAML 头是否保留、界面是否启用技能，以及当前本地/云端环境是否一致。`days/` 是行动大纲，不能替代技能目录。

新对话需要提供上一阶段的决策记录，不能假定跨工具、跨会话自动记住所有进展。只选择当前需要的模块，避免同时加载十二份指导。

本套集合未要求某个外部应用。需要表格、网站或自动化成果时使用当前环境可用的工具；联网和执行权限不会因复制 skill 自动增加。

## 共同约定

- 既定方向是 B2B，用户主动调整时再改。低成本不等于零预算。
- 当前信息须查证，来源说明日期、范围和条件；公开报价不等于实际成交价。
- 学习、调研、样品观察、客户沟通和交易事实分别记录，不伪造进展。
- 先以用户设定的探索目标开展工作，不强行加入盈利目标和成交期限。
- 研究和起草主动推进，实际花钱、联系、下单和发布遵循已有授权。
- 用户在工作间隙拍摄是制作条件，不自动成为视频主题；内容尽量用表格录屏与口播。

## 保存实际进展

使用 [决策记录模板](docs/decision-record-template.md)，保留事实、AI建议、用户决定、未知项与下一步。个人预算、供应价格和客户记录建议保存在自己的私有位置，避免误上传。

## 检查与上传

```powershell
python scripts/validate_skills.py
```

检查名称、元数据、引用、Day映射和未完成占位项。格式检查不等于市场结论或模型行为已验证。脚本只使用 Python 标准库，校验本集合采用的字符串型 YAML 子集。

本目录可由你自行上传 GitHub。提交 `README.md`、`days/`、`skills/`、`docs/`、`scripts/` 和 `.gitignore` 即可；`outputs/` 中的本地工作文件不属于公开 skill 集合。
