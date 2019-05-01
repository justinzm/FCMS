#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/21 0021
# @Author  : justin.郑 3907721@qq.com
# @File    : logger.py
# @Desc    : 日志文件

import logging.handlers
import platform
import sys


class CmsLogger:
    def __init__(self, name):
        # 业务日志的配置
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)

        if platform.system() == "Windows":
            num = 1
        else:
            num = 0

        format = logging.Formatter('[%(asctime)s[%(name)s] %(levelname)s: %(message)s')
        handler = logging.handlers.TimedRotatingFileHandler(sys.path[num] + '/logs/' + name + '.log', 'D', encoding='utf-8')
        handler.setFormatter(format)

        self.logger.addHandler(handler)

        # 错误日志的配置
        self.errorLogger = logging.getLogger("ERROR")
        self.errorLogger.setLevel(logging.ERROR)
        errorFormatter = logging.Formatter('[%(asctime)s[' + name + '] %(levelname)s: %(message)s')
        errorHandler = logging.handlers.TimedRotatingFileHandler(sys.path[num] + '/logs/error.log', 'D', encoding='utf-8')
        errorHandler.setFormatter(errorFormatter)

        self.errorLogger.addHandler(errorHandler)

        # 调试日志的配置
        self.debugLogger = logging.getLogger("DEBUG")
        self.debugLogger.setLevel(logging.DEBUG)
        debugFormatter = logging.Formatter('[%(asctime)s[' + name + '] %(levelname)s: %(message)s')
        debugHandler = logging.handlers.TimedRotatingFileHandler(sys.path[num] + '/logs/debug.log', 'D', encoding='utf-8')
        debugHandler.setFormatter(debugFormatter)

        self.debugLogger.addHandler(debugHandler)

    def info(self, message, *args):
        self.logger.info(message, *args)
        self.logger.handlers.pop()

    def error(self, message, *args):
        self.errorLogger.error(message, *args, exc_info=True)
        self.logger.handlers.pop()

    def debug(self, message, *args):
        self.debugLogger.debug(message, *args)
        self.logger.handlers.pop()


