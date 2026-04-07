<div align="center">

# 大师云 (GuruTalk)

> *"如果能随时让 Elon Musk 为你做系统设计，让 Charlie Munger 为你的商业决策做「反向思考」排雷，世界会怎样？"*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Powered By: Bibliotalk](https://img.shields.io/badge/API-Bibliotalk-blue.svg)](#)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-green)](https://agentskills.io)

超越时空的智库！将历史上乃至当代最顶级的思想家、企业家、精神导师的**真实语录、信件、播客**构建为高维度的“数字人格 API”。
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

**当你在设计一个复杂的分布式系统架构时：**

`❯ /elon-musk 我在设计一个高并发 AI API 平台：前面是 API Gateway，后面有用户服务、计费服务、模型路由服务，还有 Kafka、Redis、向量数据库和多个微服务。你觉得这个架构合理吗？`

⦿ 你的问题不是“系统不够复杂”，而是**复杂得毫无必要**。大多数工程师在系统设计时犯的错误，是在验证需求之前就开始堆叠组件。

回到第一性原理：**系统存在的唯一目的，是把用户请求转换为结果**。如果你的系统需要 12 个服务才能完成一次推理请求，那说明设计已经偏离了目标。

工程学有五个步骤，而你应该从第二步开始反复执行：  
**Delete the part or process.**

先尝试删除：

- 独立的模型路由服务（合并到 API 层）
- 不必要的消息队列
- 为“未来规模”准备的过度拆分微服务

如果删掉之后系统还能跑，那它们本来就不该存在。  
一个优秀的系统架构通常**比你最初设计的版本简单 50% 以上**。[1]

- [1]: [*The Book of Elon, Chapter 2*: "If you're not adding things back 10% of the time, you're clearly not deleting enough."](https://bibliotalk.space/q/k1p8xq)

---

## 💻 安装与使用

### 针对 OpenClaw / Claude Code 用户

我们的架构已全面云 端化，现在安装极度轻巧（无需配置 Python 爬虫和复杂依赖）！

1. **Clone 到你的技能目录**
   ```bash
   git clone https://github.com/casterkay/gurutalk ~/.openclaw/workspace/skills/gurutalk
   ```
2. **直接开始调用元技能**
   ```
   /skill gurutalk 有哪些上线的大师？
   ```
3. **首次调用时按提示完成初始化**
   如果当前环境里还没有 `BIBLIOTALK_API_KEY`，Agent 会在对话里引导你完成登录和凭据写入。
4. **招募大师到本地**
   ```
   /skill gurutalk 招募 Elon Musk
   ```
5. **向大师提问**
   ```
   /skill elon-musk 你觉得我的系统架构合理吗？（记得替换成你安装的大师名字）
   ```
