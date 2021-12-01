# -*- coding: utf-8 -*-
"""
------------------------------------------------
rcmg.common.global_constants
------------------------------------------------
Author: Tony Ben (email: nanjinghhu@vip.qq.com)
Create: 2020-07-02
------------------------------------------------
ChangeLog
------------------------------------------------
Date        |Ticket     |Describe   
------------------------------------------------

------------------------------------------------
"""
import os,sys
import yaml
PROJECT_URL=os.path.abspath(os.path.join(os.getcwd()))
SERVER_CONFIG_FILENAME=os.path.join(PROJECT_URL,"config","config_server.yaml")
CLENT_CONFIG_FILENAME=os.path.join(PROJECT_URL,"config","config_client.yaml")

DEFAULT_DATABASE_CONNECTION_POOL_MIN=1
DEFAULT_DATABASE_CONNECTION_POOL_MAX=20

DEFAULT_REDIS_SENTINEL_PORT=26379
DEFAULT_REDIS_PORT=6379
DEFAULT_REDIS_CONNECTION_POOL=20

EMAIL_ATTACH_COMMON_FILE='file'
EMAIL_ATTACH_IMAGE_FILE='image'


global config_infomation,global_config_dict
config_infomation={}
global_config_dict={}


class GLOBAL_CONFIG_INFORMATION(object):
    @staticmethod
    def set_global_configure(config_dict):
        config_infomation.update(config_dict)

    @staticmethod
    def get_global_configure(key=None):
        if key:
            _dic=config_infomation.copy()
            for k in key.split("."):
                if k in _dic.keys():
                    _dic=_dic[k]
            return _dic
        return config_infomation


class HtmlCode(object):
    OK = 200
    OK_NO_CONTENT = 204
    MULTI_STATUS = 207
    CONFLICT = 409
    UNPROCESSABLE_ENTITY = 422
    NOT_ALLOWED = 405
    BAD_REQUEST = 400
    INTERNAL = 500


class EC(object):
    UNKNOWN = "unknown"
    INVALID_SUBNET = "invalid_subnet"
    INVALID_IP = "invalid_ip"
    NOT_IN_NETWORK = "not_in_network"
    CONFLICTS_WITH = "conflicts_with"
    ALREADY_EXISTS = "object_already_exists"
    OBJ_NOT_FOUND = "object_not_found"
    OBJ_NOT_MODIFIED = "object_not_modified"
    OBJ_NOT_UNIQUE = "object_not_unique"
    OBJ_MISSING_NAME = "object_missing_name"
    CANNOT_PROVIDE_ID = "cannot_provide_id"
    ID_MISMATCH = "id_mismatch"
    DATA_MISSING = "data_missing"
    CANNOT_MODIFY = "cannot_modify"
    INVALID_REQUEST = "invalid_request"
    INVALID_VALUE = "invalid_value"
    REQUIRED_PARAMETER = "required_parameter"
    EXCLUDED_SUBNET_NOT_CONTAINED = "excluded_subnet_not_contained"
    SUBNET_DEPENDENT_ON_STATIC = "subnet_dependent_on_static"
    SUBNET_DEPENDENT_ON_EXCLUDED = "subnet_dependent_on_excluded"
    OPERATION_NOT_SUPPORTED = "operation_not_supported"






