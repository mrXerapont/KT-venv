from __future__ import absolute_import
from celery import Celery
#from celery import shared_task
from celery.task.schedules import crontab
from celery.decorators import periodic_task
#from celery.utils.log import get_task_logger

from sender.t_finder import TaskFinder
#from t_finder import TaskFinder
#import importlib
import os
import sys
#import  subprocess


sys.path.append(os.getcwd())


@periodic_task(run_every=crontab(minute='*/5'))
def notification():
    #subprocess.Popen([sys.executable, 't_finder'])
    #module = importlib.import_module('t_finder')
    #module.run()
    #print('ололо')
    TaskFinder.find()
    # DB connection
  
    
    
    
# =============================================================================
# '''
#     conn = sqlite3.connect('ktfirsttry/sender/db.sqlite3')
#     curs = connection.cursor()
#     delete_request = "DELETE FROM sender_snd WHERE id>8"
#     curs.execute(delete_request)
#     connection.commit()
#     connection.close()
# '''
# =============================================================================
