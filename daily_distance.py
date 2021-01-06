from sql_queries import sql_query
from database import Database
from calculations import calculateDistance
from datetime import date
import datetime
db = Database()

#stworzenie listy id osób zakażonych
sql_1 = db.select(sql_query(4))

infected_id = []

for row in sql_1:
    infected_id.append(row[0])


#wczoraj i przedwczoraj
yesterday = datetime.date.today() - datetime.timedelta(days=60)
day_before_yesterday = yesterday - datetime.timedelta(days=60)

for i in range(len(infected_id)):
    #zapytanie sql
    string_1 = sql_query(0)
    string_2 = (" WHERE public.user.user_id = "+str(infected_id[i]))
    string_3 = (" AND time_stamp between '"+str(day_before_yesterday)+"' AND '"+str(yesterday)+"'")
    string = string_1 + string_2 + string_3
    query = db.select(string)

    lat = []
    long= []
    id_list = []
    timestamp = []

    for row in query:
        id_list.append(row[0])
        lat.append(row[2])
        long.append(row[3])
        timestamp.append(row[1])

    print(timestamp[0])
    print(timestamp[0] - datetime.datetime.now())
        
    distance = 0
    for j in range(len(lat) - 1):
        distance += calculateDistance(lat[i],lat[i+1],long[i],long[i+1])
        
        
        


    
