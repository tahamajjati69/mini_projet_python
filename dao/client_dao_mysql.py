from entities.client import Client
from connections.mysql_connection import MySQLConnection
class ClientDAOMySQL:

    def __init__(self):
        self.conn = MySQLConnection().get_connection()
        self.init_table()

    def init_table(self):
        cur = self.conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS client (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nom VARCHAR(255),
                email VARCHAR(255)
            )
        """)
        self.conn.commit()

    def create(self, c: Client):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO client (nom, email) VALUES (%s, %s)", (c.nom, c.email))
        self.conn.commit()

    def find_all(self):
        cur = self.conn.cursor()
        cur.execute("SELECT id, nom, email FROM client")
        return [Client(*row) for row in cur.fetchall()]

    def find_by_email(self, email):
        cur = self.conn.cursor()
        cur.execute("SELECT id, nom, email FROM client WHERE email=%s", (email,))
        row = cur.fetchone()
        return Client(*row) if row else None
