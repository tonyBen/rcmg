# -*- coding: utf-8 -*-
"""
------------------------------------------------
rcmg.util.database_utils
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


class DatabaseUtils(object):
    conf=None

    def __init__(self,_conf):
        self.conf=_conf
        pass

    def close(self):
        pass

    def query(self,sql):
        return None

    def exec(self,sql):
        return None


