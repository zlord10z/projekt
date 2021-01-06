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


    def update(self, statement):
        statement = str(statement)
        self.cursor.execute(statement)

    def insert_distance(self, timestamp,inf,health):
        self.cursor.execute("insert into distance (distance_timestamp,distance_healthy,distance_infected) values (%s, %s, %s)",(timestamp,health,inf))
        self.connection.commit()

    def insert_route(self,uid,timestamp,lat,long):
        self.cursor.execute("insert into route(route_lat,route_long,route_time,user_id) values (%s, %s, %s, %s)",(lat,long,timestamp,uid))
        self.connection.commit()

    def insert_forecast(self,uid,timestamp,lat,long):
        self.cursor.execute("insert into forecast(forecast_lat,forecast_long,forecast_time,user_id) values (%s, %s, %s, %s)",(lat,long,timestamp,uid))
        self.connection.commit()
