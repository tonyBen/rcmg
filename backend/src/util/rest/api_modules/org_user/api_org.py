# -*- coding: utf-8 -*-
"""
------------------------------------------------
    util.rest.modules.api_org
------------------------------------------------
Author: Tony Ben (email: nanjinghhu@vip.qq.com)
Create: 11/29/2021
------------------------------------------------
ChangeLog
------------------------------------------------
Author        Date      Version     Describe
------------------------------------------------
tben     11/29/2021     v1.0.0      Init
------------------------------------------------
"""
from __init__ import *
@blueprint.route("/api/orgs")
def list_orgs():
    print("-------")