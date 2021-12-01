# -*- coding: utf-8 -*-
"""
------------------------------------------------
rcmg.common.initilize_service
------------------------------------------------
Author: Tony Ben (email: nanjinghhu@vip.qq.com)
Create: 2020-07-02
------------------------------------------------
ChangeLog
------------------------------------------------
Date    |Ticket |Describe   
------------------------------------------------

------------------------------------------------
"""
import logging,logging.handlers
from common.global_constants import *
from util.file_utils import FileUtils
from util.database_utils import *
logger=logging.getLogger()


def init_logging():
    handler = logging.StreamHandler(sys.stdout)
    logger.setLevel(logging.INFO)
    fmt = '%(asctime)s-[%(filename)s:%(lineno)s]-[%(threadName)s]-[%(levelname)s]- %(message)s'
    formatter = logging.Formatter(fmt)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # set ES logger to ERROR level
    logger2=logging.getLogger("elasticsearch")
    logger2.setLevel(logging.ERROR)
    pass


def initilize_service(config_name=None):
    """
    Initilize Service During Startup
    :param config_name:
    :return:
    """
    init_logging()
    GLOBAL_CONFIG_INFORMATION.set_global_configure(FileUtils.read_resource(config_name))
    _modules=GLOBAL_CONFIG_INFORMATION.get_global_configure("global.modules")
    _wm=WrapModule()
    for _m in _modules:
        method_to_call=getattr(_wm,"init_%s"%_m)
        global_config_dict[_m]=method_to_call(GLOBAL_CONFIG_INFORMATION.get_global_configure(_m))

    pass


class WrapModule(object):
    """
    Wrap Module and Init Service
    """

    def init_database(self,_conf):
        """
        Initilize DataBase of Postgres
        :param _conf:
        :return:
        """
        if "dbtype" in _conf.keys():
            dbtype = _conf['dbtype']
            if dbtype == "postgres":
                from util.database.postgres_util import PostgresDatabaseUtils
                return PostgresDatabaseUtils(_conf)
            else:
                return DatabaseUtils(_conf)
        else:
            return DatabaseUtils(_conf)

    def init_redis(self,_conf):
        from util.database.redis_sentinel_utils import RedisSentinelUtils
        return RedisSentinelUtils(_conf)

    def init_es(self,_conf):
        from util.database.es_util import ESUtils
        return ESUtils(_conf)

    def init_email(self,_conf):
        from util.notify.email_utils import EmailUtils
        return EmailUtils(_conf)

    def init_rest(self,_conf):
        from api.rest_service import FlaskRestService
        fs = FlaskRestService(_conf)
        fs.start()
        return fs
