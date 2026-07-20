# 今日 AI 学习简报：2026‑07‑20

## 0. 今日一句话总览
今天没有发生发生在 2026‑07‑20 的重大 AI 行业新闻。近期围绕 AI Agent 的多项技术进展集中在 5 月至 6 月。鉴于今日无新动态，以下内容主要回顾过去 24–36 小时内仍有重要后续或具有持续学习价值的进展。

---

## 1. 今日最值得关注的 5 件事
今日未发现发生在**2026‑07‑20**或过去 24 小时内的重大事件。近期较为重要的变化仍集中在 5–6 月份，以下列举最具实质意义且适合深入学习的内容：

### 1. Microsoft Agent Framework 正式发布与 CodeAct 插件加速
- **发生了什么：** Microsoft 在 BUILD 2026 正式推广其开源 Agent Framework（MAF），并推出 CodeAct 插件，使 Agent 可以将多步工具调用合并成一段 Python 代码执行，显著提升执行效率([devblogs.microsoft.com](https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-at-build-2026-announce/?utm_source=openai))。
- **为什么重要：** CodeAct 性能提升明显（延迟减半，token 使用减少约 64%），对于构建高效 Agent 系统具备实际意义([devblogs.microsoft.com](https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-at-build-2026-announce/?utm_source=openai))。
- **对计算机学生的价值：** 涉及编程语言（Python/.NET）、操作系统隔离机制（微 VM）、多 Agent 调度、性能优化等知识。
- **我可以怎么学：** 阅读 MAF 文档，尝试运行 CodeAct 示例；了解 Hyperlight 微 VM 原理；比较传统工具调用与 CodeAct 的差异。
- **可以做的小项目：**  
  - 项目名称：CodeAct 工具链比较  
  - 最小版本：实现一个简单 Agent 调用多个工具并对比传统与 CodeAct 的响应速度与 token 使用  
  - 需要技术：Python、Agent Framework、基本性能测量  
  - 预计耗时：4–6 小时  
  - 学到：Agent 性能优化、API 调用封装  
- **难度评级：** 中等  
- **来源：** Microsoft 官方博客 ([devblogs.microsoft.com](https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-at-build-2026-announce/?utm_source=openai))

---

