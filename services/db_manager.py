import sqlite3
from typing import List, Dict

class ArxivDB:
    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.close()

    def create_table(self, table_name: str ='papers'):
        self.cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id TEXT PRIMARY KEY,
            title TEXT,
            authors TEXT,
            abstract TEXT,
            categories TEXT,
            journal_ref TEXT,
            doi TEXT
        )
        """)

        self.connection.commit()

    def insert_paper_bulk(self, table_name: str, papers: List[Dict]):
        for p in papers:
            self.insert_paper(table_name, p)

    def insert_paper(self, table_name: str, paper: Dict):
        self.cursor.execute(f"""
            INSERT OR IGNORE INTO {table_name}        
                (id, title, authors, abstract, categories, journal_ref, doi)
            VALUES
                (?, ?, ?, ?, ?, ?, ?)
        """, (
            paper['id'],
            paper['title'],
            paper['authors'],
            paper['abstract'],
            paper['categories'],
            paper['journal_ref'],
            paper['doi'],
        ))

        self.connection.commit()

    def get_paper(self):
        pass

    def print_table(self, table_name):
        self.cursor.execute(f"SELECT * FROM {table_name}")
        print(self.cursor.fetchall())

    def close(self):
        self.connection.close()


# if __name__ == '__main__':
#     arxiv_db = ArxivDB(
#         db_path=r'C:\Users\lukev\Documents\projects\projects_home\data\arxiv_papers.db'
#     )
#     arxiv_db.create_table(
#         table_name="papers"
#     )