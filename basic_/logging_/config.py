#!/usr/bin/env python3
#

from logging import getLogger
from logging.config import fileConfig, dictConfig


def confLog(logger_name):
    conf = './logging.conf'
    fileConfig(conf)
    logger = getLogger(logger_name)
    return logger


def demo():
    logger1 = confLog('console')
    logger2 = confLog('terminate_transback')
