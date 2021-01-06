from database import Database
from calculations import most_frequently_visited_place , calculateDistance
from api_queries import api_get_waypoints
from sql_queries import sql_query
import datetime
from errors import error


#dane do bazy
list_id = []
list_distance = []
forecast_time =[]

#Stworzenie obiektu klasy Database do zapytań sql
db = Database()


#stworzenie listy id osób zakażonych
sql_1 = db.select(sql_query(4))

infected_id = []

for row in sql_1:
    infected_id.append(row[0])

#lista godzin do zapytań sql
h = []
for i in range(24):
    h.append(i)

#wczoraj i przedwczoraj
yesterday = datetime.date.today() - datetime.timedelta(days=1)
day_before_yesterday = yesterday - datetime.timedelta(days=1)

#stworzenie pętli do zapytania sql dla każdego id zakażonego (WHERE public.user.user_id = )
for i in range(len(infected_id)):
    id_2 = []
    lat_2 = []
    long_2 = []

   
    #petla dla kazdej godziny dnia poprzedniego
    for j in range(len(h)):
        #zapytanie sql
        string_1 = sql_query(0)
        string_2 = (" WHERE public.user.user_id = "+str(infected_id[i]))
        string_3 = (" AND date_part ('hour',time_stamp) BETWEEN '")
        string_4 = (str(h[j])+"' AND '"+str(h[j])+"'")
        string_5 = (" AND time_stamp between '"+str(day_before_yesterday)+"' AND '"+str(yesterday)+"'")
        string = string_1 + string_2 + string_3 + string_4 + string_5
        query = db.select(string)

        #lat,long,id,timestamp - lokalizacja dla przedziału od godziny do godziny następnej (np. od 8:00 do 8:59)
        # dnia poprzedniego dla danego id
        lat_1 = []
        long_1 = []


        for row in query:
            id_1.append(row[0])
            lat_1.append(row[2])
            long_1.append(row[3])


        #pobranie prognozy lokalizacji na tą samą godzine
        string_1 = ("select * from forecast")
        string_2 = (" WHERE user_id = "+str(infected_id[i]))
        string_3 = (" AND date_part ('hour',forecast_time) BETWEEN '")
        string_4 = (str(h[j])+"' AND '"+str(h[j])+"'")
        string_5 = (" AND forecast_time between '"+str(day_before_yesterday)+"' AND '"+str(yesterday)+"'")
        string = string_1 + string_2 + string_3 + string_4 + string_5
        query = db.select(string)

        lat_2 = []
        long_2 = []
        timestamp = []

        for row in query:
            lat_2.append(row[3])
            long_2.append(row[4])
            timestamp.append(row[2])

        try:
            # dopasowanie elementu nabliżej średniej i wskazanie indeksu elementu w liscie
            index_lat = np.argmin(np.abs(np.array(lat_1) - lat_2[0]))
            index_long = np.argmin(np.abs(np.array(long_1) - long_2[0]))

            distance = calculateDistance(lat_1[index_lat],lat_2[0],long_1[index_long],long_2[0])

            list_distance.append(distance)
            list_id.append(infected_id[i])
            forecast_time.append(timestamp[0])

        except:
            error()


#for i in range (len(timestamp)):
#    bd.insert("insert into forecast_accuracy(distance,user_id,time_stamp) values (%s,%s,%s)",(list_distance[i],list_id[i],forecast_time[i]))



#rozłączenie z bazą
db.connection.close()






        
        
       
        
        

        

