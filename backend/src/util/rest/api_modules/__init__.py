# -*- coding: utf-8 -*-
"""
------------------------------------------------
    util.rest.modules.__init__
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
from .org_user import *
blueprint = Blueprint('modules',__name__)

