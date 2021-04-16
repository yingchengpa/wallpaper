# -*- coding: utf-8 -*-


"""
服务统一的日志文件
"""

import logging
from logging.handlers import TimedRotatingFileHandler
import os
import sys

log_fmt = '%(asctime)s %(filename)s:%(lineno)d[%(levelname)s]:%(message)s'
formatter = logging.Formatter(log_fmt)
logging.basicConfig(level=logging.DEBUG, format=log_fmt)
logger = logging.getLogger()

log_pre = "daily.log"


def getexepath():
    return os.path.split(os.path.realpath(sys.argv[0]))[0]


def logfile_init():
    """循环写入日志初始化"""
    log_path = getexepath()
    log_file_handler = TimedRotatingFileHandler(filename=log_path + "/{}".format(log_pre),
                                                when="D", interval=1, backupCount=7, encoding='utf-8')
    log_file_handler.suffix = "%Y-%m-%d.log"
    log_file_handler.setFormatter(formatter)
    log_file_handler.setLevel(logging.INFO)
    logger.addHandler(log_file_handler)


logfile_init()

# 日志调用方式
# import utils.log as log

# log.logger.debug("hello log")      -- 记录调试记录
# log.logger.info("hello log")       -- 记录非异常下的重要记录
# log.logger.warning("hello log")       -- 记录有异常的记录，但不影响主要逻辑
# log.logger.error("hello log")      -- 记录有异常的记录
# log.logger.fatal("hello log")      -- 禁止使用（后续作为扩展功能)

