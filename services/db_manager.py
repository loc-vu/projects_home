import sqlite3

class ArxivDB:
    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()

    def create_table(self, table_name='papers'):
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

    def insert_paper(self):
        pass

    def get_paper(self):
        pass

    def close(self):
        pass


if __name__ == '__main__':
    arxiv_db = ArxivDB(db_path=r'C:\Users\lukev\Documents\projects\projects_home\data\arxiv_papers.db')
    arxiv_db.create_table(
        table_name="papers"
    )