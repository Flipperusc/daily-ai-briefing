import os
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import markdown
import resend
from openai import OpenAI


TIMEZONE = "America/Los_Angeles"
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
你是我的 AI 行业研究助理。请生成 {today} 的中文 AI 发展日报。

目标：
让我在 5 分钟内了解今天全球 AI 领域最重要的发展。

请重点覆盖：
1. 模型与产品发布
2. 研究论文与技术进展
3. 开源模型、框架、工具、数据集
4. 大厂、创业公司、融资、收购、合作
5. 政策、监管、安全、版权、法律动态
6. 对开发者、创业者、产品经理、投资人的影响

质量要求：
- 优先使用官方来源和可靠媒体。
- 不要把传闻当成事实。
- 合并重复新闻。
- 每条重点新闻都要说明“发生了什么”和“为什么重要”。
- 尽量附来源链接。
- 如果今天重大进展不足 5 条，请明确说明，不要凑数。
- 输出中文。
- 邮件阅读体验要好，避免过长段落。

来源策略：
{source_policy}

输出模板：
{output_template}
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
                "type": "web_search"
            }
        ],
        input=build_prompt(today),
    )

    report = response.output_text.strip()
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