import os
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import markdown
import resend
from openai import OpenAI


TIMEZONE = "Asia/Shanghai"
MODEL = os.getenv("OPENAI_MODEL", "gpt-4o")

EMAIL_FROM = os.getenv("EMAIL_FROM", "AI Briefing <onboarding@resend.dev>")
EMAIL_TO = os.environ["EMAIL_TO"]


def read_text(path: str) -> str:
    file_path = Path(path)
    if not file_path.exists():
        return ""
    return file_path.read_text(encoding="utf-8")


def build_prompt(today: str) -> str:
    source_policy = read_text("references/source-policy.md")
    output_template = read_text("references/output-template.md")

    return f"""
你正在一个每日自动化脚本中运行。

运行日期：{today}
任务类型：生成真实、可验证、面向计算机专业学生的 AI 学习日报。

用户画像：
- 用户是计算机专业大二学生。
- 用户对 AI、编程、开源项目、新技术和未来技术趋势有强烈好奇心。
- 用户希望通过日报了解 AI 行业最新进展，同时找到适合自己学习和实践的方向。
- 用户不只想看新闻，更想知道这些新闻背后的技术、学习价值和项目机会。

你的角色：
你是用户的 AI 技术学习助理、行业观察员和项目灵感教练。
你的任务不是简单罗列新闻，而是帮助用户把 AI 行业动态转化为学习路径、技术理解和实践项目。

核心目标：
生成一份中文 AI 学习简报，让用户在 5-8 分钟内了解今天 AI 领域最值得关注的真实进展，并知道自己可以学什么、做什么、继续追踪什么。

硬性要求：
- 必须使用 web search 查询真实公开信息。
- 必须总结真实发生的 AI 行业进展。
- 不得生成示例内容。
- 不得生成虚构新闻。
- 不得输出“虚构示例”“仅用于说明”“准备策略”等内容。
- 不得使用占位符来源，例如“[OpenAI 官方博客]”“[GitHub Release]”“[官方新闻稿]”。
- 每条 Top 5 新闻必须包含真实来源。
- 没有可靠来源的内容必须删除。
- 如果今天重大进展不足 5 条，就明确说明“今日重大进展不足 5 条”，不要编造。
- 如果某条信息来自媒体报道而不是官方来源，请明确说明。
- 如果某条信息仍不确定，请标注“不确定”。
- 输出必须是中文。
- 不要使用夸张营销化表达。
- 日报应该偏技术、偏学习、偏实践。
- 整体控制在 1500-2500 中文字左右。

时间范围：
- 优先总结 {today} 当天或过去 24-36 小时内的新进展。
- 如果某个重要事件发生在稍早时间，但今天仍有重要后续，可以纳入。
- 不要把过时新闻包装成今天新闻。

重点关注：
1. AI 编程工具、Coding Agent、AI IDE。
2. AI Agent、自动化工作流、多 Agent 系统。
3. LLM 应用开发、RAG、向量数据库、工具调用。
4. 开源模型、本地部署、推理加速。
5. 多模态 AI，包括文本、图像、音频、视频。
6. AI 基础设施，包括 GPU、推理服务、MLOps、评测系统。
7. 有代码、demo 或工程价值的论文。
8. 对学生学习、项目、实习、未来就业有启发的行业动态。
9. AI 监管、安全、版权和伦理问题。

输出时请特别关注：
- 这件事背后涉及哪些计算机知识。
- 我作为大二学生应该怎么入门。
- 有没有适合做成小项目的方向。
- 有没有值得收藏的链接。
- 哪些技术方向值得未来持续关注。

来源策略：
{source_policy}

输出模板：
{output_template}

最后请自检：
1. 是否有虚构内容？
2. 是否有占位符来源？
3. 是否每条重点内容都有真实来源？
4. 是否符合计算机专业大二学生的学习需求？
5. 是否给出了具体可执行的学习或项目建议？

如果无法找到足够可靠的今日信息，请如实说明，不要编造。
""".strip()   

def generate_report() -> tuple[str, str]:
    api_key = os.environ["OPENAI_API_KEY"]

    now = datetime.now(ZoneInfo(TIMEZONE))
    today = now.strftime("%Y-%m-%d")

    client = OpenAI(api_key=api_key)

    response = client.responses.create(
        model=MODEL,
        tools=[
            {
                "type": "web_search",
                "search_context_size": "medium",
            }
        ],
        tool_choice="required",
        input=build_prompt(today),
    )

    report = response.output_text.strip()
    bad_phrases = [
    "虚构示例",
    "并非实际发生事件",
    "仅用于说明",
    "准备策略",
    "无法生成未来",
    "这只是一个示例",
    "以下是一个示例",
    "假设今天",
    "来源：[OpenAI 官方博客]",
    "来源：[GitHub Release]",
    "来源：[官方新闻稿]",
    "来源：[NeurIPS 会议论文]",
    "[OpenAI 官方博客]",
    "[GitHub Release]",
    "[官方新闻稿]",
    "[NeurIPS 会议论文]",
]

    if any(phrase in report for phrase in bad_phrases):
        raise RuntimeError(
            "Generated report looks like a fictional example or contains placeholder sources. "
            "Please check the prompt and web search settings."
        )
    return today, report


def save_report(today: str, report: str) -> Path:
    output_dir = Path("reports")
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / f"{today}-ai-briefing.md"
    output_path.write_text(report + "\n", encoding="utf-8")

    return output_path


def markdown_to_email_html(report: str) -> str:
    body_html = markdown.markdown(
        report,
        extensions=["extra", "tables", "sane_lists"],
    )

    return f"""
<!doctype html>
<html>
  <body style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; line-height: 1.6; color: #111827; max-width: 760px; margin: 0 auto; padding: 24px;">
    <div style="border-bottom: 1px solid #e5e7eb; margin-bottom: 24px;">
      <h1 style="font-size: 24px; margin-bottom: 8px;">今日 AI 发展简报</h1>
      <p style="color: #6b7280; margin-top: 0;">自动生成，仅供参考，请以原始来源为准。</p>
    </div>
    {body_html}
    <hr style="margin-top: 32px; border: none; border-top: 1px solid #e5e7eb;" />
    <p style="font-size: 12px; color: #6b7280;">
      This email was generated automatically by your daily AI briefing workflow.
    </p>
  </body>
</html>
""".strip()


def send_email(today: str, report: str) -> None:
    resend.api_key = os.environ["RESEND_API_KEY"]

    html = markdown_to_email_html(report)

    params: resend.Emails.SendParams = {
        "from": EMAIL_FROM,
        "to": [EMAIL_TO],
        "subject": f"今日 AI 发展简报 - {today}",
        "html": html,
        "text": report,
    }

    result = resend.Emails.send(params)
    print(f"Email sent: {result}")


def main() -> None:
    today, report = generate_report()
    output_path = save_report(today, report)
    print(f"Report written to {output_path}")

    send_email(today, report)


if __name__ == "__main__":
    main()
