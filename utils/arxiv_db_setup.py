import sys
import json

from services.db_manager import ArxivDB
# from models.research_paper import ResearchPaper

# data = [json.loads(line) for line in open('../data/204/arxiv-metadata-oai-snapshot.json', 'r')]

table_name = 'papers'
arxiv_db = ArxivDB(db_path='../data/arxiv_papers.db')
arxiv_db.create_table(table_name=table_name)

with open('../data/204/arxiv-metadata-oai-snapshot.json', 'r') as data_file:
    for line in data_file:
        entry = json.loads(line)
        data = {
            "id": entry['id'],
            "title": entry['title'],
            "authors": entry['authors'],
            "abstract": entry['abstract'],
            "categories": entry['categories'],
            "journal_ref": entry['journal-ref'],
            "doi": entry['doi']
        }

        arxiv_db.insert_paper(table_name=table_name, papers=data)

arxiv_db.print_table(table_name=table_name)
arxiv_db.close()