# 大师云 (GuruTalk) —— 客户端产品需求文档 v2.3

> 版本说明：本版本对齐 `bibliotalk/PRD.md`（后端 v1.2）。明确 **Bibliotalk 负责数字人格 profile 的建立、维护、版本发布、检索与引用服务，但不生成回复、不调用 LLM**。同时明确引用短链 `q/{quote_id}` 为 **30 天临时引用**，并提供稳定公开分享页 `pub/{share_id}`（永久快照）。客户端/用户个人 Agent 负责调用 LLM 生成回答，并插入引用标记与短链。

---

## 1. 产品概述

**大师云 (GuruTalk)** 是一款 AI Agent 插件/客户端形态的交互入口。用户通过统一命令 `/{slug}` 进入某位“大师”的对话界面；客户端从云端 **Bibliotalk API** 拉取该人物的数字人格 profile 与检索结果；最终回答由用户个人 Agent 自主调用 LLM 生成。

首版产品目标不是做一个“云端代答助手”，而是做一个**可检索、可引用、可组合到个人 Agent 中的数字人格基础设施客户端**。

### 1.1 客户端核心职责

1. 以统一命令 `/{slug}` 启动某位人物的对话。
2. 调用 Bibliotalk 获取该人物的 profile、欢迎语与版本信息。
3. 将人物 profile 持久化到本地：`gurus/{slug}/profile.md`，保证本地可追溯、可复用、可版本化。
4. 将用户问题发送给 Bibliotalk 检索接口，获取可引用的片段结果与引用 ID。
5. 将引用 ID 映射为可点击短链：`https://bibliotalk.space/q/{quote_id}`。
6. 将 profile 与检索结果一并提供给用户个人 Agent，由其自主生成最终回答。

### 1.2 Bibliotalk 在本系统中的职责

Bibliotalk 负责：

- 建立并维护每个人物的数字人格 profile。
- 基于公有语料库完成检索与引用数据返回。
- 生成并托管引用短链页面。
- 发布 profile 版本与语料版本，供客户端同步。

Bibliotalk 不负责：

- 生成最终回答。
- 调用任何 LLM。
- 决定用户个人 Agent 的提示词、追问策略、推理策略与输出风格。
- 接收客户端本地报错信息、代码 diff 或其他运行时上下文用于“语境构建”。

### 1.3 首版产品边界

MVP 仅覆盖：

- 官方维护的公有语料库。
- 人物 profile 拉取与本地落盘。
- 基于 profile + 检索结果的个人 Agent 回答流程。
- 引用短链生成与点击查看（`/q/{quote_id}`）。
- 稳定公开分享页（`/pub/{share_id}`）。

MVP 不覆盖：

- 用户私有语料上传、入库、检索。
- Bibliotalk 侧的回答编排。
- 多人物混合对话。
- 自动追问、自动澄清、自动切换模式。

---

## 2. 用户与核心场景

### 2.1 目标用户

- 使用个人 Agent 进行学习、研究、写作或思考的人。
- 希望通过“大师”人格组织知识，而不是进行纯 roleplay 的用户。
- 对引用可追溯性有要求的用户。

### 2.2 核心使用场景

1. 用户想以某位人物的视角理解问题，但希望答案仍基于原始材料而非纯生成。
2. 用户希望在个人 Agent 中复用该人物 profile，而不是每次手写 prompt。
3. 用户希望回答中的关键判断都有可点击引用，便于复核与分享。

### 2.3 非目标场景

- 模仿式闲聊或娱乐型 roleplay。
- 无引用、无来源约束的“像某某一样说话”。
- 把 Bibliotalk 当作通用知识问答模型来直接出答案。

---

## 3. 统一交互命令与端到端流程

### 3.1 统一命令

- 查看人物目录：`/gurus`
- 进入人物对话：`/{slug}`，例如 `/elon`

### 3.2 MVP 端到端流程

1. 用户发送 `/gurus`。
2. 客户端调用 Bibliotalk `GET /v1/figures` 获取人物目录。
3. 用户输入 `/{slug}` 进入对话。
4. 客户端调用 Bibliotalk `GET /v1/figure/{slug}`。
5. Bibliotalk 返回该人物的 profile、greeting、profile_version。
6. 客户端将 profile 写入本地：`gurus/{slug}/profile.md`。
7. 客户端向用户展示 greeting，作为开场白。
8. 用户输入问题后，客户端或用户个人 Agent 调用 Bibliotalk `POST /v1/query`。
9. Bibliotalk 在该人物的官方公有语料库中检索相关片段，返回结果列表与引用 ID。
10. 客户端将引用 ID 拼接为短链 `https://bibliotalk.space/q/{quote_id}`。
11. 用户个人 Agent 基于本地 profile 与检索结果调用 LLM 生成最终回答，并在回答中插入引用标记与短链。
12. 用户点击短链时，打开 Bibliotalk 的引用卡片页 `/q/{quote_id}`；程序也可调用 `GET /v1/quote/{quote_id}` 获取引用原始数据。
13. 用户可在 `/q/{quote_id}` 页面点击“分享”，生成稳定公开分享页 `/pub/{share_id}`（即使临时引用过期，分享页仍可访问）。

