# 大师.skill (Masters-skill) —— 客户端产品需求文档 v2.1

> 版本说明：本版本明确 **Bibliotalk 仅提供检索与引用服务，不生成回复、不调用 LLM**。客户端/用户个人 Agent 负责调用 LLM 生成回答并插入引用标记与短链。

---

## 1. 产品概述

**大师.skill (Masters-skill)** 是一款 AI Agent 插件/客户端形态的交互入口：用户用 `/{slug}` 进入某位“大师”的对话界面；客户端向云端 **Bibliotalk API** 获取该人物的画像与检索结果；**回答的生成** 由用户个人 Agent 自主调用 LLM 完成（不属于 Bibliotalk 的职责）。

### 1.1 客户端核心职责

1. 以统一命令 `/{slug}` 启动该人物对话，并拉取该人物 profile。
2. 将人物 profile 持久化到本地：`masters/{slug}/profile.md`（格式参考仓库内的 `SKILL.md` 的“写入文件”思想：本地可追溯、可复用、可版本化）。
3. 将用户问题发送至 Bibliotalk 的检索接口，获取可引用的片段结果与引用 ID。
4. 生成并展示引用短链：`https://bibliotalk.space/q/{id}`（短链点击后打开引用卡片页）。

### 1.2 明确非职责

- 客户端 **不** 将本地报错信息、代码 diff 等“上下文”发送给 Bibliotalk 做“语境构建”。
- Bibliotalk **不** 生成回复、**不** 调用 LLM、**不** 负责追问/模式切换等对话编排。
- “追问”“推测”等对话策略如果存在，只能发生在用户个人 Agent（其调用的 LLM）一侧；本 PRD 暂不覆盖。

---

## 2. 统一交互命令与用户流程

### 2.1 统一命令

- 进入对话：`/{slug}`（示例：`/elon-musk`）

### 2.2 端到端流程（MVP）

1. 用户发送 `/list-masters` 调用 Bibliotalk `GET /v1/figures` API 获取人物目录。
2. 用户输入 `/{slug}` 触发对话（例如 `/elon-musk`）。
3. 客户端调用 Bibliotalk：`GET /v1/figure/{slug}`，获得 profile、greeting、version 等信息。
   - 将返回的 profile 写入本地并加入上下文：`masters/{slug}/profile.md`
   - 将greeting作为开场白回复给用户
4. 用户开始对话；每次用户输入问题后，Agent 调用 Bibliotalk API：`GET /v1/query?figure={slug}&q={q}`
5. Bibliotalk 检索 supermemory，返回相关 chunk/memory 片段（每条携带引用 ID：`quote_id`）。
6. 客户端将 `quote_id` 变为短链：`https://bibliotalk.space/q/{quote_id}`（对应 `GET /q/{id}`），并把短链提供给用户个人 Agent。
7. 用户个人 Agent 自行调用 LLM 生成回答，并在回答文本中插入 `[引用标记]` 与短链（例如 `[1] [title, chapter/section/timestamp](https://bibliotalk.space/q/abcde)`）。
8. 用户点击短链时打开引用页：`https://bibliotalk.space/q/{quote_id}`（由 Bibliotalk 渲染引用卡片页。程序也可通过 API `GET /v1/quote/{id}` 获取原始数据）。

---

## 3. 客户端本地数据结构（MVP）

### 3.1 Profile 落盘

- 路径：`masters/{slug}/profile.md`
- 目标：让“人物画像”在本地可查看、可复用（例如用于提示用户个人 Agent：该人物的口吻、关注点、禁忌等）。

---

## 4. 配置与启动

- 用户只需配置环境变量 `BIBLIOTALK_API_KEY` 用于访问 Bibliotalk API。
