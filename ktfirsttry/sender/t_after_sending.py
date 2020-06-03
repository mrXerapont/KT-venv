import psycopg2
from datetime import datetime, timedelta
import calendar
from django import db
db.connections.close_all()

class AfterSending:
    
    def __init__(self, id):
        self.id = id       
  
    
    def edit_task(self, days, dtime):
        #if monthly - find days in month
        if days == 30:
            days = calendar.monthrange(dtime.year, dtime.month)[1]                               
        newdate = dtime  + timedelta(days)
        
        try:
            conn, curs = get_connection()
            #update request string - changing date
            update_request = "UPDATE sender_snd SET dtime='%s' WHERE id=%s"%(newdate, self.id)                   
            curs.execute(update_request)
            conn.commit()
        except Exception as e:
            print(e)
        finally:
            curs.close()
            conn.close()
        
        
    def delete_task(self):
        #task done - delete task        
        try:            
            conn, curs = get_connection()
            delete_request = 'DELETE FROM sender_snd WHERE id=%s'%(self.id)
            curs.execute(delete_request)              
            conn.commit()
        except Exception as e:
            print(e)
        finally:
            curs.close()
            conn.close()            
        
    def unsaccess_task(self):
        #if task unsaccessed - change description
        try:
            conn, curs = get_connection()
            update_request = "UPDATE sender_snd SET description='%s' WHERE id=%s"%('Задание не выполнено!', self.id)        
            print(update_request)
            curs.execute(update_request)
            conn.commit()
        except Exception as e:
            print(e)
        finally:    
            curs.close()
            conn.close()                   
        
        
def get_connection():
    connection = psycopg2.connect(dbname='django_db', user='user_name', password='password', host='localhost', isolation_level=None)
    cursor = connection.cursor()
    return connection, cursor