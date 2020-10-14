from errors import Bledy
import psycopg2

b1 = Bledy()



class BazaDanych:
  


    try:
        connection = psycopg2.connect(user="user_program",
                              password="mragorp",
                              host="127.0.0.1",
                              port="5432",
                              database="gps_db")





    except:
        b1.blad()


    def selectuid(self):

        cursor2 = self.connection.cursor()
        select2 = "SELECT * FROM test_201" 
        cursor2.execute(select2)
        self.gpsrekordyid = cursor2.fetchall()


    def select(self, x):

        cursor2 = self.connection.cursor()
        cursor_al1 = self.connection.cursor()
        
        self.x = ""
        x = str(x)
        string = str("SELECT * FROM test_201 WHERE user_uid = '"+x+"'")
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
        
        string = str("SELECT * FROM test_201 WHERE user_uid = '"+str(x)+"' AND now() - interval '"+str(m)+" hours' > created_on AND now() - interval '"+str(p)+" hours' < created_on")
        cursor_al1.execute(string)
        
        self.gpsrekordy123 = cursor_al1.fetchall()
        
        #print(self.gpsrekordy123)

    def selecta2(self, x, godz):
        cursor2 = self.connection.cursor()
        cursor_al2 = self.connection.cursor()
        
        self.x = ""
        self.godz = ""
        self.wx = "\"created_on\"" 
        
        string2 = str("SELECT * FROM test_202 WHERE user_uid = '"+str(x)+"' AND "+str("\"created_on\"" )+"::time = '"+str(godz)+":00:00'")
        cursor_al2.execute(string2)
        
        self.gpsrekordy1234 = cursor_al2.fetchall()
        print(self.gpsrekordy1234)


    def selecta3(self):
        cursor3 = self.connection.cursor()
        cursor_al3 = self.connection.cursor()
        
        string3 = str("SELECT * FROM test_204")
        cursor_al3.execute(string3)
        
        self.osobyrekordy = cursor_al3.fetchall() 

        #print(self.osobyrekordy)

    
    

    def insert(self, b_ts, b_id, b_lat, b_lon):
        cursor_al = self.connection.cursor()
        

        cursor_al.execute("INSERT INTO test_202 (created_on, user_uid, lat, lon) VALUES(%s, %s, %s, %s)", (b_ts, b_id, b_lat, b_lon) )
        self.connection.commit()


    def insert2(self, b_ts, b_id, b_lat, b_lon):
        cursor_al = self.connection.cursor()
        

        cursor_al.execute("INSERT INTO test_203 (created_on, user_uid, lat, lon) VALUES(%s, %s, %s, %s)", (b_ts, b_id, b_lat, b_lon) )
        self.connection.commit()

    
    def insert3(self, osob, dzien, al_a, al_b):
        cursor_al = self.connection.cursor()
    
        cursor_al.execute("INSERT INTO test_204 (ile_osob, dzien, a, b) VALUES(%s, %s, %s, %s)", (osob, dzien, al_a, al_b) )
        self.connection.commit()
        

#bd = BazaDanych()
#bd.selecta3()
#bd.selecta2(283712,12)


        #select1 = "SELECT * FROM test_201 WHERE ts < now() - interval '24 hours' "



    







        

