from klasy111 import BazaDanych
import numpy as np
import datetime



bd = BazaDanych()

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
pkl = []
p = 0
#by policzyc ile jest uid i liste jakie sa (Dane 1)
for row in uidzbazy:
    uid_petla.append(row[0])

uid_petla = list(dict.fromkeys(uid_petla))





for i in range( len(uid_petla) ):                 #pętla do obliczen dla kazdego UID z osobna
    d = 0 + i
    
    for j in range(24):           #pętla do obliczen dla kazdej godziny
        m = 0 + j
        g = 1 + j

        bd.selecta( uid_petla[d],m,g)
        #bd.selecta( uid_petla[d],1,24)
        rekordy = getattr(bd,'gpsrekordy123')
        
        timestamp_all =[]
        uid_all = []
        lat_all = []
        lon_all = []
        
       #zapełenienie list rekordami z bazy dla danego UID i danej godziny
        for row in rekordy:
            timestamp_all.append(row[4])
            uid_all.append(row[0])
            lat_all.append(row[2])
            lon_all.append(row[3])

            #srednia
            srednia_lat = 0
            srednia_lon = 0
            for i in range(len(lat_all)):
                srednia_lat = srednia_lat + lat_all[i]
                srednia_lon = srednia_lon + lon_all[i]


            if len(lat_all) != 0:
                srednia_lat = srednia_lat / len( lat_all )
                srednia_lon = srednia_lon / len( lon_all )
                        
            #print(srednia_lat)

            #dopasowanie elementu nabliżej średniej i wskazanie indeksu elementu w liscie

            index_lat = np.argmin(np.abs(np.array(lat_all)-srednia_lat))
            index_lon = np.argmin(np.abs(np.array(lon_all)-srednia_lon))

            #print(timestamp_all[index_lon])
            
            timestamp1 = timestamp_all[index_lon]
            q = timestamp1.replace(minute = 00,second = 00)
            #print(q)
            #print(lat_all[index_lat])
            if q not in timestamp:
                uid.append( uid_all[0])
                lat.append( lat_all[index_lat])
                lon.append( lon_all[index_lon])
                timestamp.append(q)

#usuwanie duplikatow
#uid = list(dict.fromkeys(uid))
#lat = list(dict.fromkeys(lat))
#lon = list(dict.fromkeys(lon))
#timestamp = list(dict.fromkeys(timestamp))

print(uid)
print(lat)
print(lon)
print(timestamp)

#primary key for route
bd.selecta4()
pkrf = getattr(bd,'pkrf')
for row in pkrf:
    pkl.append(row[0])
p = len(pkl)
    

#test
#for i in range (len(timestamp)):
#    print(timestamp[i])

for i in range (len(timestamp)):
    bd.insert(lat[i],lon[i],timestamp[i],uid[i])
print(len(timestamp))
print(len(uid))
print(len(lat))
print(len(lon))
