import sys
import streamlit as st

sys.path.append('/Users/locvu/Documents/ds/paper_rec')
from services.arxiv_client import ArxivClient

st.title("Research Paper Recommender")
search_query = st.text_input("What research paper are you looking for?", value="")


arxiv_client = ArxivClient()
st.text_area(
    label="sample output",
    value=arxiv_client.search_paper(
        query=search_query,
        max_entry=1
    )
)



