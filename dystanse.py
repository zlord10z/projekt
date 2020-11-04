from klasy import Obliczenia
from klasy import BazaDanych
from datetime import date
from errors import Bledy

b1 = Bledy()


#klasy.dystans(10.4444,10.3421,40.5678,40.8194)
bd = BazaDanych()
obl = Obliczenia()

#Dane 1 - by policzyc ile jest uid i liste jakie sa 
bd.selectuid()
uidzbazy = getattr(bd,'gpsrekordyid')
uid_petla = [] #lista nie powtarzajacych sie uid

for row in uidzbazy:
    uid_petla.append(row[0])

uid_petla = list(dict.fromkeys(uid_petla))
inf_l = 0
inf = ""
inf_id = 0

lat = []
long = []

timestamp = date.today()
d_inf = 0
d_noinf = 0


l = []




#dla zakazonego/niezakazonego
for i in range(2):
    inf_l += i

    if inf_l == 0:
       inf = "= \'infected"
    if inf_l == 1:
       inf = "!= \'infected"

#dla kazdego id
    for i in range(len(uid_petla)):
        inf_id = uid_petla[i]

        bd.selecta5(inf,inf_id)
        rekordy = getattr(bd,'select5')
        lat = []
        long = []
        
        for row in rekordy:
            lat.append(row[3])
            long.append(row[4])

        for i in range(len(lat) - 1):
            lat1 = float(lat[i])
            lat2 = float(lat[i+1])
            long1 = float(long[i])
            long2 = float(long[i+1])

            obl.dystans(lat1,lat2,long1,long2)

            if inf_l == 0:
                d_inf += getattr(obl,'d')

            if inf_l == 1:
                d_noinf += getattr(obl,'d')


print(round(d_inf,2),"km")
print(round(d_noinf,2),"km")


            
try:
    bd.insert5(round(d_inf,2),round(d_noinf,2),timestamp)
except:
    b1.blad() 

bd.close()
        
        





        

    
    

