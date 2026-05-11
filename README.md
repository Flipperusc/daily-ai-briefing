# Daily AI Briefing

一个自动生成并发送 AI 行业日报的 GitHub Actions 项目。

这个项目会在每天固定时间自动运行，调用 OpenAI API 获取并总结最新 AI 发展动态，然后通过 Resend 邮件服务把日报发送到指定邮箱，同时将 Markdown 格式的日报保存到仓库的 `reports/` 目录中，方便后续归档和回顾。

---

## 项目目标

本项目的目标是搭建一个轻量级、可维护、可自动运行的 AI 信息工作流：

1. 每天定时运行。
2. 自动搜索并总结最新 AI 行业进展。
3. 生成中文 AI 日报。
4. 通过邮件发送给自己。
5. 同时将日报保存为 Markdown 文件。
6. 后续可以持续优化 prompt、信息源、邮件样式和分析逻辑。

适合用于：

- 每天快速了解 AI 行业动态。
- 跟踪 OpenAI、Anthropic、Google DeepMind、Meta AI、NVIDIA 等公司的更新。
- 关注模型发布、产品更新、研究论文、开源项目、政策监管和商业动态。
- 学习 GitHub Actions、OpenAI API、邮件 API 和自动化工作流搭建。

---

## 当前功能

目前项目支持：

- 使用 GitHub Actions 定时触发。
- 支持手动触发 workflow。
- 使用 OpenAI API 生成 AI 日报。
- 使用 web search 获取最新公开信息。
- 使用 Resend 发送邮件。
- 生成 Markdown 报告并保存到 `reports/` 目录。
- 通过 GitHub Secrets 安全管理 API key 和邮箱配置。
- 支持自定义日报来源策略。
- 支持自定义日报输出模板。

---

## 项目结构

```text
daily-ai-briefing/
├── .github/
│   └── workflows/
│       └── daily-ai-briefing.yml
├── references/
│   ├── output-template.md
│   └── source-policy.md
├── reports/
│   └── .gitkeep
├── scripts/
│   └── make_briefing.py
├── requirements.txt
└── README.md

### 目录说明

#### `.github/workflows/`

存放 GitHub Actions workflow 配置。

当前主要文件：

```text
.github/workflows/daily-ai-briefing.yml
```

它负责：

* 定时运行脚本。
* 安装 Python。
* 安装依赖。
* 注入 GitHub Secrets。
* 执行日报生成脚本。
* 将生成的报告提交回 GitHub 仓库。

---

#### `scripts/`

存放项目的 Python 脚本。

当前主要文件：

```text
scripts/make_briefing.py
```

它负责：

1. 读取环境变量。
2. 调用 OpenAI API。
3. 生成 AI 日报。
4. 将日报保存到 `reports/`。
5. 将日报通过 Resend 发送到邮箱。

---

#### `references/`

存放 prompt 相关的规则和模板。

当前包含：

```text
references/source-policy.md
references/output-template.md
```

这两个文件相当于项目的“日报编辑规范”。

##### `source-policy.md`

定义日报的信息来源优先级，例如：

* 官方博客和公告
* 论文和会议
* GitHub release
* 可靠科技媒体
* 政策和监管机构公告
* 社交媒体信息的使用限制

##### `output-template.md`

定义日报的输出格式，例如：

* 一句话总览
* Top 5 重点进展
* 模型与产品发布
* 研究与技术进展
* 开源与开发者工具
* 商业与市场动态
* 政策、安全与监管
* 值得关注的趋势
* 明天继续追踪

---

#### `reports/`

存放每天自动生成的 Markdown 日报。

文件命名格式：

```text
YYYY-MM-DD-ai-briefing.md
```

例如：

```text
reports/2026-05-11-ai-briefing.md
```

---

#### `requirements.txt`

记录 Python 项目依赖。

当前主要依赖包括：

```text
openai
resend
markdown
requests
python-dotenv
```

---

## 工作流原理

整体流程如下：

```text
GitHub Actions 定时触发
        ↓
运行 scripts/make_briefing.py
        ↓
读取 source-policy.md 和 output-template.md
        ↓
调用 OpenAI API 生成中文 AI 日报
        ↓
保存 Markdown 到 reports/
        ↓
调用 Resend API 发送邮件
        ↓