### 3.3 查询时序原则

- 每次问答都应先检索，再生成回答。
- 检索结果应作为回答的主要依据，而不是可选装饰。
- 当检索结果置信度不足时，个人 Agent 应降低断言强度，必要时明确表示“当前缺少足够材料支撑”。

---

## 4. 数字人格 Profile 契约

### 4.1 设计原则

Bibliotalk 需要为每个人物建立 `Persona Profile`。该 profile 的作用是帮助客户端和用户个人 Agent 更稳定地理解“这个人是谁、重视什么、如何表达、哪些材料应优先被视作其代表性观点”。

该 profile **用于约束检索理解与个人 Agent 的回答风格参考**，但 **不用于 Bibliotalk 直接生成内容**。

### 4.2 Profile 结构

前五层由 Bibliotalk 负责构建与维护，通过 API 同步到本地，第六层由用户个人 Agent 负责记录与更新。

1. `Identity`
   核心身份简介，包括人物是谁、所处时代、主要领域与代表性标签。
2. `Mental Models`
   核心观点、思维方式、方法论、判断标准等。
3. `Expression Styles`
   语言风格，包括语气、句式、表达习惯、修辞方式等。
4. `Personality`
   性格特质与个人偏好，例如：内向/外向、感知/直觉、思考/情感、判断/知觉、果断/犹豫、直率/迂回、深度思考/快速思考等。
5. `Timeline`
   重要事件和观点的时间线，用于记述不同时期的立场和语境的演变。
6. `Adjustments`
   用户对 profile 的个人修订，在对话中由 Agent 记录到本地。

### 4.3 Profile 返回字段要求

`GET /v1/figure/{slug}` 至少应返回：

- `slug`
- `display_name`
- `greeting`
- `profile_version`
- `profile`

其中 `profile` 为结构化对象，仅包含前五层（`Identity`/`Mental Models`/`Expression Styles`/`Personality`/`Timeline`），不包含 `Adjustments`。

`profile` 对象建议字段：`identity` / `mental_models` / `expr_styles` / `personality` / `timeline`。

### 4.4 Profile 本地落盘要求

- 路径：`gurus/{slug}/profile.md`
- 客户端应保留最近一次成功同步的 `profile_version`
- `profile_version` 使用“日期+序号”的字符串，例如 `2026-04-04.1`，客户端按字典序比较即可
- 当服务端 `profile_version` 变化时，客户端应覆盖本地 profile 文件
- 本地 profile 文件应尽量保留结构化标题，便于用户查看与个人 Agent 直接复用

建议的本地文件结构：

```md
# {display_name}

- slug: {slug}
- profile_version: {profile_version}

## Identity
...

## Mental Models
...

## Expression Styles
...

## Personality
...

## Timeline
...

## Adjustments
...
```

---

## 5. API 契约（MVP）

API base URL：`https://api.bibliotalk.space`

短链 base URL：`https://bibliotalk.space/q/:quote_id`

公开分享 base URL：`https://bibliotalk.space/pub/:share_id`

### 5.1 鉴权

- 使用 Better Auth + OIDC/OAuth。
- 所有 Bibliotalk API 请求均通过 `Authorization: Bearer <ACCESS_TOKEN>` 鉴权。

### 5.2 获取人物目录

**`GET /v1/figures`**

用途：

- 获取当前可用人物列表，用于 `/gurus`。

建议返回字段：

- `slug`
- `display_name`
- `headline`
- `profile_version`

### 5.3 获取人物资料

**`GET /v1/figure/{slug}`**

用途：

- 拉取人物 profile、欢迎语与版本信息。

建议响应结构：

```json
{
  "slug": "elon-musk",
  "display_name": "Elon Musk",
  "greeting": "Ask me from first principles.",
  "profile_version": "2026-04-04.1",
   "profile": {
      "identity": "...",
      "mental_models": "...",
      "expr_styles": "...",
      "personality": "...",
      "timeline": "..."
   }
}
```

### 5.4 检索查询

**`POST /v1/query`**

用途：

- 在指定人物的官方公有语料库中检索与用户问题相关的引用片段。

请求体建议结构：

```json
{
  "figure": "elon-musk",
  "query": "first-principles thinking",
  "limit": 5
}
```

说明：`figure` 取人名的 `slug` 作为 ID。

响应体建议结构：

```json
{
  "figure": "elon-musk",
  "query": "first-principles thinking",
  "results": [
    {
      "kind": "chunk",
      "quote_id": "abc123",
      "content": "Boil things down to the fundamental truths...",
      "source_title": "The Book of Elon",
      "source_type": "book",
      "source_url": null,
      "locator": "Chapter 2",
      "published_at": "2025-01-01",
      "score": 0.91
    },
    {
      "kind": "memory",
      "memory": "Elon 强调用第一性原理把问题拆到最基本事实，再从零推导。",
      "score": 0.86
    }
  ]
}
```

字段说明：

