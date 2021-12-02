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

@app.route('/api/transaction/list',methods=['GET','OPTIONS'])
def dd():
    return jsonify({
        "code": 200,
        "data": {
            "total": 20,
            "items": [
                {
                    "order_no": "64A5DF76-B2Ec-fEf8-Ef64-Fb7c17BE5B2C",
                    "timestamp": 1595746956886,
                    "username": "Eric Lewis",
                    "price": 9393.4,
                    "status": "success"
                },
                {
                    "order_no": "f7B51AD9-DECF-cD98-251b-eF2C2e3Ce58F",
                    "timestamp": 1595746956886,
                    "username": "Deborah Williams",
                    "price": 8907,
                    "status": "pending"
                },
                {
                    "order_no": "24A98E0c-81DD-8A1B-DbCd-cE7bCbb62348",
                    "timestamp": 1595746956886,
                    "username": "Shirley Taylor",
                    "price": 9292,
                    "status": "pending"
                },
                {
                    "order_no": "66Ef46cc-FEac-3D0D-CEe3-c6eC5Fb23f3E",
                    "timestamp": 1595746956886,
                    "username": "John Thompson",
                    "price": 7992.2,
                    "status": "pending"
                },
                {
                    "order_no": "b18df338-BfAB-725C-DeF5-6f6E32224C7a",
                    "timestamp": 1595746956886,
                    "username": "Mary Young",
                    "price": 4895.52,
                    "status": "success"
                },
                {
                    "order_no": "098D0AD9-aEB7-2dE8-CDBF-26dd4B59F1B7",
                    "timestamp": 1595746956886,
                    "username": "Christopher Martinez",
                    "price": 14897.2,
                    "status": "pending"
                },
                {
                    "order_no": "F3b03773-eed9-DEDF-b34b-315FEdA32E3F",
                    "timestamp": 1595746956886,
                    "username": "Laura Thompson",
                    "price": 3697.76,
                    "status": "success"
                },
                {
                    "order_no": "e1cD3A2E-DC3E-E34a-ea73-E3c8598DAcB2",
                    "timestamp": 1595746956886,
                    "username": "Paul Lewis",
                    "price": 7438.2,
                    "status": "pending"
                },
                {
                    "order_no": "FFc72e51-21d0-B1D4-6E8f-6Af6F4FA33aF",
                    "timestamp": 1595746956886,
                    "username": "George Clark",
                    "price": 5466.3,
                    "status": "success"
                },
                {
                    "order_no": "65B1A7e2-123C-c490-1D24-3d982ff66511",
                    "timestamp": 1595746956886,
                    "username": "Jason Lee",
                    "price": 2982.1,
                    "status": "pending"
                },
                {
                    "order_no": "2e435dBB-FCbD-7e6e-B3D1-5BDA8BfE1B83",
                    "timestamp": 1595746956886,
                    "username": "Helen Lopez",
                    "price": 3183.6,
                    "status": "pending"
                },
                {
                    "order_no": "2A2b8a9d-8e6c-D3eD-4FfA-Df8FdC06dDB7",
                    "timestamp": 1595746956886,
                    "username": "Barbara Johnson",
                    "price": 5002.4,
                    "status": "success"
                },
                {
                    "order_no": "2398b9E2-C4DB-7DB4-E0ef-0E67cDD59eeE",
                    "timestamp": 1595746956886,
                    "username": "Deborah Davis",
                    "price": 4742.3,
                    "status": "pending"
                },
                {
                    "order_no": "dc1df713-cf4A-A34f-Bf9F-FABcfea679dd",
                    "timestamp": 1595746956886,
                    "username": "Betty Lee",
                    "price": 5001.61,
                    "status": "pending"
                },
                {
                    "order_no": "FF805e6E-22a4-d05b-e012-4cb8bDAC32dc",
                    "timestamp": 1595746956886,
                    "username": "Eric Brown",
                    "price": 12835.6,
                    "status": "pending"
                },
                {
                    "order_no": "FAaf46D6-3F33-D9Fd-02dd-2deB78cF42a2",
                    "timestamp": 1595746956886,
                    "username": "Deborah Jackson",
                    "price": 11553.2,
                    "status": "success"
                },
                {
                    "order_no": "b1a4aCee-c6c6-63FA-06da-949f9F63CfC9",
                    "timestamp": 1595746956886,
                    "username": "Susan Jackson",
                    "price": 10736.4,
                    "status": "pending"
                },
                {
                    "order_no": "937D78F2-c438-aA66-bad7-F9F9Bd5E2EBf",
                    "timestamp": 1595746956886,
                    "username": "Steven Anderson",
                    "price": 5886,
                    "status": "pending"
                },
                {
                    "order_no": "f54C63b7-c7C2-Cb37-B0BD-d8CAA7268CAE",
                    "timestamp": 1595746956886,
                    "username": "Michael Moore",
                    "price": 12633.8,
                    "status": "pending"
                },
                {
                    "order_no": "Cc59cBde-6714-9D9D-Dfee-59bE19a682BB",
                    "timestamp": 1595746956886,
                    "username": "Donald Lopez",
                    "price": 10428.4,
                    "status": "success"
                }
            ]
        }
    })