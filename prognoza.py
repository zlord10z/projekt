from klasy import BazaDanych
from klasy import Api
from klasy import Obliczenia
import numpy as np
import datetime
from datetime import date


obl = Obliczenia()
bd = BazaDanych()

uid = []
lat = []
lon = []
timestamp = []
x = 0


holidays = []
try:
    x = 0 / 0
    #lista czy są święta dziś i jutro [true/false]
    api = Api()
    api.api_holidays()
    holidays = getattr(api,'holidays')
except:
    holidays = ["false", "false"]

print(holidays)


#pobranie wszystkich id zakażonych
bd.selecta9()
list_id_health = getattr(bd,'select9')
list_id = []
for row in list_id_health:
    list_id.append(row[0])


today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)
weekday = today.weekday()
one_day = datetime.timedelta(days=1)
winter_break = [datetime.date(2021, 1, 4),datetime.date(2021, 1, 17)]


#ostatnie 3 te same dni tygodnia (np.: 3 ostatnie poniedziałki)
days = []


for i in range(3):
    if i == 0:
        days.append(tomorrow - datetime.timedelta(days=7))
    else:
        i = i - 1
        days.append(days[i] - datetime.timedelta(days=7))


#godziny
hp = [23,24]
hm = [1,2]

for i in range(22):
    i += 1
    hp.append(i)
    hm.append(hm[i] + 1)





for i in range(len(list_id)):  # pętla do obliczen dla kazdego UID z osobna
    d = 0 + i

    bd.selecta7(d+1)
    last_location_table = getattr(bd, 'select7')
    last_location = []


    for row in last_location_table:
        last_location.append(row[1]) #uid
        last_location.append(row[2]) #lat
        last_location.append(row[3]) #lon
        last_location.append(row[4]) #timestamp


    for k in range(len(hp)): #petla dla danej godziny
        hour_mark = k




        uid_day = []
        lat_day = []
        lon_day = []
        timestamp_day = []


        for j in range(len(days)):  # pętla dla dni
            # do obliczen
            timestamp_all = []
            uid_all = []
            lat_all = []
            lon_all = []




            dm = days[j] - datetime.timedelta(days=1)
            dp = days[j] + datetime.timedelta(days=1)

            bd.selecta8(list_id[d], dm, dp, hp[k],hm[k])
            rekordy = getattr(bd, 'select8')
            #print(rekordy)

            # zapełenienie list rekordami z bazy dla danego UID i danej godziny
            for row in rekordy:
                timestamp_all.append(row[4])
                uid_all.append(row[1])
                lat_all.append(row[2])
                lon_all.append(row[3])


            # srednia (wybranie lokalizacji ktorej zakazony byl najczesciej danego dnia i godziny tego dnia)
            srednia_lat = 0
            srednia_lon = 0
            for i in range(len(lat_all)):
                srednia_lat = srednia_lat + lat_all[i]
                srednia_lon = srednia_lon + lon_all[i]

            if len(lat_all) != 0:
                srednia_lat = srednia_lat / len(lat_all)
                srednia_lon = srednia_lon / len(lon_all)

            # dopasowanie elementu nabliżej średniej i wskazanie indeksu elementu w liscie


            try:
                index_lat = np.argmin(np.abs(np.array(lat_all) - srednia_lat))
                index_lon = np.argmin(np.abs(np.array(lon_all) - srednia_lon))

                timestamp1 = timestamp_all[index_lon]
                q = timestamp1.replace(day = today.day + 1, minute = 0, second = 0)
                # print(q)
                # print(lat_all[index_lat])

                if q not in timestamp:
                    uid_day.append(uid_all[0])
                    lat_day.append(lat_all[index_lat])
                    lon_day.append(lon_all[index_lon])
                    timestamp_day.append(q)

            except:
                vvvv = 2

        # srednia (gdzie chory byl najczescie podczas tej samej godziny z 3 roznych dni)
        srednia_lat_two = 0
        srednia_lon_two = 0
        for i in range(len(lat_day)):
            srednia_lat_two = srednia_lat_two + lat_day[i]
            srednia_lon_two = srednia_lon_two + lon_day[i]

        if len(lat_day) != 0:
            srednia_lat_two = srednia_lat_two / len(lat_day)
            srednia_lon_two = srednia_lon_two / len(lon_day)



        # dopasowanie elementu nabliżej średniej i wskazanie indeksu elementu w liscie



            index_lat_two = np.argmin(np.abs(np.array(lat_day) - srednia_lat_two))
            index_lon_two = np.argmin(np.abs(np.array(lon_day) - srednia_lon_two))



            timestamp1 = timestamp_day[index_lon_two]
            q = timestamp1.replace(day=today.day + 1, minute=0, second=0)
            # print(q)
            # print(lat_all[index_lat])


            lat1 = float(lat_day[index_lat_two])
            lat2 = float(last_location[1])
            long1 = float(lon_day[index_lon_two])
            long2 = float(last_location[2])


            obl.dystans(lat1,lat2,long1,long2)


            distance = getattr(obl, 'd')

            distance_x = 1
            time_difference = 0.5

            try:
                distance_x = round((distance / 250), 0)
                distance = distance / distance_x
                time_difference = last_location[3] - timestamp1
                time_difference = (time_difference.seconds / 60) / 60
                time_difference = time_difference / distance_x


            except:
                print("za malo km")


            print(time_difference)

            if distance >= 250:
                if time_difference >= 1:
                    uid.append(uid_all[0])
                    lat.append(last_location[1])
                    lon.append(last_location[2])
                    timestamp.append(q)

                if today.weekday() > 4 and (today + one_day).weekday() > 4 or holiday[0] == 'true' and (today + one_day).weekday() > 4 or holiday[1] == 'true' or today > winter_break[0] and today <= winter_break[1]:
                    uid.append(uid_all[0])
                    lat.append(last_location[1])
                    lon.append(last_location[2])
                    timestamp.append(q)


            else:

                uid.append(uid_day[0])
                lat.append(lat_day[index_lat_two])
                lon.append(lon_day[index_lon_two])
                timestamp.append(q)















#for i in range (len(timestamp)):
#    bd.insert2(timestamp[i],uid[i],lat[i],lon[i])


bd.close()
