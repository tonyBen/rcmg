# -*- coding: utf-8 -*-
"""
------------------------------------------------
rcmg.util.database.es
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
from elasticsearch import Elasticsearch
from elasticsearch import ElasticsearchException

class ESUtils(object):
    """
    ElasticSearch Utils Class
    """
    es=None
    def __init__(self,_conf):
        logging.info("-"*80)
        logging.info("Begin Initialize ElasticSearch Service %s",_conf['host'])
        logging.info("-"*80)
        try:
            self.es = Elasticsearch(_conf['host'],
                               sniff_on_start=True,
                               sniff_on_connection_fail=True,
                               sniffer_timeout=600,
                               maxsize=30,
                               timeout=60,
                               max_retries=3,
                               retry_on_timeout=True,
                               retry_on_status=(502, 503, 504, 429,)
                               )
        except Exception as err:
            logging.error("Initialize ElasticSearch Service %s Failed, Error: %s",_conf['host'],err)
            raise ElasticsearchException(err)

