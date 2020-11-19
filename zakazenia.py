from klasy import Obliczenia
from klasy import BazaDanych
from datetime import date
from errors import Bledy

b1 = Bledy()


bd = BazaDanych()
obl = Obliczenia()

bd.selectuid()
uidzbazy = getattr(bd,'gpsrekordyid')
uid_petla = [] #lista nie powtarzajacych sie uid

for row in uidzbazy:
    uid_petla.append(row[0])

uid_petla = list(dict.fromkeys(uid_petla))

infection_loop = 0
infection = ''

infected_id = []
infected_lat = []
infected_long = []

noninfected_id = []
noninfected_lat = []
noninfected_long = []
inf_i = 0


#dla zakazonego/niezakazonego
for i in range(2):
    infection_loop += i

    if infection_loop == 0:
       infection = "= \'infected"
    if infection_loop == 1:
       infection = "!= \'infected"


    # dla kazdego id
    for i in range(len(uid_petla)):
        user_id = uid_petla[i]

        bd.selecta6(user_id, infection)
        rekordy = getattr(bd, 'select6')

        if infection_loop == 0:

            for row in rekordy:
                infected_id.append(row[2])
                infected_lat.append(row[3])
                infected_long.append(row[4])


        else:
            for row in rekordy:

                noninfected_id.append(row[2])
                noninfected_lat.append(row[3])
                noninfected_long.append(row[4])



        for i in range(len(infected_lat)):
            inf_i += i
            try:
                for j in range(len(noninfected_lat)):
                    lat1 = float(infected_lat[inf_i])
                    lat2 = float(noninfected_lat[j])
                    long1 = float(infected_long[inf_i])
                    long2 = float(noninfected_long[j])

                    obl.dystans(lat1, lat2, long1, long2)
                    distance = getattr(obl, 'd')
                    #zamiana na metry
                    distance = distance * 1000


                    print(distance)
                    #if distance < 100:
                    if distance < 1000:
                        print("user",noninfected_id[j],"był w odleglosci",distance,"metrow od zakazonego")



            except:
                print("koniec jednej z list")







