import sqlite3

class SQLiteConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SQLiteConnection, cls).__new__(cls)
            cls._instance.connection = None
        return cls._instance

    def get_connection(self):
        if self.connection is None:
            self.connection = sqlite3.connect("miniprojet.db")
            self.connection.row_factory = sqlite3.Row
        return self.connection
