from langchain_core.prompts import ChatPromptTemplate

from config import get_llm
from schemas import ResearchFinding, ResearchDecision


class ResearchEvaluator:

    def __init__(self):

        self.llm = get_llm()

        self.prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """
You are evaluating the quality of research.

Your job is NOT to answer the research question.

Your job is to determine whether the available evidence
adequately answers the research task.

If important information is missing, mark the evidence as
insufficient.

Never invent missing information.

Provide a brief explanation for your decision.

Respond in plain text using this format:

Sufficient: yes or no
Reasoning: <short explanation>
""",
                ),
                (
                    "human",
                    """
Research Task:

{task}

Summary:

{summary}

Key Points:

{key_points}

Number of Sources:

{source_count}
""",
                ),
            ]
        )

        self.chain = self.prompt | self.llm

    def _parse_decision(self, text: str) -> ResearchDecision:

        lines = [line.strip() for line in text.splitlines() if line.strip()]

        sufficient_line = next(
            (line for line in lines if line.lower().startswith("sufficient:")),
            "",
        )

        reasoning_line = next(
            (line for line in lines if line.lower().startswith("reasoning:")),
            "",
        )

        sufficient_text = text.lower()

        if ":" in sufficient_line:
            sufficient_text = sufficient_line.split(":", 1)[1].strip().lower()

        sufficient = sufficient_text.startswith(("yes", "true", "1", "sufficient"))

        reasoning = reasoning_line.split(":", 1)[1].strip() if ":" in reasoning_line else text.strip()

        return ResearchDecision(
            sufficient=sufficient,
            reasoning=reasoning,
        )

    def evaluate(
        self,
        finding: ResearchFinding,
    ) -> ResearchDecision:

        response = self.chain.invoke(
            {
                "task": finding.task,
                "summary": finding.summary,
                "key_points": "\n".join(finding.key_points),
                "source_count": len(finding.sources),
            }
        )

        content = getattr(response, "content", str(response)).strip()

        if not content:
            raise RuntimeError("Evaluator returned an empty response.")

        return self._parse_decision(content)
