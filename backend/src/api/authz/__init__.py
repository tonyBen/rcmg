# -*- coding: utf-8 -*-
"""
------------------------------------------------
    util.__init__.py
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
from flask import Blueprint
blueprint_authz = Blueprint('authz',__name__)
from .org_mgmt import *
from .user_mgmt import *
#from api.authz import org_mgmt
#from . import org_mgmt

