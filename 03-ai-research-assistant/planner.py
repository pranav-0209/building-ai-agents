from langchain_core.prompts import ChatPromptTemplate

from config import get_llm
from schemas import ResearchPlan

SYSTEM_PROMPT =  """
You are a research planning assistant.

Your job is to convert a user's research question
into a clear and focused research plan.

Break the topic into independent research tasks.

Rules:

- Create between 3 and 6 research tasks.
- Each task should investigate a specific aspect.
- Avoid duplicate tasks.
- Keep tasks concise.
- Do not answer the research question.
- Only create the research plan.
"""

class ResearchPlanner:

    def __init__(self):
        llm = get_llm()

        self.structured_llm = llm.with_structured_output(ResearchPlan)

        self.prompt = ChatPromptTemplate.from_messages([
            ("system", SYSTEM_PROMPT),
            ("human", "{question}"),
        ])

        self.chain = self.prompt | self.structured_llm

    def create_plan(self, question: str) -> ResearchPlan:
        plan = self.chain.invoke({
            "question": question
        })

        return plan