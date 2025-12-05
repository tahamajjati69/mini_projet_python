import mysql.connector

class MySQLConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MySQLConnection, cls).__new__(cls)
            cls._instance.connection = None
        return cls._instance

    def get_connection(self):
        if self.connection is None:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",  # laisse vide si tu n’as pas de mot de passe
                database="boutique"
            )
        return self.connection
