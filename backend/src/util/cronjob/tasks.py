# -*- coding: utf-8 -*-
"""
------------------------------------------------
    util.cronjob.tasks
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
from .extensions import scheduler

@scheduler.task(
    "interval",
    id="job_sync",
    seconds=10,
    max_instances=1,
    start_date="2000-01-01 12:19:00",
)
def task1():
    """Sample task 1.
    Added when app starts.
    """
    print("running task 1!")  # noqa: T001

    # oh, do you need something from config?
    with scheduler.app.app_context():
        print(scheduler.app.config)  # noqa: T001


def task2():
    """Sample task 2.
    Added when /add url is visited.
    """
    print("running task 2!")  # noqa: T001