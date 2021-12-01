# -*- coding: utf-8 -*-
"""
------------------------------------------------
rcmg.util.database.redis_util
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
import redis
from common.global_constants import *
class RedisCacheUtils(object):
    conn_pool=None
    def __init__(self,_conf):
        logging.info("Begin init Redis")
        try:
            self.conn_pool=redis.ConnectionPool(host=_conf['host'],
                                                db=_conf['index_name'],
                                                username=_conf['master_name'],
                                                password=_conf['master_auth'])
            r = redis.Redis(connection_pool=self.conn_pool)
        except Exception as err:
            logging.error("Inlitilize Redis Connection Failed :%s",err)

        pass