提交 reports/ 更新到 GitHub
```

---

## GitHub Actions 定时运行

当前 workflow 使用 GitHub Actions 的 `schedule` 定时触发。

如果希望每天北京时间早上 8 点运行，可以在：

```text
.github/workflows/daily-ai-briefing.yml
```

中设置：

```yaml
on:
  workflow_dispatch:
  schedule:
    - cron: "0 0 * * *"
```

GitHub Actions 的 cron 使用 UTC 时间。

北京时间是 UTC+8，所以：

```text
北京时间 08:00 = UTC 00:00
```

如果想避开整点高峰，也可以设置为北京时间 08:07：

```yaml
schedule:
  - cron: "7 0 * * *"
```

---

## 手动运行

除了定时运行，本项目也支持手动触发。

在 GitHub 仓库页面：

```text
Actions
→ Daily AI Briefing
→ Run workflow
```

这对于测试非常有用。

建议在每次修改代码、prompt 或邮件配置后，先手动运行一次，确认无误后再依赖自动运行。

---

## 环境变量与 GitHub Secrets

本项目不会把 API key 写进代码，而是通过 GitHub Secrets 注入环境变量。

需要在 GitHub 仓库中配置以下 Repository secrets：

```text
OPENAI_API_KEY
RESEND_API_KEY
EMAIL_TO
EMAIL_FROM
```

配置路径：

```text
GitHub Repository
→ Settings
→ Secrets and variables
→ Actions
→ Repository secrets
→ New repository secret
```

---

## 必需的 Secrets

### 1. `OPENAI_API_KEY`

OpenAI API key。

示例格式：

```text
sk-proj-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

注意：

不要写成：

```text
OPENAI_API_KEY=sk-proj-xxx
```

只需要填写 key 本身。

---

### 2. `RESEND_API_KEY`

Resend API key。

示例格式：

```text
re_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

注意：

不要写成：

```text
RESEND_API_KEY=re_xxx
```

只需要填写 key 本身。

---

### 3. `EMAIL_TO`

日报收件邮箱。

示例：

```text
example@gmail.com
```

如果你还没有在 Resend 验证自己的域名，并且使用的是测试发件地址：

```text
onboarding@resend.dev
```

那么 `EMAIL_TO` 必须是你的 Resend 账号邮箱，否则 Resend 会拒绝发送。

---

### 4. `EMAIL_FROM`

日报发件人。

测试阶段可以使用：

```text
AI Briefing <onboarding@resend.dev>
```

长期建议改成你自己验证过的域名邮箱，例如：

```text
AI Briefing <briefing@example.com>
```

其中 `example.com` 必须是你在 Resend 中验证过的域名。

---

## Resend 测试限制说明

如果使用：

```text
onboarding@resend.dev
```

作为发件人，那么 Resend 只允许你把测试邮件发送给 Resend 账号自己的邮箱。

如果看到类似错误：

```text
You can only send testing emails to your own email address
```

说明你当前的 `EMAIL_TO` 不是 Resend 账号邮箱。

解决方式有三种：

1. 将 `EMAIL_TO` 改成 Resend 账号邮箱。
2. 使用目标邮箱重新注册或登录 Resend，并生成新的 API key。
3. 验证自己的域名，然后使用自己的域名邮箱作为 `EMAIL_FROM`。

长期推荐第 3 种方式。

---

## 本地运行

如果想在本地测试，可以先安装依赖：

```bash
pip install -r requirements.txt
```

然后设置环境变量：

```bash
export OPENAI_API_KEY="你的 OpenAI API key"
export RESEND_API_KEY="你的 Resend API key"
export EMAIL_TO="你的收件邮箱"
export EMAIL_FROM="AI Briefing <onboarding@resend.dev>"
export OPENAI_MODEL="gpt-4o"
```

运行脚本：

```bash
python scripts/make_briefing.py
```

如果成功，会看到类似输出：

```text
Report written to reports/2026-05-11-ai-briefing.md
Email sent: ...
```

---

## GitHub Actions 运行流程

workflow 文件大致包含以下步骤：

1. 拉取仓库代码。
2. 设置 Python 运行环境。
3. 安装依赖。
4. 检查 OpenAI API key 是否存在。
5. 运行日报生成脚本。
6. 提交生成的报告。

示例：

```yaml
name: Daily AI Briefing

