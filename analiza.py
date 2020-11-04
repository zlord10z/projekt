from klasy import BazaDanych
import math
from datetime import date
data = date.today()



bd = BazaDanych()

#Dane 1 - by policzyc ile jest uid i liste jakie sa 
bd.selectuid()
uidzbazy = getattr(bd,'gpsrekordyid')
uid_petla = [] #lista nie powtarzajacych sie uid
#Dane 2 - analiza
al_x = []
al_y = []
al_a = []
al_b = []
osob_dzis = 0
dzien = 0
dni = []

for row in uidzbazy:
    uid_petla.append(row[0])

uid_petla = list(dict.fromkeys(uid_petla))


osob_dzis = len(uid_petla)
print(uid_petla)

#pobranie z bazy analizy
bd.selecta3()
bazaosoby = getattr(bd,'osobyrekordy')

#ile rzędów tyle dni od początku liczenia
for row in bazaosoby:
    dzien = dzien + 1

print(dzien)

#y osoby, x dni

for row in bazaosoby:
    al_y.append(row[1])
    dni.append(row[0])

al_y.append(osob_dzis)
dzien = len(dni) + 1

for i in range(dzien):
    al_x.append(i+1)
    
print(al_x)
print(al_y)


#analiza liniowa liczona dopiero od 3 rzedow
if dzien > 2:

    al_sumax = 0
    al_sumay = 0
    al_srednia = []
    
    al_a1 = 0
    al_a2 = 0
    

    for i in range(len(al_x)):
        al_sumax = al_sumax + al_x[i]
        al_sumay = al_sumay + al_y[i]
    al_srednia.append(al_sumax / len(al_x))
    al_srednia.append(al_sumay / len(al_y))
    print(al_srednia)

    for i in range(len(al_x)):
        al_a1 = al_a1 + (al_x[i] - al_srednia[0]) * (al_y[i] - al_srednia[1])
        al_a2 = al_a2 + (al_x[i] - al_srednia[0]) ** 2

    al_a = al_a1 / al_a2

    al_b = al_srednia[1] - al_a * al_srednia[0]

    print(al_a,al_b)

else:
    al_a = 0
    al_b = 0

bd.insert3(osob_dzis,data, al_a, al_b)

bd.close()
