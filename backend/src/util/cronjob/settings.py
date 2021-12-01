# -*- coding: utf-8 -*-
"""
------------------------------------------------
    util.cronjob.settings.py
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
"""App configuration."""


class Config:
    """Prod config."""

    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    """Dev config."""

    DEBUG = True