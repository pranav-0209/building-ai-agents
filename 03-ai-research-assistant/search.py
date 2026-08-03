from langchain_tavily import TavilySearch

from schemas import SearchResult


class WebSearchService:

    def __init__(self):
        self.search_tool = TavilySearch(
            max_results=3
        )

    def search(self, query: str) -> list[SearchResult]:

        response = self.search_tool.invoke({
            "query": query
        })

        results = response.get("results", [])

        search_results = []

        for result in results:
            search_result = SearchResult(
                title=result.get("title", ""),
                url=result.get("url", ""),
                content=result.get("content", "")
            )

            search_results.append(search_result)

        return search_results