- `kind="chunk"`：可展示的原文片段，服务端会分配 `quote_id`，可用于 `/q/{quote_id}` 与后续分享。
- `kind="memory"`：从语料中抽取/归纳的记忆条目，不分配 `quote_id`，仅用于补充 Agent 上下文，不作为“原文引用”。
- `score`：服务端返回的相关度分数（已按来源权重加权并重排；权重本身不对外暴露）。
- `results` 仅返回检索结果与元数据，不返回任何生成答案。

### 5.5 引用详情

**`GET /v1/quote/{quote_id}`**

用途：

- 获取某条引用的原始内容与展示所需元数据。

至少应返回：

- `quote_id`
- `content`
- `source_title`
- `source_type`
- `locator`
- `published_at`
- `figure`

---

## 6. 引用系统要求

### 6.1 引用原则

- 回答中的关键判断默认应附带引用，除非问题极轻或当前没有足够高置信度材料。
- 引用应优先服务于“可复核”，其次才是“可分享”。
- 没有足够可靠材料时，不应强行拼接引用。

### 6.2 生命周期

- `quote_id` 对应临时引用短链：`https://bibliotalk.space/q/{quote_id}`。
- 服务端会将临时引用以 `q:{quote_id}` 写入 Cloudflare KV，并设置 **30 天 TTL**；过期后 `/q/{quote_id}` 会返回“引用不存在”。
- 用户在 `/q/{quote_id}` 页面点击“分享”后，服务端会生成稳定公开分享链接：`https://bibliotalk.space/pub/{share_id}`，并将 **完整 quote snapshot** 写入 `pub:{share_id}`（不设置过期），用于保证临时引用过期后依然可访问。

### 6.3 客户端行为要求

- 客户端不得自行伪造引用 ID。
- 客户端应直接使用服务端返回的 `quote_id` 拼接短链。

---

## 7. 客户端本地数据与状态管理

### 7.1 本地数据结构

- `gurus/{slug}/profile.md`

首版本地只要求持久化人物 profile，不要求持久化完整检索历史。
需要将后端返回的 profile 与用户本地的 `Adjustments` 进行拼接组成 profile.md。

### 7.2 状态要求

客户端至少需要维护以下运行时状态：

- 当前激活人物 `slug`
- 当前已加载的 `profile_version`
- 当前问答轮次使用的检索结果
- 当前引用列表及对应短链

### 7.3 同步规则

- 首次进入 `/{slug}` 时必须拉取服务端 profile。
- 若本地已有 profile，仍应通过 `GET /v1/figure/{slug}` 检查版本是否更新。

---

## 8. 失败处理与降级策略

### 8.1 人物不存在

- 若 `GET /v1/figure/{slug}` 返回不存在，客户端应提示该人物当前不可用。

### 8.2 Profile 拉取失败

- 若首次拉取失败，客户端不应进入该人物对话。
- 若本地已有旧版 profile 且用户明确接受，可在后续版本考虑“使用缓存继续”，但不属于首版必做。

### 8.3 检索无结果

- 若 `POST /v1/query` 返回空结果，客户端应明确告知“当前未检索到足够相关材料”。
- 用户个人 Agent 在这种情况下应避免输出看似有依据的强断言。

### 8.4 引用不存在或已过期

- 若用户点击 `https://bibliotalk.space/q/{quote_id}` 返回“引用不存在”，客户端应提示该引用可能已过期（30 天 TTL）或无效。
- 建议的用户引导：优先将引用在引用页生成 `/pub/{share_id}`（稳定公开页）后再传播；或重新检索生成新的引用。
- 若用户访问 `/pub/{share_id}` 返回不存在，客户端应提示该分享链接无效或已被移除，并建议重新从新的引用页生成分享链接。

---

## 9. MVP 验收标准

MVP 至少满足：

1. 用户可通过 `/gurus` 获得可用人物目录。
2. 用户可通过 `/{slug}` 拉取人物 profile，并在本地生成 `gurus/{slug}/profile.md`。
3. 用户发问后，客户端可调用 `POST /v1/query` 获得检索结果。
4. 用户个人 Agent 可基于 profile 与检索结果生成回答，并插入 Bibliotalk 短链。
5. 用户点击短链后，若引用未过期（30 天 TTL），可看到对应引用卡片页 `/q/{quote_id}`。
6. 用户可在引用卡片页生成稳定分享链接 `/pub/{share_id}`，并可长期访问分享页内容。
7. 当人物不存在、检索无结果、引用不存在或已过期、分享链接不存在时，客户端行为明确且不误导用户。

---

## 10. 配置与启动

- 环境变量：`BIBLIOTALK_API_TOKEN`
- 客户端启动后应支持 `/gurus` 与 `/{slug}` 两类入口命令

---

## 11. MVP 之后备忘

以下内容不属于首版交付范围，但需要在后续版本考虑：

- 用户私有语料上传与检索
- 公有语料与私有语料的混合检索
- 私有语料的权限隔离与身份模型
- 引用链接续期策略
- profile 的用户个性化修订机制
