import psycopg2
from datetime import datetime, timedelta
from sender.t_sender import Sender
from django import db
db.connections.close_all()


class TaskFinder:

    def find():
        #DB connection
       # conn = sqlite3.connect('../db.sqlite3')
        conn = psycopg2.connect(dbname='django_db', user='user_name', password='password', host='localhost')
        curs = conn.cursor()
    
        #current date\time
        now = datetime.now()
        #date\time + 5 minutes
        delta = datetime.now() + timedelta(minutes=5)    
        
        #Create sql req
        read_info = "SELECT * FROM sender_snd WHERE dtime BETWEEN '%s' AND '%s';"%(now,delta)
        
        #exec request        
        try:
            curs.execute(read_info)                
            rows = {}            
            rows = curs.fetchall()            
        finally:
            curs.close()
            conn.close()
            
        #put results to sender        
        for row in rows:
            Sender(row[0], row[1], row[2], row[3], row[4], row[5]).sending()          
     
        
        
        

    if __name__ == '__main__':
        find()



    