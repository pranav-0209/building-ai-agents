from langchain_core.prompts import ChatPromptTemplate

from config import get_llm
from schemas import ResearchFinding, ResearchDecision


class ResearchEvaluator:

    def __init__(self):

        llm = get_llm()

        self.structured_llm = llm.with_structured_output(
            ResearchDecision
        )

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

        self.chain = self.prompt | self.structured_llm

    def evaluate(
        self,
        finding: ResearchFinding,
    ) -> ResearchDecision:

        return self.chain.invoke(
            {
                "task": finding.task,
                "summary": finding.summary,
                "key_points": "\n".join(finding.key_points),
                "source_count": len(finding.sources),
            }
        )
