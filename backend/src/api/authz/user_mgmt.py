# -*- coding: utf-8 -*-
"""
------------------------------------------------
    api.authz.user_mgmt
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
from flask import request,jsonify
import logging

logger=logging.getLogger(__name__)

@blueprint_authz.route("/api/authz/user/list")
def list_user():
    return "test"

@blueprint_authz.route("/api/authz/user/login", methods=["POST","OPTIONS"])
def login():
    args=request.args
    username=args['username']
    password=args['password']
    logger.info("Verify UserLogin: %s",username)

    return jsonify({"code":200,"data":{"token":"asdfasdfasdfasdf12312313"}})

