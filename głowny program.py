import math
import psycopg2
gps_x = []
gps_y = []
gps_xx = []
gps_yy = []
najczesciej = []

baza_baza = ""





petla_glowna_programu = True
while petla_glowna_programu:
    menu_glowne = int(input("0.Wyjscie\n1.Baza danych\n2.Siec Neuronowa\n3.Gdzie najczesciej byla osoba"))
    if menu_glowne == 0:
        petla_glowna_programu = False
    if menu_glowne == 1:
        

            

                
        if menu_baza == 0:
            menu_glowne = 33





    if menu_glowne == 3:

        try:
            baza_user = input("login: ")
            baza_haslo = input("haslo: ")
            connection = psycopg2.connect(user=baza_user,
                  password=baza_haslo,
                  host="127.0.0.1",
                  port="5432",
                  database="gps_db")

            cursor = connection.cursor()



            cursor = connection.cursor()
            select = "select * from gps2"

            cursor.execute(select)
            gps_rekordy = cursor.fetchall() 

            for row in gps_rekordy:
               
                gps_x.append(row[1])
                gps_y.append(row[2])
                gps_xx.append(row[1])
                gps_yy.append(row[2])
                
            gps_x.sort()
            gps_y.sort()
            x = int(len(gps_x) / 2)
            najczesciej.append(gps_x[x])
            najczesciej.append(gps_y[x])
            print("osoba najczesciej przebywala w miejscu X: ",gps_x[x],"Y: ",gps_y[x])






                
        except:
             print("blad")      





    if menu_glowne == 5:
        print(gps_x)
        sumax = 0
        sumay = 0
        srednia = []
        a = 0
        b = 0

        for i in range(len(gps_xx)):
            sumax = sumax + gps_xx[i]
            sumay = sumay + gps_yy[i]
        srednia.append(sumax / len(gps_xx))
        srednia.append(sumay / len(gps_yy))

        for i in range(len(gps_xx)):
            a = a + (gps_xx[i] - srednia[0]) * (gps_yy[i] - srednia[1] ) / (gps_xx[i] - srednia[0] + 0.1) ** 2

        b = srednia[1] - a * srednia[0]

        print(a,b)















        
    if menu_glowne == 2:
        xyzz = True

        #warstwa wejsciowa
        x_x90 = []
        x_y180 = []
        x = []
        wynik_x = 0
        wynik_y = 0



        #w - waga, x - wejscia, ww - wejscie * waga, y - wyjscie
        ww_a = []
        ww_b = []
        net = []
        yy = []


        w1_1 = []
        net1_1 = 0

        w1_2 = []
        net1_2 = 0

        y = []

        #warstwa ukryta
        w2_1 = []
        ww2_1 = []
        net2_1 = 0

        w2_2 = []
        ww2_2 =[]
        net2_2 = 0
        y2 = []

        #warstwa wyjsciowa
        w3 = []
        net3 = 0
        y3 = 0

        #w - waga, x - wejscia, ww - wejscie * waga, y - wyjscie
        ww_a = []
        ww_b = []
        net = []
        yy = []



        w1_1 = []
        net1_1 = 0

        w1_2 = []
        net1_2 = 0

        y = []

        #warstwa ukryta
        w2_1 = []
        ww2_1 = []
        net2_1 = 0

        w2_2 = []
        ww2_2 =[]
        net2_2 = 0
        y2 = []

        #warstwa wyjsciowa
        w3 = []
        net3 = 0
        y3 = 0


        with open('wagi1','r') as plik1:
            for line in plik1.readlines():
                l = line.strip().split('\t')
                w1_1.append(float(l[0]))
                w1_2.append(float(l[1]))
            plik1.close()

        with open('wagi2','r') as plik1:  
            for line in plik1.readlines()[1:100]:
                l = line.strip().split('\t')
                w2_1.append(float(l[0]))
                w2_2.append(float(l[1]))
                w3.append(float(l[2]))
            plik1.close()    







        while xyzz:
            xyz = int(input("1.X \n2.Y\n3.pokaz x y\n4.zapisz wagi do pliku\n5.wczytaj wagi\n0.wylacz"))
            if xyz == 0:
                xyzz = False
            if xyz == 1:
                for i in range(len(x_x90)):
                    x.append(x_x90[i] / 900)
            if xyz == 2:
                for i in range(len(x_y180)):
                    x.append(x_y180[i] / 1800)
              
            if xyz == 3:
                print("x: ",wynik_x)
                print("y: ",wynik_y)


            if xyz == 6:

                print(w1_1)
                print(w1_2)
                print(w2_1)
                print(w2_2)



                print(w3)




            

            




            #siec
            #warstwa wejsciowa


            for i in range(len(x)):
                ww_a.append(w1_1[i] * x[i])
                ww_b.append(w1_2[i] * x[i])

            for i in range(len(ww_a)):
                net1_1 = net1_1 + ww_a[i]
                net1_2 = net1_2 + ww_b[i]

            net.append(net1_1)
            net.append(net1_2)
            ww_a.clear()
            ww_b.clear()


            for i in range(len(net)): 
                y.append( (1 - math.exp(-net[i])) / (1 + math.exp(-net[i])) )

            net.clear()

            #warstwa ukryta
            for i in range(len(w2_1)):
                net.append( (y[0] * w2_1[i]) + (y[1] * w2_2[i] ) )



                
            for i in range(len(net)): 
                y2.append( (1 - math.exp(-net[i])) / (1 + math.exp(-net[i])) )

            net.clear()

            #warstwa wyjscia
            for i in range(len(y)):
                net3 = net3 + (y[i] * w3[i])
            #wynik

             
            y3 = ( (1 - math.exp(-net3)) / (1 + math.exp(-net3) ) )
            y3 = y3 
            print(y3)

            if xyz == 1:
                wynik_x = y3 * 900
            if xyz == 2:
                wynik_y = y3 * 1800




            x.clear()
            if xyz == 4:
                
                plik1 = open('wagi1', 'w')
                plik2 = open('wagi2', 'w')
                for i in range(len(w1_1)):
                    if i > 0:
                        plik1.write("\n")
                        plik1.write(str(w1_1[i]))
                        plik1.write('\t')
                        plik1.write(str(w1_2[i]))
                    else:
                        plik1.write(str(w1_1[i]))
                        plik1.write('\t')
                        plik1.write(str(w2_2[i]))
                    print(x)
                plik1.close()

                for i in range(len(w3)):

                        plik2.write("\n")
                        plik2.write(str(w2_1[i]))
                        plik2.write('\t')
                        plik2.write(str(w2_2[i]))
                        plik2.write('\t')
                        plik2.write(str(w3[i]))
                        plik2.write('\t')
                plik2.close()

                    
                




















                    ##algorytm propagacji wstecznej
                    









            
        