on:
  workflow_dispatch:
  schedule:
    - cron: "0 0 * * *"

permissions:
  contents: write

jobs:
  generate-and-send:
    runs-on: ubuntu-latest

    steps:
      - name: Check out repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Check OpenAI key exists
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
        run: |
          python - <<'PY'
          import os
          key = os.getenv("OPENAI_API_KEY", "")
          print("OPENAI_API_KEY exists:", bool(key))
          print("OPENAI_API_KEY length:", len(key))
          PY

      - name: Generate and send briefing
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          RESEND_API_KEY: ${{ secrets.RESEND_API_KEY }}
          EMAIL_TO: ${{ secrets.EMAIL_TO }}
          EMAIL_FROM: ${{ secrets.EMAIL_FROM }}
          OPENAI_MODEL: gpt-4o
        run: python scripts/make_briefing.py

      - name: Commit report
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add reports/ || true
          git commit -m "Add daily AI briefing" || echo "No changes to commit"
          git push || echo "No changes to push"
```

---

## 常见问题

### 1. 报错：Missing credentials

错误示例：

```text
openai.OpenAIError: Missing credentials
```

原因：

GitHub Actions 没有读取到 `OPENAI_API_KEY`。

检查：

1. 是否在 Repository secrets 中创建了 `OPENAI_API_KEY`。
2. Secret 名字是否完全正确。
3. 是否误加到了 Codespaces secrets，而不是 Actions secrets。
4. workflow 里是否写了：

```yaml
OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
```

可以通过日志中的检查步骤确认：

```text
OPENAI_API_KEY exists: True
OPENAI_API_KEY length: 100+
```

如果输出：

```text
OPENAI_API_KEY exists: False
OPENAI_API_KEY length: 0
```

说明 secret 没有被正确读取。

---

### 2. 报错：You can only send testing emails to your own email address

原因：

你正在使用 Resend 的测试发件地址：

```text
onboarding@resend.dev
```

但收件人不是 Resend 账号邮箱。

解决方式：

* 将 `EMAIL_TO` 改成 Resend 账号邮箱。
* 或者在 Resend 验证自己的域名。
* 或者用目标邮箱注册 Resend，并重新生成 API key。

---

### 3. 日报生成了，但邮件没发出去

先确认日志里是否有：

```text
Report written to reports/YYYY-MM-DD-ai-briefing.md
```

如果有，说明 OpenAI 生成和本地写文件成功，问题只在邮件发送。

继续检查：

1. `RESEND_API_KEY` 是否正确。
2. `EMAIL_TO` 是否正确。
3. `EMAIL_FROM` 是否符合 Resend 要求。
4. 是否使用了未验证域名。
5. 是否触发了 Resend 测试限制。

---

### 4. 日报内容像“准备策略”，不是新闻日报

如果生成内容类似：

```text
抱歉，我无法生成未来特定日期的内容...
```

说明模型没有正确理解任务，或者没有实际搜索最新信息。

可以优化 prompt，明确要求：

```text
这不是未来预测任务。
你正在每日自动化脚本中运行。
请总结过去 24 到 36 小时内的 AI 领域最新进展。
不要输出准备策略。
必须直接生成日报。
```

也可以在代码中强制启用 web search。

---

### 5. GitHub Actions 没有按预期时间运行

检查：

1. cron 是否使用 UTC 时间。
2. workflow 文件是否在默认分支。
3. GitHub Actions 是否启用。
4. 仓库是否长期没有活动。
5. 是否刚刚修改 workflow，但没有 push 到 GitHub。

北京时间早上 8 点对应：

```text
UTC 00:00
```

所以 cron 应该写：

```yaml
cron: "0 0 * * *"
```

---

### 6. Commit report 失败

如果日志里出现和 `git add`、`git commit` 或 `git push` 相关的错误，可以确认 workflow 里是否有：

```yaml
permissions:
  contents: write
```

同时建议使用更稳妥的提交写法：

```bash
git add reports/ || true
git commit -m "Add daily AI briefing" || echo "No changes to commit"
git push || echo "No changes to push"
```

---

## 如何自定义日报内容

### 修改信息源偏好

编辑：

```text
references/source-policy.md
```

可以加入你特别关注的公司、技术方向或信息源。

例如：

```markdown
我特别关注：
- OpenAI
- Anthropic
- Google DeepMind
- Meta AI
- NVIDIA
- Coding agents
- AI infra
- Multimodal models
- Open-source LLMs

