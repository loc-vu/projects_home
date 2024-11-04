import streamlit as st
from models.research_paper import ResearchPaper

def display_paper_card(paper: ResearchPaper, number: int):
    """
    Display a research paper's details in a card format.

    Parameters:
        paper (ResearchPaper): The research paper object with title, authors, and abstract.
    """
    # Styling for card
    card_style = """
    <style>
        .card {
            padding: 15px;
            margin: 10px 0;
            border-radius: 10px;
            border: 2px solid rgba(189, 195, 199, 0.6);
            font-family: 'Times New Roman', Times, serif;
        }
        .card-number {
            position: absolute;
            bottom: 5px;
            right: 5px;
            font-size: 0.8rem;
            font-weight: bold;
            padding: 2px 6px;
        }

        .card-title {
            font-size: 1.2rem;
            font-weight: bold;
            margin-bottom: 5px;
        }
        .card-authors {
            font-size: 0.9rem;
            margin-bottom: 10px;
        }
        .card-abstract {
            font-size: 0.95rem;
        }
    </style>
    """
    # Injecting the style
    st.markdown(card_style, unsafe_allow_html=True)

    card_html = f"""
    <div class="card">
        <div class="card-title">
            <a href="{paper.pdf_url}" target="_blank">{paper.title}</a>
        </div>
        <div class="card-authors"><strong>Authors:</strong> {', '.join(paper.authors)}</div>
        <div class="card-abstract"><strong>Abstract:</strong> {paper.abstract}</div>
        <div class="card-number">{number}</div>
    </div>
    """
    # Render the card HTML
    st.markdown(card_html, unsafe_allow_html=True)