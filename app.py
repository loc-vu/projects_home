import streamlit as st

def main():
    home_page = st.Page("pages/home.py", title="Home", icon=":material/home:")
    search_page = st.Page("pages/search.py", title="Paper Recommender", icon=":material/search:")
    dashboard_page = st.Page("pages/dashboard.py", title="Arxiv Dashboard", icon=":material/dashboard:")
    
    pages = st.navigation([home_page, search_page, dashboard_page])
    # st.set_page_config(page_title="Home")
    pages.run()




if __name__ == "__main__":
    main()