import sys

import wikipedia
from crewai.tools import BaseTool


class WikipediaSearchTool(BaseTool):
    name: str = "Wikipedia Search"
    description: str = (
        "Search Wikipedia for the article most relevant to a query and return "
        "its summary. Use this for factual movie research."
    )

    def _run(self, query: str) -> str:
        normalized_query = query.strip()
        if not normalized_query:
            return "The query cannot be empty."

        try:
            titles = wikipedia.search(normalized_query, results=3)
            if not titles:
                return f"No Wikipedia article found for: {normalized_query}"

            for title in titles:
                try:
                    page = wikipedia.page(title=title, auto_suggest=False)
                    return (
                        f"Source: {page.title}\n"
                        f"URL: {page.url}\n\n"
                        f"{page.summary}"
                    )
                except wikipedia.DisambiguationError as error:
                    if error.options:
                        page = wikipedia.page(
                            title=error.options[0],
                            auto_suggest=False,
                        )
                        return (
                            f"Source: {page.title}\n"
                            f"URL: {page.url}\n\n"
                            f"{page.summary}"
                        )
                except wikipedia.PageError as error:
                    print(error, file=sys.stderr)

            return f"No usable Wikipedia article found for: {normalized_query}"
        except wikipedia.WikipediaException as error:
            return f"Wikipedia search failed: {error}"
