# -*- coding: utf-8 -*-
"""
------------------------------------------------
rcmg.util.database.PostgresDatabaseUtils
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
from psycopg2.pool import *
import logging
from util.database_utils import DatabaseUtils
from common.global_constants import *


class PostgresDatabaseUtils(DatabaseUtils):
    connection_pool=None

    def __init__(self,_conf):
        logging.info("-"*80)
        logging.info("Begin Initialize Postgres Connection %s@%s:%s/%s",
                     _conf['username'],_conf['host'],_conf['port'],_conf['dbname'])
        logging.info("-"*80)
        _min_conn=DEFAULT_DATABASE_CONNECTION_POOL_MIN if not "min_conn" in _conf.keys() else  _conf['min_conn']
        _max_conn=DEFAULT_DATABASE_CONNECTION_POOL_MAX if not "_max_conn" in _conf.keys() else  _conf['_max_conn']
        try:
            self.connection_pool=psycopg2.pool.SimpleConnectionPool(_min_conn,
                                                                    _max_conn,
                                                                    user=_conf['username'],
                                                                    password=_conf['password'],
                                                                    host=_conf['host'],
                                                                    port=_conf['port'],
                                                                    database=_conf['dbname'])

        except (Exception, psycopg2.Error) as error :
            logging.error("Initialize Postgres Connection Pool %s@%s:%s/%s Failed,%s",
                          _conf['username'],_conf['host'],_conf['port'],_conf['dbname'],error)
            return None
        pass

    def close(self):
        logging.info("Begin Close Database Connection Pool")
        if self.connection_pool:
            try:
                self.connection_pool.closeall()
                logging.info("Close Database Connection Pool Successfully")
            except (Exception, psycopg2.Error) as error :
                logging.error("Close Database Failed:%s",error)

    def query(self,sql,hasResult=True):
        logging.info("EXEC COMMAND on Postgres: %s",sql)
        conn=None
        try:
            conn=self.connection_pool.getconn()
            if conn:
                cursor=conn.cursor()
                cursor.execute(sql)
                if hasResult:
                    _result=cursor.fetchall()
                    result=[]
                    for _r in _result:
                        result.append(_r)
                    cursor.close()
                    self.connection_pool.putconn(conn)
                    return result
                else:
                    conn.commit()
                    return True
            else:
                return None
        except (Exception, psycopg2.Error) as error :
            if not hasResult:
                if conn:
                    conn.rollback()
            logging.error("Query Failed: %s , error:%s",sql,error)
            return None

    def exec(self,sql):
        return self.query(sql,False)