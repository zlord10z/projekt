from datetime import date
import datetime
from database import Database
from errors import error
from sql_queries import sql_query
from calculations import calculateDistance 

db = Database()

all_id = []

distance_infected = 0
distance_noninfected = 0
yesterday = datetime.date.today() - datetime.timedelta(days=1)

#tworzenie listy id wszystkich użytkowników (zakażonych i niezakażonych)
query = db.select(sql_query(3))
for row in query:
    all_id.append(row[0])

print(all_id)
  
    
#dla zakazonego/niezakazonego
for i in range(2):
    infection_stamp = 0 + i

    if i == 0:
       health_condition = "= \'infected'"

    if i == 1:
       health_condition = "!= \'infected'"


#dla kazdego id
    for i in range(len(all_id)):
        user_id = all_id[i]
        string_1 = (sql_query(0)+"where public.user.user_id = "+str(user_id))
        string_2 = (" and health_condition " + health_condition)
        string_3 = (" and time_stamp between '" + str(yesterday) + "' and '"+str(yesterday  + datetime.timedelta(days=1))+"'")
        string = string_1 + string_2 + string_3
        query = db.select(string)
        
        lat = []
        long = []
        
        for row in query:
            lat.append(row[2])
            long.append(row[3])


        for i in range(len(lat) - 1):
            lat1 = float(lat[i])
            lat2 = float(lat[i+1])
            long1 = float(long[i])
            long2 = float(long[i+1])
            
            try:
                d = calculateDistance(lat1, lat2, long1, long2)
           
                if infection_stamp == 0:
                    distance_infected += d

                else:
                    distance_noninfected += d
            except:
                error()

print(distance_infected)

print("zakazeni dystans:",round(distance_infected,2),"km")
print("niezakazeni dystans:",round(distance_noninfected,2),"km")

db.insert_distance(yesterday,distance_noninfected,distance_infected)
db.connection.close()

