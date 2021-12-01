# -*- coding: utf-8 -*-
"""
------------------------------------------------
rcmg.util.database.redis_sentinel_utils
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
from redis.sentinel import Sentinel
from common.global_constants import *

class RedisSentinelUtils(object):
    sentinel=None
    master=None
    slave=None

    def __init__(self,_conf):
        _host_list=[]
        for _h in _conf['host'].split(','):
            _tmp=_h.split(":")
            if len(_tmp)==1:
                _host_list.append((_tmp[0],DEFAULT_REDIS_SENTINEL_PORT))
            else:
                _host_list.append((_tmp[0],_tmp[1]))
        logging.info("-"*80)
        logging.info("Begin Initialize Redis Sentinel Service %s@%s/%s",
                     _conf['master_name'],_conf['host'],_conf['index_name'])
        logging.info("-"*80)
        self.sentinel = Sentinel(_host_list,socket_timeout=0.1)
        logging.info("RedisSentinel Master:%s",self.sentinel.discover_master(_conf['master_name']))
        logging.info("RedisSentinel Slaves:%s",self.sentinel.discover_slaves(_conf['master_name']))
        self.master = self.sentinel.master_for(_conf['master_name'], socket_timeout=0.1,password=_conf['master_auth'])
        self.slave = self.sentinel.slave_for(_conf['master_name'], socket_timeout=0.1,password=_conf['master_auth'])

    def hset(self,key,value):
        self.master.hset(key,value)
        return True

    def hget(self,key):
        return self.slave.hget(key)

    def hgetall(self,name):
        return self.slave.hgetall(name)

    def set(self,key,value):
        self.master.set(key,value)
        return True

    def get(self,key):
        return self.slave.get(key)

    def info(self,sname=None):
        logging.info("-------get info ---%s",sname)
        if sname:
            if sname == "master":
                return self.master.info()
            else:
                return self.slave.info()
        return {"master":self.master.info(),"slave":self.slave.info()}


    def get_master(self):
        return self.master

    def get_slave(self):
        return self.slave

    def test(self):
        self.master.hset('50-CXNK005D3F17','2018-07-10','CXNK0057A67C_1566190800.csv')
        self.master.hset('50-CXNK005D3F17','2018-07-11','CXNK0057A67C_1566190811.csv')
        logging.info(self.slave.exists('50-CXNK005D3F17'))
        logging.info(self.slave.hgetall('50-CXNK005D3F17'))
        for keys in self.slave.hgetall('50-CXNK005D3F17'):
            logging.info("===%s",keys)

        for key, value in (('A', '1'), ('B', '2'), ('C', '3')):
            self.master.set(key,value)
        for key in self.slave.scan_iter():
            logging.info(key)