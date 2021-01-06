from database import Database
from calculations import most_frequently_visited_place , calculateDistance
from api_queries import api_get_waypoints
from sql_queries import sql_query
import datetime
from errors import error

#wyniki
list_id = []
list_lat = []
list_long = []

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
        id_1 = []

        for row in query:
            id_1.append(row[0])
            lat_1.append(row[2])
            long_1.append(row[3])



        try:
            indexes = most_frequently_visited_place(lat_1,long_1)
            id_2.append(id_1[0])
            lat_2.append(lat_1[indexes[0]])
            long_2.append(long_2[indexes[1]])
        except:
            error()

    try:
    
        lat_2 = sorted(lat_2, key=lambda x: x[0])
        long_2 = sorted(long_2, key=lambda x: x[0])

        for i in range(len(lat_2) - 1):
            #aby nie liczyc drogi dla punktow oddalonych o wiecej niz 10 km
            distance = calculateDistance(lat_1[i],lat_2[i+1],long_2[i],long_2[i+1])

            if distance < 10:

                api_get_waypoints(lat_2[i], long_2[i], lat_2[i+1], long_2[i+1] )

                list_from_api = getattr(api,"l")



                #zapełnienie do formatu do bazy
            for i in range(len(list_from_api)):
                #ograniczenie dokladnosci punktow do co piatego
                if i % 5 == 0 :
                    list_lat.append(list_from_api[i][0])
                    list_long.append(list_from_api[i][1])
                    list_id.append(id_2[0])

    except:
        error()


for i in range (len(list_lat)):
    bd.insert_route(list_lat[i],list_long[i],yesterday,list_id[i])

#rozłączenie z bazą
db.connection.close()






        
        
       
        
        

        

