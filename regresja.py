import psycopg2
import math

al_x = []
al_y = []
al_a = []
al_b = []
osob_dzis = 0
dzien = 0
dni = []

connection = psycopg2.connect(user="user_program",
                                  password="mragorp",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="gps_db")
cursor_al1 = connection.cursor()
select_al1 = "select * from gps_id"
cursor_al1.execute(select_al1)
gps_rekordy_al1 = cursor_al1.fetchall() 



for row in gps_rekordy_al1:
    osob_dzis = osob_dzis + 1



cursor_al2 = connection.cursor()
select_al2 = "select * from ile_osob"
cursor_al2.execute(select_al2)
gps_rekordy_al2 = cursor_al2.fetchall() 

for row in gps_rekordy_al2:
    al_y.append(row[0])

al_y.append(osob_dzis)

for row in gps_rekordy_al2:
    dni.append(row[1])

dzien = len(dni) + 1





for i in range(dzien):
    al_x.append(i+1)
    
print(al_x)
print(al_y)


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


cursor_al2.execute("INSERT INTO ile_osob (liczba, dzien, x, y) VALUES(%s, %s, %s, %s)", (osob_dzis, dzien, al_a, al_b) )
connection.commit()





