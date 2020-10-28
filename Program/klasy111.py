from errors import Bledy
import psycopg2

b1 = Bledy()


se1 = "select public.user.user_id, public.user.user_uid, public.location.latitude, public.location.longtitude, public.user_location.time_stamp from public.user join public.user_location on public.user.user_id = public.user_location.user_id join public.location on public.user_location.location_id = public.location.location_id "



class BazaDanych:
  


    try:
        connection = psycopg2.connect(user="maurycy",
                              password="mragorp",
                              host="192.168.1.140",
                              port="5432",
                              database="covid")





    except:
        b1.blad()


    def selectuid(self):

        cursor2 = self.connection.cursor()
        select2 = "select public.user.user_id from public.user"  
        cursor2.execute(select2)
        self.gpsrekordyid = cursor2.fetchall()


    def select(self, x):

        cursor2 = self.connection.cursor()
        cursor_al1 = self.connection.cursor()
        
        self.x = ""
        x = str(x)
        string = str(se1 + "WHERE user_id = '"+x+"'")
        cursor_al1.execute(string)
        
        self.gpsrekordy = cursor_al1.fetchall()

    def pokaz(self):
        print(self.gpsrekordy)



    def selecta(self, x, m, p):
        cursor2 = self.connection.cursor()
        cursor_al1 = self.connection.cursor()
        
        self.x = ""
        self.m = ""
        self.p = ""
        self.m = str(self.m)
        self.p = str(self.p)
        
        #string = str(se1 + "WHERE public.user.user_id = '"+str(x)+"' AND now() - interval '"+str(m)+" hours' > time_stamp AND now() - interval '"+str(p)+" hours' < time_stamp")
        string = str(se1 + "WHERE public.user.user_id = '"+str(x)+"'")
        cursor_al1.execute(string)
        
        
        self.gpsrekordy123 = cursor_al1.fetchall()
        
        print(self.gpsrekordy123)

    def selecta2(self, x, godz):
        cursor2 = self.connection.cursor()
        cursor_al2 = self.connection.cursor()
        
        self.x = ""
        self.godz = ""
        self.wx = "\"created_on\"" 
        #tutaj select z trasy do forecasta
        string2 = str("SELECT * FROM route WHERE user_id = '"+str(x)+"' AND "+str("\"route_time\"" )+"::time = '"+str(godz)+":00:00'")
        cursor_al2.execute(string2)
        
        self.gpsrekordy1234 = cursor_al2.fetchall()
        


    def selecta3(self):
        cursor3 = self.connection.cursor()
        cursor_al3 = self.connection.cursor()
        
        string3 = str("SELECT * FROM linear_function")
        cursor_al3.execute(string3)
        
        self.osobyrekordy = cursor_al3.fetchall() 

        #print(self.osobyrekordy)

    

    def selecta4(self):
        #do obliczenia route_id(pk), i forecast_id(pk)
        cursor4 = self.connection.cursor()
        cursor_al4 = self.connection.cursor()
        
        string4 = str("SELECT route_id,forecast_id FROM route,forecast")
        cursor_al4.execute(string4)
        
        self.pkrf = cursor_al4.fetchall() 


        

    

    def insert(self, b_lat, b_lon,b_ts, b_id):
        cursor_al = self.connection.cursor()
        

        cursor_al.execute("insert into route(route_lat,route_lon,route_time,user_id) values (%s, %s, %s, %s)", (b_lat, b_lon, b_ts, b_id)  )
        self.connection.commit()


    def insert2(self, b_ts, b_id, b_lat, b_lon):
        cursor_al = self.connection.cursor()
        

        cursor_al.execute("insert into forecast(forecast_lat,forecast_long,forecast_time,user_id,location_id) values (%s, %s, %s, %s, %s)", (b_lat, b_lon, b_ts, b_id, b_id) )
        self.connection.commit()

    
    def insert3(self, osob, dzien, al_a, al_b):
        cursor_al = self.connection.cursor()
    
        cursor_al.execute("INSERT INTO linear_function (day, amount_of_people, a_coefficient, b_coefficient) VALUES(%s, %s, %s, %s)", (dzien, osob, al_a, al_b) )
        self.connection.commit()
        

#bd = BazaDanych()
#bd.selecta3()
#bd.selecta2(283712,12)


        #select1 = "SELECT * FROM test_201 WHERE ts < now() - interval '24 hours' "



    







        

