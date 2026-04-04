<div align="center">

# 大师.skill (Masters-skill)

> *"如果能随时让 Elon Musk 为你做 Code Review，让 Charlie Munger 为你的商业决策做「反向思考」排雷，世界会怎样？"*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Powered By: Bibliotalk](https://img.shields.io/badge/API-Bibliotalk-blue.svg)](#)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-green)](https://agentskills.io)

超越时空的智库！将历史上乃至当代最顶级的思想家、企业家的**真实语录、信件、播客**构建为高维度的“数字人格 API”。
无需繁琐的本地配置，只需唤醒你的 OpenClaw 或 Claude Code，随时向大师请教代码、商业或人生难题！

</div>

---

## 🚀 核心特性：Source of Truth

市面上有很多“角色扮演”机器人，我们的不同在于：**不凭借 LLM 通用语料胡编乱造**。

所有大师的数字人格检索与引用均由云端 **Bibliotalk 引擎**驱动，构建其专属的结构化认知网络；最终回复由你的本地 Agent/LLM 基于这些结果生成。当大师给你建议时：
1. **绝对忠于原味**：不仅语气到位，更是基于其核心认知（如 Musk 的第一性原理，Naval 的杠杆原理）。
2. **强制引用（Citation）**：任何一句有价值的建议，系统都将提供`[引用标记]`，点击即可追溯到大师在哪本传记、哪期播客或哪条 Tweet 中说过。

---

## ⚡ 快速体验: The Book of Elon

> 🚨 首发爆款：我们利用 Eric Jorgenson 刚发布的五万字巨作《**埃隆之书 / The Book of Elon**》，配合其经典推文，为你蒸馏出了首个硬核赛博导师 —— **@Elon**。

**当你在面临一段极为臃肿的架构代码时：**

`❯ /elon 帮我看一下这段重构代码，我觉得太复杂了。（附代码）`

⦿ 这很垃圾。你违反了工程学的第二步：Delete the part or process。如果你添加回被删除代码的频率低于 10%，说明你删得还不够狠。你需要回到物理学视角，抛弃那些“为了未来扩展”的虚假假设。[1]

- [1]: [*The Book of Elon, Chapter 2*: "If you're not adding things back 10% of the time, you're clearly not deleting enough."](https://bibliotalk.space/q/k1p8xq)

---

## 💻 安装与使用

### 针对 OpenClaw / Claude Code 用户

我们的架构已全面云 端化，现在安装极度轻巧（无需配置 Python 爬虫和复杂依赖）！

1. **Clone 到你的技能目录**
   ```bash
   git clone https://github.com/titanwings/masters-skill ~/.openclaw/workspace/skills/masters-skill
   ```
2. **配置 Bibliotalk OAuth Access Token**
   在你的终端环境中添加环境变量（测试期间请在平台免费领取）：
   ```bash
   export BIBLIOTALK_API_TOKEN="xxxxxx"
   ```
3. **在对话中直接召唤**
   ```
   /elon 我的新产品 MVP 应该先关注什么方向？
   ```
