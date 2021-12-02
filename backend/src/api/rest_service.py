# -*- coding: utf-8 -*-
"""
------------------------------------------------
rcmg.util.rest.rest_service
------------------------------------------------
Author: Tony Ben (email: nanjinghhu@vip.qq.com)
Create: 2020-07-03
------------------------------------------------
ChangeLog
------------------------------------------------
Date        |Ticket     |Describe   
------------------------------------------------

------------------------------------------------
"""
import threading
import logging
from flask import Flask, request, jsonify,render_template,Blueprint
from common.global_constants import HtmlCode,EC
from flask_cors import *
from api.authz import *
app = Flask(__name__)
CORS(app,supports_credentials=True)
logger = app.logger
app.register_blueprint(blueprint_authz)


class FlaskRestService(threading.Thread):
    http_port=80
    host='0.0.0.0'
    debug=True

    def __init__(self,_conf):
        threading.Thread.__init__(self)
        self.http_port=_conf['port'] if 'port' in _conf.keys() else self.http_port
        self.host=_conf['host'] if 'host' in _conf.keys() else self.host
        self.debug=bool(_conf['debug']) if 'debug' in _conf.keys() else self.host
        logging.info("-"*80)
        logging.info("Begin Initialize Rest Service %s:%s",self.host,self.http_port)
        logging.info("-"*80)


    def run(self):
        logger.info("start web")
        app.run(
            host=self.host,
            port=int(self.http_port),
            debug=self.debug
        )


class ServerException(Exception):
    status_code = HtmlCode.INTERNAL

    def __init__(self, status_code=None, error_code=EC.UNKNOWN, info=None):
        Exception.__init__(self)
        if status_code is not None:
            self.status_code = status_code
        else:
            self.status_code = self.status_code_from_ec(error_code)

        self.error_code = error_code
        self.info = info

    def status_code_from_ec(self,ec):
        if ec == EC.NOT_IN_NETWORK or ec == EC.CONFLICTS_WITH or ec == EC.ALREADY_EXISTS or ec == EC.OBJ_NOT_FOUND:
            return HtmlCode.CONFLICT

        if ec == EC.UNKNOWN:
            return HtmlCode.INTERNAL

        return HtmlCode.BAD_REQUEST


    def to_dict(self):
        rv = dict()
        rv['error_code'] = self.error_code
        if self.info is not None:
            if isinstance(self.info, str):
                rv['info'] = self.info
            else:
                n = 0
                try:
                    for i in self.info:
                        name = 'info' if n == 0 else 'info_' + str(n)
                        rv[name] = i
                        n += 1
                except:
                    pass

        return rv


@app.route('/', methods=('GET', 'POST'))
def index():
    func_list = {}
    for rule in app.url_map.iter_rules():
        if rule.endpoint != 'static':
            desc=app.view_functions[rule.endpoint].__doc__
            func_list[rule.rule] = "Method: [%s] Desc: [%s]"%(",".join(rule.methods),str(desc.replace('\n','')).strip() if desc else "")
    return jsonify(func_list)

@app.route('/test/<path:subpath>', methods=('GET', 'POST'))
def test(subpath):
    """
    Desc: For Test,
    :param orgId
    :param orgName
    :return List
    """
    #import time
    #time.sleep(10)
    logger.info("headers:%s",request.headers)
    return jsonify({"path":subpath,"remote_ip":request.remote_addr,"real_ip":request.headers.get("X-Real-IP"),"remote_user":request.remote_user,"localTime":request.args.get("time")})