# -*- coding: utf-8 -*-
"""
------------------------------------------------
rcmg.util.notify.email_utils
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

import smtplib
import logging
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from urllib.parse import urlparse
from email.mime.base import MIMEBase
from email import encoders
import ntpath
import mimetypes
import base64
from common.global_constants import *

class EmailUtils(object):
    emailService=None
    send_from=None

    def __init__(self,_conf):
        logging.info("-"*80)
        logging.info("Begin Initialize Email Service %s/%s:%s",_conf['username'],_conf['smtp_host'],_conf['smtp_port'])
        logging.info("-"*80)
        self.send_from=_conf['username']
        self.emailService=smtplib.SMTP(_conf['smtp_host'])
        self.emailService.connect(_conf['smtp_host'], int(_conf['smtp_port']))
        self.emailService.ehlo()
        self.emailService.starttls()
        self.emailService.ehlo()
        if "password" in _conf.keys() and _conf['password']:
            self.emailService.login(_conf['username'], urlparse(_conf['password']))

    def sendEmail(self,subject,context,receivers,attachList=None):
        logging.info("Begin SendEmail sub: %s to %s",subject,receivers)
        msg = MIMEMultipart()
        msg['From'] = self.send_from
        msg['Subject'] = subject
        msg.attach(MIMEText(context, 'html'))
        msg['TO']=receivers
        if attachList:
            if isinstance(attachList,list):
                for name in attachList:
                    logging.info("attachment:%s",name)
                    part = MIMEBase('application', "octet-stream")
                    part.set_payload(open(name, "rb").read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', 'attachment; filename="%s"'%(ntpath.basename(name)))
                    msg.attach(part)
            elif isinstance(attachList,str):
                logging.info("attachment:%s",attachList)
                part = MIMEBase('application', "octet-stream")
                part.set_payload(open(attachList, "rb").read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', 'attachment; filename="%s"'%(ntpath.basename(attachList)))
                msg.attach(part)
        self.emailService.sendmail(self.send_from,receivers.split(","),msg.as_string())

    # def sendEmail(self,subject,context,receivers,attachList=None,attach_type=EMAIL_ATTACH_COMMON_FILE):
    #     logging.info("Begin SendEmail sub: %s to %s",subject,receivers)
    #     msg = MIMEMultipart()
    #     msg['From'] = self.send_from
    #     msg['Subject'] = subject
    #     msg.attach(MIMEText(context, 'html'))
    #     msg['TO']=receivers
    #     if attachList:
    #         for f in attachList:
    #             if not os.path.isfile(f):
    #                 continue
    #             ctype, encoding = mimetypes.guess_type(f)
    #             if ctype is None or encoding is not None:
    #                 ctype = 'application/octet-stream'
    #             maintype, subtype = ctype.split('/', 1)
    #             with open(f, 'rb') as fp:
    #                 msg.attach(fp.read(),
    #                                    maintype=maintype,
    #                                    subtype=subtype,
    #                                    filename=f)
    #
    #     self.emailService.sendmail(self.send_from,receivers.split(","),msg.as_string())




