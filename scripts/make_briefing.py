import os
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from openai import OpenAI


TIMEZONE = "America/Los_Angeles"
MODEL = os.getenv("OPENAI_MODEL", "gpt-5")


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


def main() -> None:
    today, report = generate_report()
    output_path = save_report(today, report)
    print(f"Report written to {output_path}")


if __name__ == "__main__":
    main()