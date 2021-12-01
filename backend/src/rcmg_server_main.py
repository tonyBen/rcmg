# -*- coding: utf-8 -*-
"""
------------------------------------------------
rcmg.rcmg_server_main
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
from common.initilize_service import *
from common.web_service import *

if __name__ == '__main__':
    initilize_service(SERVER_CONFIG_FILENAME)
    ws=WebService()

