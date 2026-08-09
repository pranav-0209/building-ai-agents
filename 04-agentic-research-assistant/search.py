from langchain_tavily import TavilySearch

from schemas import SearchResult


class WebSearchService:

    def __init__(self):
        self.search = None

    def _get_search_client(self):

        if self.search is None:
            try:
                self.search = TavilySearch(max_results=3)
            except Exception as exc:
                raise RuntimeError(
                    "Tavily search is unavailable. Set TAVILY_API_KEY before running web search."
                ) from exc

        return self.search

    def search_web(self, query: str) -> list[SearchResult]:

        results = self._get_search_client().invoke({"query": query})

        if not isinstance(results, dict):
            raise RuntimeError(
                f"Unexpected Tavily response type: {type(results).__name__}"
            )

        if "error" in results:
            raise RuntimeError(f"Tavily search failed: {results['error']}")

        if "results" not in results:
            raise RuntimeError(
                f"Tavily search response did not include results: {results}"
            )

        search_results = []

        for item in results["results"]:
            search_results.append(
                SearchResult(
                    title=item["title"],
                    url=item["url"],
                    content=item["content"],
                )
            )

        return search_results
