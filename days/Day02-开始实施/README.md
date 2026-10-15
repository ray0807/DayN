# Day2：销售方案与实践启动包

**你只做关键选择，AI负责研究、解释、计算和起草。**

Day1回答“卖什么”，Day2回答“怎么卖”。最终交付一份实践启动包：一页行动摘要、报价测算、客户渠道方案、必备的独立站首版方案与文案、沟通和交易模板、收款交付研究、带证据的首批潜在客户名单、验证清单，最后以一张“直接开干表”收尾，看完就能动手。

## 使用入口

可执行技能：[dayn-start-action/SKILL.md](dayn-start-action/SKILL.md)。概览：[TASK.md](TASK.md)。

~~~text
使用 $dayn-start-action，读取我的Day1产品和报告，先分析已知条件，
再准备报价、客户渠道、必备独立站首版、展示话术和收款交付方案，
交付首批潜在客户名单及实践启动包。你负责研究、解释和起草，我只做关键选择；
先给一页行动摘要，最后给直接开干表。Day2只准备，实际对外动作在后续实践按授权执行。
~~~

开始前准备好Day1的选品报告或决策记录（例如私有 `records/` 目录中的文件）。新对话无法读取以前的聊天，没有记录时Agent只补问影响销售方案的关键缺口，不重做选品。

## 整体流程

读取Day1结果 → 整理已确认条件 → 解释渠道差别并了解偏好 → 并行研究报价、渠道、竞争、收款与手续 → 集中让用户做关键选择 → 起草网站文案与各类模板 → 一页摘要 + 启动包 + 直接开干表。

独立研究和草稿可以并行，不机械逐项串行。每轮最多问1–3个真正影响方案的问题；已有明确选择不重问。

## 交付内容

| 部分 | 内容 |
|---|---|
| 底价与报价 | 公开货源价、费用承担方、内部测算与缺项、供应商询价单、起订量冲突的处理、样品政策 |
| 客户与渠道 | 客户筛选条件、1–2个主触达渠道、竞争对手如何获客与报价 |
| 独立站首版（必交付） | 实现路线与费用、页面结构、目标市场语言文案、图片资料清单、询盘入口、实施与验收任务 |
| 展示与话术 | 价值主张、零库存展示方式、开发信与跟进、常见问题回复 |
| 交付与收款 | 物流线路与参考价、贸易条款、符合主体与市场条件的收款候选、出口手续 |
| 成交与履约 | 询盘处理、报价单/形式发票/订单确认单、付款条款、样品单、设计稿确认、验货节点、复购机制 |
| 首批客户名单 | 先验证筛选规则再扩展，记录公开来源、匹配证据与核实状态，不猜邮箱、不凑数 |
| 实践启动包 | 动手清单、验证清单与判断标准、跟进表、直接开干表 |

价格、运费、关税、收款费率、出口手续等当前信息都要查证并标注来源与日期。公开价只用于内部测算，供应商确认前不当对外报价；效果图标明是示意，不写成实物。

## 你负责决定

主触达渠道、报价及样品方案、资金与垫付边界、收款方案、独立站首版范围与实现路线、验证标准。独立站是本系列约定的必备阵地，不再问要不要建站；实际注册、付费、发布由你按权限决定。

## Day2不做什么

不联系供应商或客户，不注册账号，不购买域名，不发布网站，不付款，不对外承诺价格或交期。这些都整理进直接开干表，在实践阶段按授权执行。

## 结束与后续

启动包交付后，按你的授权把决策记录保存到私有位置（建议 `records/`，写入前检查是否被 Git 忽略）。记录模板随技能一起安装：[references/decision-record-template.md](dayn-start-action/references/decision-record-template.md)。

之后使用 [持续实践](../DayN-持续实践/TASK.md)，从直接开干表的第一项开始，根据真实结果更新价格、网站和行动安排。录制脚本仅在聊天提供，不保存到项目或上传GitHub。

## 给 AI Agent 的安装说明

当用户要求安装 Day2 技能时：

1. 获取完整技能文件夹 `days/Day02-开始实施/dayn-start-action`（本地仓库，或克隆 `https://github.com/ray0807/DayN`）。必须保留 `SKILL.md`、`agents/openai.yaml` 和 `references/decision-record-template.md`。
2. 确定技能目录：Codex 使用 `$CODEX_HOME/skills`，未设置时使用 `~/.codex/skills`；新版 Codex 也识别项目 `.agents/skills/` 或个人 `~/.agents/skills/`。目标应为 `<技能目录>/dayn-start-action/SKILL.md`，不要多套一层目录。
3. 同名技能已存在时，先比较内容并按用户要求决定是否覆盖，不静默替换本机修改。
4. 复制后确认上述三个文件都存在，回复安装路径和调用示例 `$dayn-start-action`。当前会话没有识别新技能时，请用户开新会话再调用。
5. 安装时不启动业务研究，不读取或上传用户的私人记录。

Windows PowerShell（在仓库根目录运行）：

~~~powershell
$source = (Resolve-Path -LiteralPath 'days/Day02-开始实施/dayn-start-action').Path
$skillRoot = if ($env:CODEX_HOME) { Join-Path $env:CODEX_HOME 'skills' } else { Join-Path $env:USERPROFILE '.codex/skills' }
$target = Join-Path $skillRoot 'dayn-start-action'
if (Test-Path -LiteralPath $target) { throw '技能已存在，请先检查再更新。' }
New-Item -ItemType Directory -Path $skillRoot -Force | Out-Null
Copy-Item -LiteralPath $source -Destination $target -Recurse
Get-Item -LiteralPath (Join-Path $target 'SKILL.md'), (Join-Path $target 'agents/openai.yaml'), (Join-Path $target 'references/decision-record-template.md')
~~~

macOS / Linux（在仓库根目录运行）：

~~~bash
source_dir='days/Day02-开始实施/dayn-start-action'
skill_root="${CODEX_HOME:-$HOME/.codex}/skills"
target="$skill_root/dayn-start-action"
if [ -e "$target" ]; then
  echo '技能已存在，请先检查再更新。'
else
  mkdir -p "$skill_root" && cp -R "$source_dir" "$target" &&
    test -f "$target/SKILL.md" && test -f "$target/agents/openai.yaml" &&
    test -f "$target/references/decision-record-template.md" && echo '安装完成'
fi
~~~

更新已安装的版本时，先确认本机没有需要保留的修改，再删除旧目录后重新复制。不支持加载技能的工具，可以直接要求 Agent 读取本目录的 `dayn-start-action/SKILL.md`，这只是本次对话使用，不等于安装。
