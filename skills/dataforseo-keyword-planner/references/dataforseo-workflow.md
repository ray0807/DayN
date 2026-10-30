# DataForSEO接入与数据规则

文档核对日期：2026-10-30。实际运行前重新查看当前工具schema和相关API文档，不能仅凭此文件断言接口永远不变。以下是能力与端点映射，不是某个客户端必定存在的MCP函数。

## 1. 识别连接

先查看当前可用工具。官方v3 MCP文档列出 `docs_index`、`docs_list_sections`、`docs_search`、`api_request`；具体前缀与参数以本环境为准。旧版或第三方封装可能暴露专用工具，按其schema调用，不强行更换用户已有实现。

官方资料：

- [DataForSEO API v3](https://docs.dataforseo.com/v3/)
- [官方MCP仓库与接入说明](https://github.com/dataforseo/mcp-server-typescript)

只有API凭据但没有工具时，说明尚未在当前会话接入。用户要求连接时才按客户端当前文档配置；仅接入不授权无限付费查询。HTTP认证与环境变量方式以官方版本为准，不自行把API密码当Bearer令牌，也不把Base64认为是加密。用户密钥只保存在获准使用的私密配置或进程环境，报告不回显凭据和认证头。

## 2. 选择当前需要的API

| 目的 | HTTP能力路径参考 | 怎么使用 |
|---|---|---|
| 核实地区语言 | `/v3/dataforseo_labs/locations_and_languages` | 确认支持组合，不猜location_code或默认美国 |
| 批量关键词概览 | `/v3/dataforseo_labs/google/keyword_overview/live` | 给已筛词补指标，保留市场和语言范围 |
| 产品词扩展 | `/v3/dataforseo_labs/google/keyword_suggestions/live` | 少量相关种子开始，控制limit |
| 相关需求 | `/v3/dataforseo_labs/google/related_keywords/live` | 控制depth，初轮小深度，避免递归全量扩展 |
| 搜索意图 | `/v3/dataforseo_labs/google/search_intent/live` | 仅已有结果缺少必要意图时使用 |
| 关键SERP抽查 | 当前MCP支持的目标搜索引擎SERP工具 | 明确地区、语言、设备，核实结果页面类型；无工具用可访问搜索并标实际观察范围 |

参考文档：

- [Keyword Overview](https://docs.dataforseo.com/v3/dataforseo_labs-google-keyword_overview-live/)
- [Keyword Suggestions](https://docs.dataforseo.com/v3/dataforseo_labs-google-keyword_suggestions-live/)
- [Related Keywords](https://docs.dataforseo.com/v3/dataforseo_labs-google-related_keywords-live/)
- [Search Intent](https://docs.dataforseo.com/v3/dataforseo_labs-google-search_intent-live/)

优先已有同一结果里取得的数据，不为每个词机械调用所有端点。请求体、批次上限、支持参数和返回层级按当前端点文档或工具schema核实。不要把某页示例中的市场和产品直接照搬。

## 3. 调用与恢复

先确认产品、市场、语言和当前工作范围。发起小规模有效查询，检查HTTP或封装状态、顶层结果和各任务状态，不能把HTTP成功视为每项任务成功。保留任务ID与参数用于核对，不记录认证头。

异步任务保存已有ID并取结果，不重复提交；Live超时且是否受理未知时先核对可用任务记录或支持路径。认证错误、额度限制、访问权限问题停止相应请求，说明缺口并继续独立工作，不循环撞接口。用户未授权的充值、扩区、大规模深度或额外数据产品不自动执行。

按“端点＋规范化输入词＋市场＋语言＋引擎／设备＋指标口径＋数据时间”去重。分页用当前端点的游标或offset规则，不能把重复页当新增结果。

## 4. 字段解释

| 实际字段或指标 | 报告应如何说明 |
|---|---|
| `keyword_info.search_volume` | 对应市场口径的近似月搜索量，不是该站访问量 |
| `monthly_searches` | 返回的月度历史，保留年份月份，不当每周流量 |
| `last_updated_time` | 供应商数据更新时间，与本次查询时间分开 |
| `competition` / `competition_level` | 广告竞争指标，不当SEO难度 |
| `keyword_properties.keyword_difficulty` | DataForSEO的SEO难度估算；以实际返回层级为准，不保证排名 |
| `search_intent_info` | 供应商意图分类，必要时结合SERP与采购场景复核 |
| normalized、clickstream等搜索量 | 独立保留指标标签，不能覆盖标准字段混报 |
| null、没有返回、0 | 分别为未知或未覆盖与真实零，不相互替换 |

字段可能位于不同返回层级，如嵌套的keyword_data中。以实际响应与端点文档核对，不生搬固定JSON路径。导出数据含更新时间和参数不足时说明局限，不伪装已核验来源。

## 5. SEO应用依据

- [Google SEO入门指南](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)：围绕用户问题组织内容，关键词自然用于描述，不能承诺收录排名。
- [Google页面标题指导](https://developers.google.com/search/docs/appearance/title-link)：标题清楚、准确、各页有区别，避免重复堆词。
- [Google搜索垃圾内容政策](https://developers.google.com/search/docs/essentials/spam-policies)：不做隐藏文本、机械堆词或无价值变体页面。

这些是页面规划原则，不代表某个词已得到实际排名、流量或客户。接入和指标可用性需要运行时确认；本skill的创建不执行真实数据查询。