我不太关注：
- 纯融资新闻
- 没有技术细节的营销稿
- 重复报道
```

---

### 修改输出格式

编辑：

```text
references/output-template.md
```

例如，你可以加入：

```markdown
## 对我的行动建议

请给出 3 条适合开发者或创业者的行动建议。
```

或者限制长度：

```markdown
整篇日报控制在 1200 到 1800 中文字。
每条新闻最多 150 字。
```

---

### 修改模型

在 workflow 中修改：

```yaml
OPENAI_MODEL: gpt-4o
```

例如：

```yaml
OPENAI_MODEL: gpt-4o-mini
```

或者：

```yaml
OPENAI_MODEL: gpt-5
```

具体使用哪个模型取决于你的 API 权限、成本预算、输出质量要求和是否需要工具支持。

---

### 修改发送时间

编辑：

```text
.github/workflows/daily-ai-briefing.yml
```

北京时间每天早上 8 点：

```yaml
schedule:
  - cron: "0 0 * * *"
```

北京时间每天早上 8:07：

```yaml
schedule:
  - cron: "7 0 * * *"
```

---

## 安全注意事项

请不要把以下内容写进代码或提交到 GitHub：

```text
OPENAI_API_KEY
RESEND_API_KEY
邮箱登录密码
SMTP 密码
个人隐私信息
```

正确做法是使用 GitHub Secrets。

如果不小心提交了 API key：

1. 立即删除代码中的 key。
2. 重新生成新的 API key。
3. 删除或废弃旧 key。
4. 检查 Git 历史中是否泄露。
5. 必要时重写 Git 历史。

---

## 当前项目状态

当前项目已经实现：

* GitHub Actions 可运行。
* OpenAI API 可生成日报。
* 报告可写入 `reports/`。
* Resend 可用于发送邮件。
* 邮件发送需要确保 `EMAIL_TO` 和 `EMAIL_FROM` 符合 Resend 限制。

---

## 后续优化方向

### 1. 增加日报质量检查

可以在脚本中检查生成内容是否包含无效句子，例如：

```text
无法生成未来内容
准备策略
你可以查看这些网站
```

如果出现这些内容，则让 workflow 失败，而不是发送低质量邮件。

---

### 2. 避免重复发送

可以在生成前检查当天日报是否已经存在。

如果存在：

* 默认跳过。
* 或通过 `FORCE_RUN=true` 强制重新生成。

---

### 3. 加入固定 RSS 信息源

可以增加 RSS 抓取逻辑，优先读取：

* OpenAI Blog
* Anthropic News
* Google DeepMind Blog
* Meta AI Blog
* Microsoft AI Blog
* NVIDIA Blog
* Hugging Face Blog
* arXiv
* GitHub Trending

这样可以让日报来源更稳定，减少模型遗漏重要信息的概率。

---

### 4. 拆分搜索和总结步骤

当前流程通常是：

```text
搜索 + 总结一次完成
```

后续可以拆成：

```text
第一步：搜索候选新闻
第二步：去重和排序
第三步：生成日报
第四步：发送邮件
```

这样更容易调试，也更容易提高质量。

---

### 5. 增加失败通知

如果 workflow 失败，可以额外发送一封失败提醒邮件，或者使用 GitHub 的 Actions notification。

---

### 6. 增加历史回顾

可以每周自动生成一份周报：

```text
过去 7 天 AI 行业重点回顾
```

也可以每月生成一份月报：

```text
本月 AI 行业趋势总结
```

---

## 推荐开发流程

每次修改项目时，建议按以下流程：

```bash
git status
git add .
git commit -m "Describe your change"
git push
```

然后在 GitHub Actions 页面手动运行一次：

```text
Actions
→ Daily AI Briefing
→ Run workflow
```

确认无误后，再等待自动定时运行。

---

## License

This project is for personal automation and learning purposes.

You may modify and reuse it for your own daily briefing workflow.

````

复制后在 Codespaces 里打开 `README.md`，全选替换保存，然后执行：

```bash
git add README.md
git commit -m "Add detailed README"
git push
````