### 2. Microsoft 发布 ASSERT：Agent 安全评估框架
- **发生了什么：** Microsoft 在 BUILD 2026 推出 ASSERT——一个开源的 policy‑driven 的 Agent 运行时评估与安全控制框架，适用于任何 Agent 架构([devblogs.microsoft.com](https://devblogs.microsoft.com/foundry/build-2026-open-trust-stack-ai-agents/?utm_source=openai))。
- **为什么重要：** 安全评估和策略控制是 Agent 系统从 demo 向生产环境迈进的核心痛点，ASSERT 提供了统一、安全的解决方案([devblogs.microsoft.com](https://devblogs.microsoft.com/foundry/build-2026-open-trust-stack-ai-agents/?utm_source=openai))。
- **对计算机学生的价值：** 涉及政策驱动、安全策略、运行时监控、Agent 行为验证等系统设计知识。
- **我可以怎么学：** 探索 ASSERT 官网文档，了解如何编写 policy；在已有 Agent 示例中加入 ASSERT 评估机制。
- **可以做的小项目：**  
  - 项目名称：Agent 安全策略演练  
  - 最小版本：定义简单策略（如工具调用次数限制），让 Agent 在违反策略时触发警告  
  - 技术：Python、Agent Framework、ASSERT（policy 写法）  
  - 预计耗时：3–5 小时  
  - 学到：策略评估、安全监控机制  
- **难度评级：** 中等  
- **来源：** Microsoft Foundry 博客 ([devblogs.microsoft.com](https://devblogs.microsoft.com/foundry/build-2026-open-trust-stack-ai-agents/?utm_source=openai))

---

### 3. Linux Foundation 推出 Agent Name Service（ANS）身份标准
- **发生了什么：** Linux Foundation 宣布计划推出 Agent Name Service（ANS），使用 DNS 架构为 AI Agent 提供去中心化身份认证及发现机制([linuxfoundation.org](https://www.linuxfoundation.org/press/linux-foundation-announces-intent-to-launch-agent-name-service-to-establish-trusted-identity-infrastructure-for-ai-agents?hs_amp=true&utm_source=openai))。
- **为什么重要：** Agent 身份验证和发现是整个 agentic 生态可信运行的基础，标准化有助于避免 shadow Agent 漏洞并增强可治理性([linuxfoundation.org](https://www.linuxfoundation.org/press/linux-foundation-announces-intent-to-launch-agent-name-service-to-establish-trusted-identity-infrastructure-for-ai-agents?hs_amp=true&utm_source=openai))。
- **对计算机学生的价值：** 涉及网络协议（DNS）、分布式系统、安全机制、身份验证等知识点。
- **我可以怎么学：** 学习 DNS 基础与扩展机制；阅读 ANS 规范草案；实验设计一个 Agent 注册与解析服务。
- **可以做的小项目：**  
  - 项目名称：简易 Agent DNS 注册系统  
  - 最小版本：模拟 Agent 使用自定义子域名进行注册、查询与验证  
  - 技术：Python、DNS 库（dnspython）、网络 API  
  - 预计耗时：6–8 小时  
  - 学到：DNS 操作、身份注册、Agent 探索机制  
- **难度评级：** 中等偏进阶  
- **来源：** Linux Foundation 公告 ([linuxfoundation.org](https://www.linuxfoundation.org/press/linux-foundation-announces-intent-to-launch-agent-name-service-to-establish-trusted-identity-infrastructure-for-ai-agents?hs_amp=true&utm_source=openai))

---

### 4. Google Agent Executor：分布式 Agent 运行时开源
- **发生了什么：** Google 发布 Agent Executor，这是一个用于 Agent 长流程执行、挂起恢复以及分布式部署的开源运行时标准([cloud.google.com](https://cloud.google.com/blog/products/ai-machine-learning/agent-executor-googles-distributed-agent-runtime?utm_source=openai))。
- **为什么重要：** Agent 在长运行任务中的稳定性、恢复能力是提升 Agent 可用性的关键，Agent Executor 提供了可靠解决方案。
- **对计算机学生的价值：** 包括分布式计算、容错设计、任务调度、系统可靠性等系统知识。
- **我可以怎么学：** 查阅文档，理解断点恢复机制；下载并运行样例部署本地 Agent；测试故障恢复能力。
- **可以做的小项目：**  
  - 项目名称：Agent Executor 异常恢复演示  
  - 最小版本：实现一个简单 Agent 在中途故障时恢复运行状态  
  - 技术：Python、Agent Executor、任务状态持久化  
  - 预计耗时：4–6 小时  
  - 学到：分布式任务可靠运行与恢复机制  
- **难度评级：** 中等  
- **来源：** Google Cloud 官方博客 ([cloud.google.com](https://cloud.google.com/blog/products/ai-machine-learning/agent-executor-googles-distributed-agent-runtime?utm_source=openai))

---

### 5. NIST 启动 AI Agent 标准化倡议
- **发生了什么：** 美国 NIST 通过 CAISI 推出 “AI Agent Standards Initiative”，旨在推动 agent 可互操作、安全认证与标准协议的建立([nist.gov](https://www.nist.gov/news-events/news/2026/02/announcing-ai-agent-standards-initiative-interoperable-and-secure?utm_source=openai))。
- **为什么重要：** 国家级标准化对于 Agent 技术应用的规范、安全与普及具有深远意义。
- **对计算机学生的价值：** 涉及政策导向、安全标准、协议设计、标准组织运作等内容。
- **我可以怎么学：** 阅读 NIST 发布的倡议文档与 RFI 内容；关注后续标准草案与公开征询结果。
- **可以做的小项目：**  
  - 项目名称：“Agent Standards 学习报告”  
  - 最小版本：撰写一页总结 NIST Agent Standards Initiative 的目标与当前进展  
  - 技术：文档阅读、报告写作  
  - 预计耗时：2–3 小时  
  - 学到：标准制定流程与安全需求理解能力  
- **难度评级：** 入门  
- **来源：** NIST 官方新闻稿 ([nist.gov](https://www.nist.gov/news-events/news/2026/02/announcing-ai-agent-standards-initiative-interoperable-and-secure?utm_source=openai))

---

## 2. 模型与产品更新
近期无发生在今日的模型发布，但 Google 在 I/O 期间推出了 Antigravity agent 开发平台的新功能，包括 Antigravity 2.0 应用、CLI、SDK、多 agent 协同、WebMCP 开放标准等，适合长期关注([blog.google](https://blog.google/innovation-and-ai/technology/ai/google-io-2026-all-our-announcements/?utm_source=openai))。

---

## 3. 开源与开发者工具
- **Microsoft Agent Framework**：已 GA，适合构建多 Agent 工作流和工具调用的入门工具([devblogs.microsoft.com](https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-at-build-2026-announce/?utm_source=openai))。
- **Agent Executor**：Google 开源，方便 Agent 长流程容错与调度([cloud.google.com](https://cloud.google.com/blog/products/ai-machine-learning/agent-executor-googles-distributed-agent-runtime?utm_source=openai))。
- **ASSERT**：Agent 安全评估工具，可作为 Agent 项目中的安全模块添加([devblogs.microsoft.com](https://devblogs.microsoft.com/foundry/build-2026-open-trust-stack-ai-agents/?utm_source=openai))。

---

## 4. 研究与论文进展
虽然没有今天的新论文，但以下几项近期论文值得关注：
- **Auton Agentic AI Framework**：提出认知蓝图与运行时引擎分离架构，加入并行图执行、推理优化、安全投影等机制([arxiv.org](https://arxiv.org/abs/2602.23720?utm_source=openai))。
- **AI Planning Framework for LLM‑Based Web Agents**：将 Agent 架构映射为经典搜索算法（BFS/DFS），提出评价指标与新的数据集([arxiv.org](https://arxiv.org/abs/2603.12710?utm_source=openai))。

学生可从 Agent 架构理解、搜索算法映射、系统优化入手。

---

## 5. AI 基础设施与工程实践
- Agent 的运行效率、可恢复性、安全控制是当前开发重点（参见 Microsoft CodeAct、Google Agent Executor、ASSERT）。
- Agent 身份与发现问题得到标准化重视（参见 ANS 提案）。
- 国家和企业层面推动 Agent 规范化与治理（参见 NIST Initiatives）。

---

## 6. 商业、行业与创业动态
- 虽无今日新融资或商业动向，但 Microsoft、Google、Linux Foundation、NIST 等机构强力推动 Agent 技术生态发展，说明此方向正在成为主流开发基础。

---

## 7. 政策、安全与伦理
- NIST 的 AI Agent 标准倡议代表政策层面的重要推动([nist.gov](https://www.nist.gov/news-events/news/2026/02/announcing-ai-agent-standards-initiative-interoperable-and-secure?utm_source=openai))。
- ASSERT 框架体现开发者角度的安全控制实践([devblogs.microsoft.com](https://devblogs.microsoft.com/foundry/build-2026-open-trust-stack-ai-agents/?utm_source=openai))。
- ANS 提出身份验证层级提升系统可信度([linuxfoundation.org](https://www.linuxfoundation.org/press/linux-foundation-announces-intent-to-launch-agent-name-service-to-establish-trusted-identity-infrastructure-for-ai-agents?hs_amp=true&utm_source=openai))。

---

## 8. 今日技术关键词
### CodeAct
- 解释：将多工具调用合并为 Python 代码执行模型，减少模型 turn 和 token 消耗。
- 重要性：提升 Agent 性能，适合实践学习。
- 入门：参见 MAF 文档，理解 Hyperlight 微 VM。
- 搜索关键词：Microsoft Agent Framework CodeAct

### ASSERT 框架
- 解释：policy‑driven Agent 安全评估与控制框架。
- 重要性：Agent 从 demo 向生产的安全保障。
- 入门：官方博客与 GitHub（若公开）。
- 搜索关键词：Microsoft ASSERT Agent evaluation

### Agent Name Service (ANS)
- 解释：基于 DNS 提供 Agent 身份与发现的开源标准。
- 重要性：增强 agentic 生态的身份可信度。
- 入门：阅读 LF ANS 声明与标准草案。
- 搜索关键词：Linux Foundation Agent Name Service

---

## 9. 今天可以动手做的 3 件小事
1. 运行 CodeAct 示例并对比性能（约 3 小时）。
2. 加入 ASSERT 政策到已有 Agent 项目中，实现简单安全检查（约 3 小时）。
3. 阅读 NIST AI Agent Standards Initiative 文档并撰写 500 字总结（约 2 小时）。

---

## 10. 值得收藏的链接
- Microsoft Agent Framework with CodeAct（Microsoft DevBlogs）—深入理解 Agent 性能优化机制。
- Microsoft ASSERT（Foundry Blog）—学习 agent 安全策略评估方法。
- Linux Foundation ANS 宣告—理解 Agent 身份标准化基础。
- Google Agent Executor（Google Cloud Blog）—探索 Agent 分布式运维机制。
- NIST AI Agent Standards Initiative（NIST News）—掌握 Agent 政策与标准发展动向。

---

## 11. 明天继续追踪
- Microsoft Agent SDK 社区反馈与 GitHub 活动。
- ASSERT 框架 GitHub 项目是否开源、示例更新。
- ANS 标准草案进展与应用示范。
- Google Agent Executor 的用户案例或社区部署经验。
- 相关开源论文项目实现及代码仓库。

---

## 12. 今日总结
- 今天虽无即时新闻，但 Agent 技术依然是当前 AI 技术生态中的焦点，包括性能优化、安全评估、身份验证和长期运行机制。  
- 推荐继续关注 Microsoft、Google、LF 和 NIST 的 Agent 技术动向。  
- 对大二学生而言，可从 CodeAct、ASSERT 和 Agent Executor 入手，实践中学习 Agent 系统结构、性能与安全。  
- Agent 技术短期内适合作为项目练习与简历亮点，值得建立基础与持续关注。

---

**自检确认：**  
- 未编造今日新闻；  
- 所有条目有真实来源；  
- 内容偏技术、适合大二学生；  
- 提供了明确学习与实践建议。
