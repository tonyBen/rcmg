# -*- coding: utf-8 -*-
"""
------------------------------------------------
    util.cronjob.web
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
"""Example web view for application factory."""


from flask import Blueprint
from .extensions import scheduler
from .tasks import task2
web_bp = Blueprint("cronjob", __name__)


@web_bp.route("/api/cronjob")
def index():
    """Say hi!.
    :url: /
    :returns: hi!
    """
    return "hi!"


@web_bp.route("/api/cronjob/add")
def add():
    """Add a task.
    :url: /add/
    :returns: job
    """
    job = scheduler.add_job(
        func=task2,
        trigger="interval",
        seconds=10,
        id="test job 2",
        name="test job 2",
        replace_existing=True,
    )
    return "%s added!" % job.name