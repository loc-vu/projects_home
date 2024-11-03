import streamlit as st

def main():
    home_page = st.Page("pages/home.py", title="Home", icon=":material/home:")
    
    paper_search_page = st.Page("pages/paper_rec/arxiv_search.py", title="Paper Recommender", icon=":material/search:")
    paper_dashboard_page = st.Page("pages/paper_rec/arxiv_dashboard.py", title="Arxiv Dashboard", icon=":material/dashboard:")
    
    bls_dashboard_page = st.Page("pages/bls/bls_dashboard.py", title="BLS Dashboard", icon=":material/dashboard:")
    
    pages = st.navigation(
        pages={
            "": [home_page],
            "Research Paper Recommender": [paper_search_page, paper_dashboard_page],
            "BLS Analysis": [bls_dashboard_page]
        },
        expanded=False
    )
    # st.set_page_config(page_title="Home")
    pages.run()




if __name__ == "__main__":
    main()