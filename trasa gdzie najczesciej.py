import datetime
import numpy as np
import psycopg2
import time
import datetime
from datetime import date

connection = psycopg2.connect(user="",
                                  password="",
                                  host="",
                                  port="5432",
                                  database="")


cursor_al1 = connection.cursor()
select_al1 = "SELECT * FROM gps_101 WHERE ts < now() - interval '24 hours' " 



cursor_al1.execute(select_al1)


gps_rekordy_al1 = cursor_al1.fetchall() 

today = date.today()

r = today.year
m = today.month
d = today.day 
print(r,m,d)

g = list(range(0,24))
g_m = [23] + g
g_p = list(range(1,24))
g_p.append(1)



t = []
tt = []

id_1 = []
idd = []
x = []
xx = []
y = []
yy = []
do_bazy_x = []
do_bazy_y = []
do_bazy_timestamp = []
do_bazy_id = []


for row in gps_rekordy_al1:
    idd.append(row[0])
    xx.append(row[1])
    yy.append(row[2])
    tt.append(row[3])

print(g_m)
print(g)
print(g_p)

#id_petla = list(dict.fromkeys(idd))
#roznica_petla = len(idd) - len(id_petla)
#for i in range (roznica_petla):
#    id_petla.append(0)


    


    
for j in range(len(tt)):
    for i in range(len(g)):    
        
        
    
        
        if tt[j] >= datetime.datetime(r, m, d, g_m[i], 0, 0):


            if tt[j] <= datetime.datetime(r, m, d, g_p[i], 0, 0):
                
                print(tt[j])
                id_1.append(idd[j])
                x.append(xx[j])
                y.append(yy[j])
                t.append(tt[j])
                
               
#srednia
srednia_x = 0
srednia_y = 0

for i in range(len(x)):
    srednia_x = srednia_x + x[i]
    srednia_y = srednia_y + y[i]


if len(x) != 0:
    srednia_x = srednia_x / len(x)
    srednia_y = srednia_y / len(y)

#dopasowanie elementu nabliżej średniej

    index_x = np.argmin(np.abs(np.array(x)-srednia_x))
    index_y = np.argmin(np.abs(np.array(y)-srednia_y))

    gg = g[i]

    do_bazy_x.append(x[index_x])
    do_bazy_y.append(y[index_y])
    do_bazy_timestamp.append(datetime.datetime(r, m, d, gg, 0, 0))
    do_bazy_id.append(idd[1])
    

if srednia_x != 0:
    cursor_al1 = connection.cursor()

    cursor_al2.execute("INSERT INTO gps_111 (ID, x, y, ts) VALUES(%s, %s, %s, %s)", (do_bazy_id, do_bazy_x, do_bazy_y, do_bazy_timestamp) )
    connection.commit()
    print("ok")
                                                                         
    



    srednia_x = 0
    srednia_y = 0
    id_1.clear()
    t.clear()
    x.clear()
    y.clear()

print(do_bazy_x)




