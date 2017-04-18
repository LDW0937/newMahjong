# -*- coding:utf-8 -*-
#!/bin/python

"""
Author: $Author$
Date: $Date$
Revision: $Revision$

Description: Describe module function
"""
import logging

logger = None

def _get():
    global logger
    if not logger:
        logger = logging.getLogger("wsgi")
    return logger

def log_info(msg):
    _get().log(logging.INFO, message)

def log_debug(message):
    _get().log(logging.DEBUG, message)