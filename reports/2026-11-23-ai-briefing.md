# 今日 AI 学习简报：2026-11-23

## 0. 今日一句话总览

**今日重大进展不足 5 条。** 截至检索时，未找到足够多可由可靠来源核实、且发生于 11 月 23 日或过去 24–36 小时内的重大 AI 发布。下面列出近几日能查到的 3 项官方技术更新；它们不是今天新发生的新闻，其中 OpenAI 的自述数据也应视为公司提供的材料，而非独立验证结论。

## 1. 近日值得关注的 3 件事

### 1. OpenAI 提议用困惑度作为观察模型进步的共同指标（11 月 22 日）

- **发生了什么：** OpenAI 首席科学家讨论用困惑度（perplexity）或交叉熵追踪预训练进展，并倡议行业共享评测标准、提高透明度。文章也提到，困惑度不能直接代表具体任务能力，跨公司比较还受数据集差异影响。([openai.com](https://openai.com/index/perplexity-and-intelligence/))
- **为什么重要：** 它把“模型进步如何衡量”与“何时需要加强安全评估”联系起来；但这是作者的观点与提议，不是已达成的行业标准。
- **对计算机学生的价值：** 复习语言模型下一个词预测、交叉熵、训练集与留出集；思考单一指标为何不能代替任务评测。
- **我可以怎么学／做什么：** 用一个小型语言模型或现成文本分类器，对比训练损失、验证损失与实际任务准确率，观察指标之间的差异。
- **难度：** 入门—中等。**来源：** OpenAI 研究文章《Perplexity and Intelligence》。([openai.com](https://openai.com/index/perplexity-and-intelligence/))

### 2. MedChemBench 测试模型能否推理药物化学问题（11 月 20 日）

- **发生了什么：** OpenAI 发布 MedChemBench，包含基于 117 篇论文与专利的 99 道题，考察模型识别分子结构、解释实验结果、筛选化合物和预测性质等能力。其公布的结果显示，分子结构识别相对较强，化合物选择和数值预测仍较难。([openai.com](https://openai.com/index/introducing-medchembench/))
- **为什么重要：** 这提醒开发者，领域任务的评测不能只看流畅回答；需要拆分能力、依据真实数据检验。OpenAI 也明确说明，该基准**不能证明模型能发现新药或改善实验决策**，且无法排除模型曾接触过公开来源。([openai.com](https://openai.com/index/introducing-medchembench/))
- **对计算机学生的价值：** 关联数据集设计、基准测试、错误分析与多模态结构识别。
- **小项目：** 选一个公开图表问答或分子数据集，建立“输入—模型输出—人工核对—错误分类”的评测表。
- **难度：** 中等。**来源：** OpenAI MedChemBench 介绍与论文入口。([openai.com](https://openai.com/index/introducing-medchembench/))

### 3. OpenAI 介绍用 Agent 自动调查和修复性能回归（11 月 19 日）

- **发生了什么：** OpenAI 描述了内部 Performance Factory：性能告警触发任务后，Agent 调查日志、指标和代码，提出修复，再由后续流程检查部署后是否恢复。公司称该工作流运行三个月以上，跟踪了 1,700 多次调查、定位了 600 多个问题；这些是公司自报数据。([openai.com](https://openai.com/index/how-openai-performance-factory-keeps-chatgpt-fast/))
- **为什么重要：** 展示的不是“让 Agent 自主写代码”这么简单，而是把任务状态、工具权限、人工审核和部署后验证接成闭环。
- **对计算机学生的价值：** 涉及软件工程、可观测性、日志与指标、状态机、测试和持续交付。
- **小项目：** 做一个简化版告警助手：读取测试失败或耗时异常，生成排查摘要和修复建议，必须由人确认后才改代码。
- **难度：** 中等。**来源：** OpenAI 工程文章《How OpenAI’s Performance Factory keeps ChatGPT fast》。([openai.com](https://openai.com/index/how-openai-performance-factory-keeps-chatgpt-fast/))

## 2. 模型、工具与工程观察

这几项更新没有提供足够证据说明某个新模型或 API 在今天发布。近期更值得学习的工程主题是：**Agent 需要可评估、可追踪、可限制权限，并在执行后验证结果**。OpenAI 的性能工作流强调任务状态和人工审核；其 Codex 沙箱文章也介绍了文件与网络权限边界，适合结合操作系统权限和安全设计理解。([openai.com](https://openai.com/index/how-openai-performance-factory-keeps-chatgpt-fast/))

## 3. 今日技术关键词

- **困惑度（Perplexity）：** 衡量语言模型预测文本的表现，不能直接等同于真实任务能力。入门可搜索：`语言模型 交叉熵 困惑度 留出集`。([openai.com](https://openai.com/index/perplexity-and-intelligence/))
- **基准测试（Benchmark）：** 用固定任务和评分规则比较系统表现；关键是防止数据泄漏，并分析分项错误。搜索：`benchmark data leakage error analysis`。([openai.com](https://openai.com/index/introducing-medchembench/))
- **Agent 工作流：** 将模型调用、工具执行、任务状态和人工检查组织成流程。搜索：`agent workflow state machine human approval`。([openai.com](https://openai.com/index/how-openai-performance-factory-keeps-chatgpt-fast/))

## 4. 今天可以动手做的 3 件小事

1. **1 小时：** 阅读困惑度文章，写下“困惑度能说明什么、不能说明什么”各两点。([openai.com](https://openai.com/index/perplexity-and-intelligence/))
2. **1–2 小时：** 为一个小型问答系统建立 20 条测试问题，记录正确性、引用依据和失败类型。
3. **2–3 小时：** 用 Python 写一个简单工作流：检测测试失败 → 生成摘要 → 等待人工批准 → 运行测试复核。不要直接让模型自动部署。

## 5. 值得收藏的链接

- [Perplexity and Intelligence（OpenAI）](([openai.com](https://openai.com/index/perplexity-and-intelligence/)))：理解预训练指标及其局限。
- [MedChemBench（OpenAI）](([openai.com](https://openai.com/index/introducing-medchembench/)))：观察领域评测如何拆分能力、标注局限。
- [Performance Factory（OpenAI）](([openai.com](https://openai.com/index/how-openai-performance-factory-keeps-chatgpt-fast/)))：参考 Agent 工作流、告警处置与复核设计。
- [Inside the Codex sandbox（OpenAI）](([openai.com](https://openai.com/index/inside-the-codex-sandbox/)))：学习编程 Agent 的沙箱、文件和网络权限控制。

## 6. 明天继续追踪

1. 是否有 11 月 23 日当天可由官方公告或论文确认的新模型、API 或开源项目。
2. 其他 AI 实验室是否公开可比较的预训练指标与评测方法。
3. 编程 Agent 在权限隔离、人工审核和结果验证方面的实践进展。

## 今日总结

今天最值得学习的不是追逐新模型，而是理解 **AI 评测与 Agent 工程闭环**。短期可做一个带人工确认和测试复核的排障小工具；长期则关注如何用可靠基准、权限控制和可观测性，让 Agent 在真实软件流程里安全工作。今天能核实的材料数量有限，因此没有凑满五条，也没有把前几日的更新冒充为今日新闻。
