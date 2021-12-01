# -*- coding: utf-8 -*-
"""
------------------------------------------------
rcmg.common.web_service
------------------------------------------------
Author: Tony Ben (email: nanjinghhu@vip.qq.com)
Create: 2020-07-03
------------------------------------------------
ChangeLog
------------------------------------------------
Date        |Ticket     |Describe   
------------------------------------------------

------------------------------------------------
"""
import logging
from common.global_constants import *


class WebService(object):
    def __init__(self):
        for x in global_config_dict:
            logging.info("%s:%s",x,global_config_dict[x])


def verify_postgres():
    logging.info(global_config_dict['database'].query("select * from pg_database"))
    logging.info(global_config_dict['database'].query("select now()"))
    logging.info(global_config_dict['database'].query("select * from pg_tables"))
    global_config_dict['database'].exec("insert into cloudstats values('obtype','obname','obactualsize','obdisksize','obrowcount','2020-07-01')")
    logging.info(global_config_dict['database'].query("select * from cloudstats"))
    global_config_dict['database'].exec("insert into cloudstats values('obtype2','obname2','obactualsize','obdisksize','obrowcount')")
    logging.info(global_config_dict['database'].query("select * from cloudstats"))
    global_config_dict['database'].exec("truncate table cloudstats")
    logging.info(global_config_dict['database'].query("select * from cloudstats"))
    global_config_dict['database'].close()

    logging.info(global_config_dict['redis'].info())
    logging.info(global_config_dict['redis'].get_master().keys())


    global_config_dict["email"].sendEmail("test","test","tony.ben@calix.com,nanjinghhu@vip.qq.com")
    #global_config_dict["email"].sendEmail("test2","test2","tony.ben@calix.com,nanjinghhu@vip.qq.com",[os.path.join("C","Users","tben","Pictures","qq.jpg")])
    global_config_dict["email"].sendEmail("test2","test2","tony.ben@calix.com,nanjinghhu@vip.qq.com",["C:\\Users\\tben\\Pictures\\qq.jpg"])