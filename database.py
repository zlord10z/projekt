import psycopg2
from errors import error

class Database():


    try:
        connection = psycopg2.connect(user="",
                                      password="",
                                      host="",
                                      port="",
                                      database="")


        cursor = connection.cursor()
    except:
        error()

    def select(self, statement):
        statement = str(statement)
        self.cursor.execute(statement)
        return self.cursor.fetchall()


    def insert(self, statement):
        statement = str(statement)
        self.cursor.execute(statement)


