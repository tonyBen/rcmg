# -*- coding: utf-8 -*-
"""
------------------------------------------------
    util.cronjob.extensions
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
"""Initialize any app extensions."""

from flask_apscheduler import APScheduler
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = APScheduler(scheduler=BackgroundScheduler(timezone="UTC"))

# ... any other stuff.. db, caching, sessions, etc.
