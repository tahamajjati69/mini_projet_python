from connections.mysql_connection import MySQLConnection
from entities.produit import Produit

class ProduitDAOMySQL:
    def __init__(self):
        self.conn = MySQLConnection().get_connection()
        self.init_table()

    def init_table(self):
        cur = self.conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS produit (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nom VARCHAR(255),
                prix FLOAT
            )
        """)
        self.conn.commit()

    def create(self, produit: Produit):
        cur = self.conn.cursor()
        cur.execute(
            "INSERT INTO produit (nom, prix) VALUES (%s, %s)",
            (produit.nom, produit.prix)
        )
        self.conn.commit()

    def get_all(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM produit")
        return cur.fetchall()
