import mysql.connector
import locale


def _open():
    try:
        bdd = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="mythologie"
        )
        print('test')
    except mysql.connector.Error as err:
        print(err)
    return bdd


class Database:
    """
    Variables
    """
    bdd = None
    """
    Connexion à la BDD
    """

    def __init__(self):
        bdd = _open()

    def __exit__(self):
        self.bdd.close()

    def _query(self, query, args):
        cursor = self.bdd.cursor()
        cursor.execute(query, args)
        return cursor.fetchall()