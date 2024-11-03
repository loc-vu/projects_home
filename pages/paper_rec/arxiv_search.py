import sys
import streamlit as st
import streamlit_pydantic as sp

sys.path.append('/Users/locvu/Documents/ds/paper_rec')
from services.arxiv_client import ArxivClient

st.set_page_config(
    page_title="Research Paper Recommender",
    layout="wide",
)

st.title("Research Paper Recommender")
search_query = st.text_input("What research paper are you looking for?", value="")

arxiv_client = ArxivClient()
papers = arxiv_client.search_paper(
    query=search_query,
    max_entry=10
)

num_col = 5
grid = st.columns(num_col)

if papers:
    for i in range(len(papers)):
        with grid[i % num_col]:
            data = sp.pydantic_form(key=f"paper_{i}", model=papers[i])
            if data:
                st.json(data.model_dump_json())



# st.text_area(
#     label="sample output",
#     value=arxiv_client.search_paper(
#         query=search_query,
#         max_entry=1
#     )
# )


    


