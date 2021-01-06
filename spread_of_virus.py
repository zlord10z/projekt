from database import Database
from sql_queries import sql_query
from calculations import calculateDistance
from errors import error

db = Database()

#stworzenie listy ID osób zakażonych
sql = db.select(sql_query(4))

infected_id = []

for row in sql:
    infected_id.append(row[0])

#lista wszystkich ID
all_id = []
sql = db.select("select  public.user.user_id from public.user")
for row in sql:
    all_id.append(row[0])

#lista ID osob niezakazonych
healthy_id = []
for element in all_id:
    if element not in infected_id:
        healthy_id.append(element)
#wyniki -mozliwie zakazone
possibly_infected = []

#aby wyk
for k in range(15):

    sql_1 = " AND time_stamp >= NOW() - INTERVAL '"+str(k + 1)+" minutes'"
    sql_2 = " AND time_stamp <= NOW() - INTERVAL '"+str(k)+" minutes'"

    for i in range(len(infected_id)):
        id_inf = []
        timestamp_inf = []
        lat_inf = []
        long_inf = []
        
        sql = db.select(str(sql_query(7) + str(infected_id[i]) + sql_1 + sql_2))
        for row in sql:
            id_inf.append(row[0])
            timestamp_inf.append(row[1])
            lat_inf.append(row[2])
            long_inf.append(row[3])
        
        
        for j in range(len(healthy_id)):
            id_healthy = []
            timestamp_healthy = []
            lat_healthy = []
            long_healthy = []

            sql = db.select(str(sql_query(7) + str(healthy_id[j]) + sql_1 + sql_2))
            for row in sql:
                id_healthy.append(row[0])
                timestamp_healthy.append(row[1])
                lat_healthy.append(row[2])
                long_healthy.append(row[3])

            for inf in range(len(id_inf)):

                for h in range(len(id_healthy)):
                    try:
                        distance = calculateDistance(lat_inf[inf],lat_healthy[h],long_inf[inf],long_healthy[h])

                        #jeżeli dystans osoby zakażonej od niezakażonej wynosi mniej niż 100 metrów oznaczyc jako mozliwie zarazona
                        if distance < 0.1:
                            possibly_infected.append(id_healthy[0])
                    except:                        
                        error()
            
for i in range(len(possibly_infected)):        
    #update health condition
    query = sql_query(6) + str(possibly_infected[i])
    db.insert(query)

db.connection.close()






















