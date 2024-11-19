import sys
import streamlit as st
import streamlit_pydantic as sp

sys.path.append("/Users/locvu/Documents/ds/paper_rec")
from services.arxiv_client import ArxivClient
from components.paper_card import display_paper_card

st.set_page_config(
    page_title="Paper Recommender",
    layout="wide",
)

st.title("Research Paper Recommender")
with st.form(" "):
    search_query = st.text_input("What research paper are you looking for?", value="")

    # TODO: Add column to select the type of recommender system to use
    max_entries_col, _ = st.columns([0.1, 0.9])

    with max_entries_col:
        max_entries = st.selectbox(
            "Max Entries",
            options=[5, 10, 20, 50, 100],
            help="Choose the maximum number of research papers to retreive",
        )
    st.form_submit_button("Search")


arxiv_client = ArxivClient()
papers = arxiv_client.search_paper(query=search_query, max_entry=max_entries)

num_col = 3
grid = st.columns(num_col)

if papers:
    for i in range(len(papers)):
        with grid[i % num_col]:
            display_paper_card(paper=papers[i], number=i + 1)


# st.text_area(
#     label="sample output",
#     value=arxiv_client.search_paper(
#         query=search_query,
#         max_entry=1
#     )
# )
