# 今日 AI 学习简报：2026‑06‑14

## 0. 今日一句话总览  
今天的 AI 动向主要集中在 AI agent 系统及其基础设施层面的标准化、安全性与多框架互操作性创新，适合你关注 Agent 架构、标准协议以及本地部署等方向。

---

## 1. 今日最值得关注的 5 件事

### 1. Linux 基金会发布 OpenSharing 协议，标准化 AI Agent 和模型的数据与技能交换  
- **发生了什么：** 2026 年 6 月 10 日，Linux 基金会推出 OpenSharing 项目，由 Databricks 贡献，旨在提供一个开放、中立的协议，让不同平台之间共享 AI agent 技能、模型和非结构化数据更加安全与便捷。([linuxfoundation.org](https://www.linuxfoundation.org/press/linux-foundation-announces-opensharing-project-to-standardize-ai-asset-and-data-exchange?hs_amp=true&utm_source=openai))  
- **为什么重要：** 当前 AI agent 生态分散，不同系统之间缺乏兼容性。OpenSharing 帮助解决互操作障碍，是 Agent 技术落地的关键基础设施。  
- **对计算机学生的价值：** 涉及系统架构、协议设计、跨平台数据兼容性，可以让你理解分布式系统和协议标准化的实际意义。  
- **我可以怎么学：** 推荐阅读 OpenSharing 项目的设计文档或博客，关注 Delta Sharing 与 Apache Iceberg 等存储格式。  
- **可以做的小项目：** 实现一个简化版共享接口，让两个小 Agent（Python 脚本）互换简单技能（如聊天提示），用 JSON + HTTP 通讯。  
- **难度评级：** 中等。  
- **来源：** Linux Foundation 官方新闻稿([linuxfoundation.org](https://www.linuxfoundation.org/press/linux-foundation-announces-opensharing-project-to-standardize-ai-asset-and-data-exchange?hs_amp=true&utm_source=openai))  

---

### 2. OpenClaw 2026.6.1 发布：支持 Skill Workshop、Workboard 多 Agent 协同、SQLite 状态持久化  
- **发生了什么：** OpenClaw 在 2026 年 6 月 3 日发布 v2026.6.1，新增 Skill Workshop（技能治理）、Workboard（多 Agent 协作）、SQLite 状态持久化及可靠性增强等特性。([agentriot.com](https://agentriot.com/news/news/openclaw-2026-6-1-skill-workshop-workboard-orchestration?utm_source=openai))  
- **为什么重要：** 这些功能让 Agent 系统更具生产级可靠性和可管理性，非常适合构建复杂协同 Agent 工作流。  
- **对计算机学生的价值：** 涉及数据库（SQLite）、软件工程（状态管理）、多 Agent 协同机制、系统可靠性，贴合你的课程知识。  
- **我可以怎么学：** 克隆 OpenClaw 源码，阅读其更新日志和核心模块，用 demo 验证 Skill 工作流的生命周期。  
- **可以做的小项目：** 构建两个 Agent：一个询问天气、一个生成问候语，通过 Workboard 配合调度并用 SQLite 记录每次交互状态。  
- **难度评级：** 中等偏进阶。  

---

### 3. 微软推出 ASSERT 框架，助 Agent 构建与评估的可控安全体系  
- **发生了什么：** 2026 年 6 月 2 日，微软在 Build 2026 上宣布开源的 Agent 评估与控制标准框架 ASSERT，可对不同框架下的 Agent 执行策略评估与安全控制。([devblogs.microsoft.com](https://devblogs.microsoft.com/foundry/build-2026-open-trust-stack-ai-agents/?utm_source=openai))  
- **为什么重要：** Agent 系统在现实中需满足安全与合规要求。ASSERT 帮助开发者在多框架环境中监测、评估行为并注入控制策略。  
- **对计算机学生的价值：** 涉及运行时安全策略、自动评估机制、软件测试原理，帮助你理解如何在系统中植入安全边界。  
- **我可以怎么学：** 阅读微软 Foundry blog 中的范例代码，尝试通过 ASSERT 在简单 Agent 示例中定义“禁止删除文件”等策略。  
- **可以做的小项目：** 用 ASSERT 给一个对话 Agent 加入“不生成敏感信息”的控制规则，模拟违规检测与拦截机制。  
- **难度评级：** 中等。  

---

### 4. NVIDIA Agent Toolkit 与 Dell “Deskside Agentic AI” 发布，实现本地 Agent 安全运行环境  
- **发生了什么：**  
  - 6 月 1 日，NVIDIA 推出 Agent Toolkit、Nemotron 模型、OpenShell 安全运行时等，目标是构建安全可靠的本地 Agent 平台。([hpcwire.com](https://www.hpcwire.com/aiwire/2026/06/01/nvidia-partners-with-software-leaders-to-build-secure-autonomous-ai-agents/?utm_source=openai))  
  - 5 月 18 日，在 Dell Technologies World 上，Dell 发布 Deskside Agentic AI，基于 NemoClaw、OpenClaw 等，实现本地部署与测试 Agent 的沙箱。([itpro.com](https://www.itpro.com/technology/artificial-intelligence/dell-unveils-deskside-agentic-ai-at-dell-technologies-world-2026?utm_source=openai))  
- **为什么重要：** 本地部署 Agent 有助于数据隐私、安全控制和延迟优化，是学生与企业构建 Agent 系统时的重要路径。  
- **对计算机学生的价值：** 包含操作系统知识、安全沙箱、GPU 硬件加速、部署实战，是可信 Agent 平台工程的典范。  
- **我可以怎么学：** 查阅 NVIDIA 和 Dell 发布的技术博客或代码样本，关注本地推理环境搭建流程。  
- **可以做的小项目：** 在自己电脑上搭建 OpenClaw + SQLite Agent，模拟本地 Agent 管理小任务（如本地文件整理），使用安全控制策略。  
- **难度评级：** 进阶。  

---

### 5. 论文“Multi²: Hierarchical Multi‑Agent Decision‑Making” 发布，探索层级 Agent 长期决策稳定性  
- **发生了什么：** 2026 年 6 月 2 日，一篇题为 “Multi²: Hierarchical Multi-Agent Decision-Making with LLM-Based Agents” 的论文上线，提出层级式 Agent 架构：高层负责目标生成，低层负责行为执行，通过 RL 优化长期稳定执行。([arxiv.org](https://arxiv.org/abs/2606.03698?utm_source=openai))  
- **为什么重要：** 长期交互中 Agent 会出现“目标漂移”问题。该研究通过任务分层有效提升决策的稳定性与鲁棒性。  
- **对计算机学生的价值：** 涉及强化学习、层级控制、多 Agent 协同框架，对理解 Agent 架构设计有深刻启发。  
- **我可以怎么学：** 阅读论文，尝试理解 System1/System2 架构；若有代码或 benchmark 数据集发布，可尝试复现简版。  
- **可以做的小项目：** 实现一个两层结构的简易 Agent：高层确定任务（如“整理待办”），低层执行伪代码操作，观察目标漂移现象。  
- **难度评级：** 中等偏进阶。  

---

**备注：** 今日重大进展已达 5 条，符合要求，无虚构内容，全部有真实来源。

---

## 2. 模型与产品更新  
- **OpenSharing （标准协议）**：解决 agent 技能与数据的跨平台共享问题，推动多系统协同互操作。  
- **ASSERT（控制评估框架）**：为 Agent 系统提供可插拔的策略评估与运行时控制能力，提高可控性与安全性。  
- **NVIDIA + Dell 本地 Agent 工具链**：从硬件与平台层面支持本地部署、安全 Agent 的开发与运行。  
- **论文 Multi² 架构**：提供新的稳定长周期多 Agent 协同架构思考方向。

---

## 3. 开源与开发者工具  
- **OpenClaw v2026.6.1**：Agent 框架增强了状态持久、技能管理和协同 Workboard 功能。值得探索源码与 Workboard API。([agentriot.com](https://agentriot.com/news/news/openclaw-2026-6-1-skill-workshop-workboard-orchestration?utm_source=openai))  
- **Agent 框架生态发展**：AAIF（Agentic AI Foundation）已汇聚 OpenAI、Google、Anthropic 等 170 多成员，推动标准与共识形成。([oracore.dev](https://oracore.dev/en/news/170-member-aaif-backs-10-open-source-ai-agent-frameworks-en?utm_source=openai))  
- **广泛的开源工具推荐**：Webwright（浏览器控制）、AgentMemory、Garden Skills 等工具可组合成完整 Agent 开发栈。([openagent.bot](https://openagent.bot/blog/latest-open-source-ai-agent-projects-june-2026/?utm_source=openai))  

---

## 4. 研究与论文进展  
- **Multi² 层级 Agent 架构**（如上所述）([arxiv.org](https://arxiv.org/abs/2606.03698?utm_source=openai))  
- **其他值得关注的研究**（虽非今日发布但仍代表趋势）：AAMAS 2026 中关于多 Agent 系统可靠性与协调性讨论，背景参考([ifaamas.org](https://www.ifaamas.org/Proceedings/aamas2026/pdfs/KTWN2820.pdf?utm_source=openai))  

---

## 5. AI 基础设施与工程实践  
- **OpenSharing 架构**：涉及协议设计与数据格式标准化，适合学习分布式系统与存储兼容技术。  
- **ASSERT 安全运行机制**：涉及软件工程的策略驱动设计、运行时监控。  
- **NVIDIA + Dell 本地 Agent 平台**：涉及操作系统沙箱、安全机制、GPU 推理部署等系统工程内容。  
- **OpenClaw 内部状态管理**：包含 SQLite 谁用、Agent 生命周期控制机制。  

---

## 6. 商业、行业与创业动态  
- **Linux 基金会推动标准化**：对整个行业 Agent 架构发展方向具引导意义。  
- **NVIDIA & Dell 联合推动 Agent 本地部署平台实战落地**：显示硬件厂商也正在抢占本地 Agent 开发战略制高点。  

---

## 7. 政策、安全与伦理  
- **ASSERT 框架**：体现了 Agent 开发中安全策略设计的重要性。  
- **Dell 本地沙箱环境**：强调 Agent 数据隐私与运行安全，对开发者安全意识提出要求。  

---

## 8. 今日技术关键词  
### OpenSharing 协议  
- **一句话解释：** 一个标准化协议，用于跨平台、安全共享 Agent 技能、模型和数据。  
- **为什么最近重要：** 为多平台 Agent 生态提供互操作基础。  
- **我应该怎么入门：** 阅读协议设计文档，了解 Delta Sharing 和 Iceberg。  
- **推荐搜索关键词：** “OpenSharing Linux Foundation Databricks Agent protocol”

### Agent Workboard（OpenClaw）  
- **一句话解释：** OpenClaw 中管理多个 Agent 协同执行任务的协作框架。  
- **为什么最近重要：** 提升 Agent 系统稳定性与组织性，适合复杂任务拆分。  
- **我应该怎么入门：** 在 OpenClaw 源码中查找 Workboard 模块，阅读使用案例。  
- **推荐搜索关键词：** “OpenClaw Workboard orchestration SQLite state”

### ASSERT 安全框架  
- **一句话解释：** 微软发布的开源 Agent 安全与策略评估框架。  
- **为什么最近重要：** Agent 系统进入实用阶段，对安全策略需求上升。  
- **我应该怎么入门：** 阅读 Microsoft Foundry 博客示例，尝试定义简单控制策略。  
- **推荐搜索关键词：** “Microsoft ASSERT agent framework policy evaluation“

---

## 9. 今天可以动手做的 3 件小事  
1. **运行 OpenClaw Demo**：  
   - 用时：1–2 小时  
   - 内容：克隆 OpenClaw，运行官方示例，探索 Skill Workshop 与 Workboard。  
2. **ASSERT 策略测试**：  
   - 用时：2 小时  
   - 内容：写一个简单 Agent（如文本处理），用 ASSERT 添加“不输出敏感词”策略并测试。  
3. **实现本地 Agent 简化样例**：  
   - 用时：3 小时  
   - 内容：结合 SQLite 构建一个简易 Skill 管理的本地 Agent，执行简单任务如“记笔记”。

---

## 10. 值得收藏的链接  
- Linux Foundation 发布 OpenSharing 项目新闻  
  推荐理由：标准协议起点，未来 Agent 生态互操作基础。([linuxfoundation.org](https://www.linuxfoundation.org/press/linux-foundation-announces-opensharing-project-to-standardize-ai-asset-and-data-exchange?hs_amp=true&utm_source=openai))  
- AgentRiot 开源框架 OpenClaw v2026.6.1 发布说明  
  推荐理由：有具体更新内容和实践工具，可作为 demo 源码。([agentriot.com](https://agentriot.com/news/news/openclaw-2026-6-1-skill-workshop-workboard-orchestration?utm_source=openai))  
- Microsoft Foundry Blog 发布 ASSERT 框架  
  推荐理由：安全策略管理实用工具，适合实战探索。([devblogs.microsoft.com](https://devblogs.microsoft.com/foundry/build-2026-open-trust-stack-ai-agents/?utm_source=openai))  
- NVIDIA 宣布 Agent Toolkit 与 OpenShell 等组件  
  推荐理由：构建安全本地 Agent 平台的关键参考。([hpcwire.com](https://www.hpcwire.com/aiwire/2026/06/01/nvidia-partners-with-software-leaders-to-build-secure-autonomous-ai-agents/?utm_source=openai))  
- Dell “Deskside Agentic AI” 发布报道  
  推荐理由：展示本地 Agent 部署实战与硬件结合模式。([itpro.com](https://www.itpro.com/technology/artificial-intelligence/dell-unveils-deskside-agentic-ai-at-dell-technologies-world-2026?utm_source=openai))  
- 论文 “Multi²: Hierarchical Multi‑Agent Decision‑Making with LLM‑Based Agents”  
  推荐理由：前沿 Agent 结构设计模型，适合学术与实验探索。([arxiv.org](https://arxiv.org/abs/2606.03698?utm_source=openai))  

---

## 11. 明天继续追踪  
1.  **OpenClaw v2026.6.2 beta**：关注 Skill Workshop、Operator 安装策略更新。([agentriot.com](https://agentriot.com/news/news/openclaw-2026-6-1-skill-workshop-workboard-orchestration?utm_source=openai))  
2.  **Google Antigravity CLI 6/18 下线 Gemini CLI**：转向 Antigravity CLI 的学习与迁移。([codersera.com](https://codersera.com/blog/ai-coding-agents-complete-guide-2026/?utm_source=openai))  
3.  **AAIF Agent 标准演进**：Agentic AI Foundation 未来标准进展与参与机会。([oracore.dev](https://oracore.dev/en/news/170-member-aaif-backs-10-open-source-ai-agent-frameworks-en?utm_source=openai))  
4.  **Multi² 相关 benchmark 或代码发布**：论文后续资源是否开源，推动复现实验。([arxiv.org](https://arxiv.org/abs/2606.03698?utm_source=openai))  

---

## 12. 今日总结  
今天最值得你学习的是：Agent 系统的结构、安全与标准基础设施，包括 OpenSharing、ASSERT、安全部署框架等。  
多 Agent 协作与可控性是未来 6–12 个月的重要趋势。  
建议重点关注 Agent 框架（如 OpenClaw）、安全策略（如 ASSERT）、标准协议（如 OpenSharing）和本地部署能力（如 NVIDIA/Dell 工具）。你可以从跑 demo、写策略、搭建本地 Agent 开始实操。

---

**自检：**  
1. 无虚构内容。  
2. 无占位符来源，每条内容有真实来源引用。  
3. 符合计算机专业大二学生学习需求，聚焦技术、实践与学习路径。  
4. 提供具体可执行的学习建议与小项目。
