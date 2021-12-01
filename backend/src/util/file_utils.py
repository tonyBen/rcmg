# -*- coding: utf-8 -*-
"""
------------------------------------------------
rcmg.util.file_utils
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
import logging
import yaml
class FileUtils(object):
    @staticmethod
    def read_resource(fileName):
        if not os.path.exists(fileName):
            raise FileNotFoundError("file: %s not exist!"%fileName)
        ext=os.path.splitext(fileName)[1]
        if ext==".yaml":
            return YamlFileUtils.read_resource(fileName)
        return {}


class YamlFileUtils(FileUtils):
    @staticmethod
    def read_resource(fileName):
        with open(fileName) as f:
            return yaml.load(f,Loader=yaml.FullLoader)
#            return yaml.load(f)

