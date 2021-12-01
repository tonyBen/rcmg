# -*- coding: utf-8 -*-
"""
------------------------------------------------
rcmg..scheduleTest
------------------------------------------------
Author: Tony Ben (email: nanjinghhu@vip.qq.com)
Create: 2020-07-06
------------------------------------------------
ChangeLog
------------------------------------------------
Date        |Ticket     |Describe   
------------------------------------------------

------------------------------------------------
"""
#from pytz import utc
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.events import EVENT_EXECUTOR_ADDED
from apscheduler.executors.asyncio import AsyncIOExecutor
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.cron import CronTrigger
from apscheduler.events import EVENT_JOB_EXECUTED
import datetime
import asyncio
import socket

def get_Host_name_IP():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        print("Hostname :  ",host_name)
        print("IP : ",host_ip)
    except:
        print("Unable to get Hostname and IP")

    # Driver code
get_Host_name_IP() #Function call
jobstores={
    'default':SQLAlchemyJobStore(url='postgresql://postgres:postgres@nancloud-onprem-06.calix.local:5432/rcmg',tablename='sch_jobs')
}
executors = {
    'default': ThreadPoolExecutor(20),
    'processpool': ProcessPoolExecutor(5)
}
job_defaults = {
    'coalesce': False,
    'max_instances': 3
}
#schd=AsyncIOScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults, timezone=utc)
#schd=BlockingScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults, timezone=utc)
def my_job(test=None):
    print("sch:%s"%test)

def job_execute(event):
    print("=====\n job execute:\n code==>{}\n job.id==>{} \n jobstore==>{} ".format(event.code,event.job_id,event.jobstore))


def interval_func(message):
    print("Now:{}".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    print("Interval Fun:%s"%message)
async def async_fun(message):
    print("Now:{}".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    print("Async Fun:%s"%message)

#job=schd.add_job(my_job,'interval',seconds=1,name="testJob",id='123')
#schd.print_jobs()
#print(schd.print_jobs())
#job.remove()
#schd.start()
first_executor=AsyncIOExecutor()
schd=AsyncIOScheduler(jobstores=jobstores,executors=executors,job_defaults=job_defaults)
schd.start()
schd.add_listener(job_execute,EVENT_JOB_EXECUTED)
if schd.get_job("interval_func_10s"):
    schd.remove_job("interval_func_10s","default")
schd.add_job(interval_func,'interval',args=["Normal Execute every 10s"],seconds=10,id="interval_func_10s")
trigger=IntervalTrigger(seconds=5)
if schd.get_job("interval_func_5s"):
    schd.remove_job("interval_func_5s","default")

#schd.add_job(async_fun,trigger,args=["Async Execute every 5s"],seconds=5,id="interval_func_5s")
print("Start:{}".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
asyncio.get_event_loop().run_forever()




schd.shutdown()
