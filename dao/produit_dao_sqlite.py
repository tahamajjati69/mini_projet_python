from connections.sqlite_connection import SQLiteConnection
from entities.produit import Produit

class ProduitDAOSQLite:
    def __init__(self):
        self.conn = SQLiteConnection().get_connection()
        self.init_table()

    def init_table(self):
        cur = self.conn.cursor()
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS produit (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT,
                prix REAL
            )
        """
        )

    def create(self, produit: Produit):
        cur = self.conn.cursor()
        cur.execute(
            "INSERT INTO produit (nom, prix) VALUES (?, ?)",
            (produit.nom, produit.prix)
        )
        self.conn.commit()

    def get_all(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM produit")
        return cur.fetchall()
