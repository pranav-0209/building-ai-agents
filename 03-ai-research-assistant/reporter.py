from langchain_core.prompts import ChatPromptTemplate

from config import get_llm
from schemas import ResearchFinding, ResearchReport


SYSTEM_PROMPT = """
You are a professional research report writer.

Your job is to synthesize research findings into a clear,
accurate, and concise research report.

Rules:

- Use only the provided research findings.
- Do not introduce outside knowledge.
- Do not invent facts.
- Do not invent sources.
- Directly address the original research question.
- Combine overlapping findings.
- Highlight important comparisons and trade-offs.
- Keep the report well structured.
- Base the conclusion only on the supplied findings.
"""


class ReportGenerator:

    def __init__(self):

        llm = get_llm()

        self.structured_llm = llm.with_structured_output(
            ResearchReport
        )

        self.prompt = ChatPromptTemplate.from_messages([
            ("system", SYSTEM_PROMPT),
            (
                "human",
                """
Original research question:

{question}


Research findings:

{findings}


Generate the final research report.
"""
            )
        ])

        self.chain = self.prompt | self.structured_llm

    def generate(
        self,
        question: str,
        findings: list[ResearchFinding]
    ) -> ResearchReport:

        formatted_findings = self._format_findings(findings)

        report = self.chain.invoke({
            "question": question,
            "findings": formatted_findings
        })

        return report

    def _format_findings(
        self,
        findings: list[ResearchFinding]
    ) -> str:

        formatted = []

        for index, finding in enumerate(findings, start=1):

            key_points = "\n".join(
                f"- {point}"
                for point in finding.key_points
            )

            finding_text = f"""
FINDING {index}

Research Task:
{finding.task}

Summary:
{finding.summary}

Key Points:
{key_points}
"""

            formatted.append(finding_text)

        return "\n".join(formatted)