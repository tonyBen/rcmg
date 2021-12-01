# -*- coding: utf-8 -*-
"""
------------------------------------------------
    api.authz.org_mgmt
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
from . import blueprint_authz
@blueprint_authz.route("/api/authz/org/list",methods=["GET","POST"])
def list_org():
    return "test"


