from connections.mysql_connection import MySQLConnection
from connections.sqlite_connection import SQLiteConnection

from dao.produit_dao_mysql import ProduitDAOMySQL
from dao.produit_dao_sqlite import ProduitDAOSQLite

from dao.client_dao_mysql import ClientDAOMySQL
from dao.client_dao_sqlite import ClientDAOSQLite

from entities.produit import Produit
from entities.client import Client

def choose_db():
    print("1. SQLite\n2. MySQL")
    c = input("Choix: ")
    return "sqlite" if c == "1" else "mysql"

def main():
    db = choose_db()

    if db == "sqlite":
        prod_dao = ProduitDAOSQLite()
        client_dao = ClientDAOSQLite()
    else:
        prod_dao = ProduitDAOMySQL()
        client_dao = ClientDAOMySQL()

    print("Inserting product...")
    prod_dao.create(Produit(nom="phone", prix=2000))

    print("Inserting client...")
    client_dao.create(Client(nom="Taha", email="motahamajjati@gmail.com"))

    print("Products:")
    print(prod_dao.get_all())

    print("Clients:")
    print(client_dao.find_all())

if __name__ == "__main__":
    main()
