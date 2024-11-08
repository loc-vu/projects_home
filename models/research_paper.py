from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime

@dataclass
class ResearchPaper:
    """Base data model for representing a research paper"""

    id: str
    title: str
    authors: List[str]
    abstract: str
    publication_date: datetime
    pdf_url: Optional[str] = None
    categories: str = None