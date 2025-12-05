from entities.client import Client
from connections.sqlite_connection import SQLiteConnection
class ClientDAOSQLite:

    def __init__(self):
        self.conn = SQLiteConnection().get_connection()
        self.init_table()

    def init_table(self):
        cur = self.conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS client (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT,
                email TEXT
            )
        """)
        self.conn.commit()

    def create(self, c: Client):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO client (nom, email) VALUES (?, ?)", (c.nom, c.email))
        self.conn.commit()

    def find_all(self):
        cur = self.conn.cursor()
        cur.execute("SELECT id, nom, email FROM client")
        return [Client(*row) for row in cur.fetchall()]

    def find_by_email(self, email):
        cur = self.conn.cursor()
        cur.execute("SELECT id, nom, email FROM client WHERE email=?", (email,))
        row = cur.fetchone()
        return Client(*row) if row else None
