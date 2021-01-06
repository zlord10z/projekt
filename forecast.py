import numpy as np
import datetime
from datetime import date
from database import Database
from errors import error
from sql_queries import sql_query
from calculations import calculateDistance
from calculations import most_frequently_visited_place
from api_queries import api_holidays


db = Database()


today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)
weekday = today.weekday()
one_day = datetime.timedelta(days=1)

uid_forecast = []
lat_forecast = []
long_forecast = []
timestamp_forecast = []



#pobranie wszystkich id zakażonych
query = db.select(sql_query(4))
list_id = []
for row in query:
    list_id.append(row[0])

print(list_id)


#ostatnie 3 te same dni tygodnia (np.: 3 ostatnie poniedziałki jezeli jutro poniedzialek)
#do zapytania sql
days = []

for i in range(3):
    if i == 0:
        days.append(tomorrow - datetime.timedelta(days=7))
    else:
        i = i - 1
        days.append(days[i] - datetime.timedelta(days=7))



#godziny do zapytania sql
h = [23,24]
#hm = [1,2]

for i in range(22):
    i += 1
    h.append(i)
    #hm.append(hm[i] + 1)



for i in range(len(list_id)):  # pętla do obliczen dla kazdego UID z osobna
    d = 0 + i

    for k in range(len(h)): #petla dla danej godziny
        hour_mark = k

        uid_day = []
        lat_day = []
        long_day = []
        timestamp_day = []


        for j in range(len(days)):  # pętla dla dni
            timestamp = []
            uid = []
            lat = []
            long = []


            dm = days[j] 
            dp = days[j] + datetime.timedelta(days=1)

            string_1 = sql_query(0)
            string_2 = (" WHERE public.user.user_id = "+str(list_id[d]))
            string_3 = (" AND date_part ('hour',time_stamp) BETWEEN '")
            string_4 = (str(h[k])+"' AND '"+str(h[k])+"'")
            string_5 = (" AND time_stamp between '"+str(dm)+"' AND '"+str(dp)+"'")
            string = string_1 + string_2 + string_3 + string_4 + string_5
            query = db.select(string)


            for row in query:
                timestamp.append(row[1])
                uid.append(row[0])
                lat.append(row[2])
                long.append(row[3])

            try:
                mfvp = most_frequently_visited_place(lat, long)

            
                timestamp1 = timestamp[mfvp[0]]
                q = timestamp1.replace(day = today.day + 1, minute = 0, second = 0)

                if q not in timestamp:
                    uid_day.append(uid_all[0])
                    lat_day.append(lat_all[mfvp[0]])
                    long_day.append(lon_all[mfvp[1]])
                    timestamp_day.append(q)
            except:
                pass

        try:    
            mfvp = most_frequently_visited_place(lat_day, long_day)

        
            timestamp1 = timestamp_all[mfvp[0]]
            q = timestamp1.replace(day = today.day + 1, minute = 0, second = 0)

            if q not in timestamp:
                uid_forecast.append(uid_day[0])
                lat_forecast.append(lat_day[mfvp[0]])
                long_forecast.append(long_day[mfvp[1]])
                timestamp_day.append(q)

        except:
            pass



for i in range(len(uid_day)):
    bd.insert("insert into forecast(forecast_lat,forecast_long,forecast_time,user_id) values (%s, %s, %s, %s)",(lat_forecast[i],long_forecast[i],timestamp_forecast[i],uid_forecast[i]))


db.connection.close()


        
