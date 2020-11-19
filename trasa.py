from klasy import BazaDanych
from klasy import Api
from klasy import Obliczenia
import numpy as np
import datetime


api = Api()
bd = BazaDanych()
obl = Obliczenia()

#Dane 1 - by policzyc ile jest uid i liste jakie sa 
bd.selectuid()
uidzbazy = getattr(bd,'gpsrekordyid')
uid_petla = [] #lista nie powtarzajacych sie uid

d = 0
uid_all = []
lat_all = []
lon_all = []

uid = []
lat = []
lon = []
timestamp = []
list_latlong = []

list_lat = []
list_long = []
list_timestamp = []
list_id = []
list_from_api = []


p = 0
#by policzyc ile jest uid i liste jakie sa (Dane 1)
for row in uidzbazy:
    uid_petla.append(row[0])

uid_petla = list(dict.fromkeys(uid_petla))





for i in range( len(uid_petla) ):                 #pętla do obliczen dla kazdego UID z osobna
    d = 0 + i
    timestamp_all =[]
    uid_all = []
    lat_all = []
    lon_all = []
    
    
    #for j in range(24):           #pętla do obliczen dla kazdej godziny
    for j in range(48):
        m = 0 + j
        g = 2 + j

        bd.selecta( uid_petla[d],m,g)
        #bd.selecta( uid_petla[d],1,24)
        rekordy = getattr(bd,'gpsrekordy123')
        



        

                
        
       #zapełenienie list rekordami z bazy dla danego UID i danej godziny
        for row in rekordy:
            timestamp_all.append(row[4])
            uid_all.append(row[0])
            lat_all.append(row[2])
            lon_all.append(row[3])

            #srednia
            average_lat = 0
            average_lon = 0
            
            for i in range(len(lat_all)):
                average_lat = average_lat + lat_all[i]
                average_lon = average_lon + lon_all[i]

            if len(lat_all) != 0:
                average_lat = average_lat / len( lat_all )
                average_lon = average_lon / len( lon_all )


            #dopasowanie elementu nabliżej średniej i wskazanie indeksu elementu w liscie

            index_lat = np.argmin(np.abs(np.array(lat_all)-average_lat))
            index_lon = np.argmin(np.abs(np.array(lon_all)-average_lon))
            
            #print(timestamp_all[index_lon])
            
            timestamp1 = timestamp_all[index_lon]
            #q = timestamp1.replace(hour = 00,minute = 00,second = 00)
            q = datetime.datetime.date(timestamp1)
           

            
            #if q not in timestamp:
                
            uid.append( uid_all[0])
            lat.append( lat_all[index_lat])
            lon.append( lon_all[index_lon])
            timestamp.append(q)
            lat_all = []
            lon_all = []
    
    lat = list(dict.fromkeys(lat))
    lon = list(dict.fromkeys(lon))         
                    
    
    #stworzenie jednej listy
    for i in range(len(lat)):
        

                            
        to_list = []
        to_list.append(lat[i])
        to_list.append(lon[i])
        list_latlong.append(to_list)
        
        
              
   
   

    # posortowanie aby droga "niewracala" sie
    
    list_latlong = sorted(list_latlong, key=lambda x: x[0])

 
    
    #print(list_latlong)

    # petla aby uzyskac waypointy
    for i in range(len(list_latlong) - 1):
        obl.dystans(float(list_latlong[i][0]), float(list_latlong[i+1][0]), float(list_latlong[i][1]), float(list_latlong[i + 1][1]) )
        warunek_1 = getattr(obl,'d')
        print(warunek_1)
        #aby nie liczyc drogi dla punktow oddalonych o wiecej niz 10 km
        if warunek_1 <= 10:

            list_from_api = []

            api.api_get_waypoints(list_latlong[i][0], list_latlong[i][1], list_latlong[i + 1][0], list_latlong[i + 1][1] )

            list_from_api = getattr(api,"l")
        
    list_latlong = []

    try:

            #zapełnienie do formatu do bazy
        for i in range(len(list_from_api)):
            #ograniczenie dokladnosci punktow do co piatego
            if i % 5 == 0 :
             
                
                list_lat.append(list_from_api[i][0])
                list_long.append(list_from_api[i][1])
                list_id.append(uid_petla[d])
                list_timestamp.append(timestamp[0])

    except:
        print("brak")

    list_from_api = [[]]


             
        

        #wyczysczenie list

    lat = []
    long = []
    list_latlong = []
            

uid = []
timestamp = []




#for i in range (len(timestamp)):
#    bd.insert(list_lat[i],list_lon[i],list_timestamp[i],list_id[i])


bd.close()
