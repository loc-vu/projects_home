import sys
import os
import requests
import feedparser
from typing import List, Optional

sys.path.append('/Users/locvu/Documents/ds/paper_rec')
from models.research_paper import ResearchPaper

class ArxivClient:
    """Class for connecting to Arxiv API"""

    # http://export.arxiv.org/api/{method_name}?{parameters}
    BASE_URL = "http://export.arxiv.org/api/query"

    def __init__(self):
        pass

    def search_paper(self, query: str, max_entry: int = 10) -> List[ResearchPaper]:
        """
            Search Arxiv for research papers based on a query string.

            Parameters:
                query (str): The search query.
                max_results (int): The maximum number of results to return.

            Returns:
                List[ResearchPaper]: A list of ResearchPaper objects with data from Arxiv.
        """
        params = {
            "search_query": query,
            "max_results": max_entry,
            "sortBy": "relevance",
            "sortOrder": "descending"
        }
        
        response = requests.get(self.BASE_URL, params=params)
        response.raise_for_status()
        
        return feedparser.parse(response.text)
    


if __name__ == "__main__":
    client = ArxivClient()
    
    papers = client.search_paper(
        query="electron",
        max_entry=10
    )
    print(papers)