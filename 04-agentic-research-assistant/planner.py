from langchain_core.prompts import ChatPromptTemplate

from config import get_llm
from schemas import ResearchPlan

class ResearchPlanner:

    def __init__(self):

        llm = get_llm()

        self.structured_llm = llm.with_structured_output(ResearchPlan)

        self.prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """
You are a research planning assistant.

Your job is to break a user's research question into a small set of
focused research tasks.

Create tasks that help gather enough evidence to answer the question well.

Guidelines:
- Keep tasks specific and researchable.
- Avoid duplicate tasks.
- Prefer 3 to 5 tasks.
- Focus only on information necessary to answer the user's question.
- Do not answer the research question yourself.
""",
                ),
                (
                    "human",
                    """
Research question:

{question}

Create a research plan.
""",
                ),
            ]
        )

        self.chain = self.prompt | self.structured_llm

    def create_plan(self, question: str) -> ResearchPlan:
        return self.chain.invoke({"question": question})

