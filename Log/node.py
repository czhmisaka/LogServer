import logging as log
import sqlite3 as sq
import time
from enum import Enum, unique
import os
import path
from Log import *

'''
czh家庭服务器的日志模块
分布式节点从机
'''

class NodeLogServer:
    def __init__(self, StorageName="LogStorage"):
        ''' 初始参数
            sqlStorageName      : 数据库保存名称 
            txtStorageName      : txt格式日志保存文件路径
            status              : 日志模块服务状态
            tickRange           : txt日志文件分时保存
        初始参数'''
        LogStorageNode.__init__(self)
        self.sqlStorageName = StorageName
        self.txtStorageName = StorageName
        self.status = 'init'
        self.tickRange = 10 * 60
        pass

    # 正常日志
    def log(self):
        pass

    # 错误日志
    def err(self):
        pass

    # 警告日志
    def warn(self):
        pass
    
    # 启动日志模块守护线程
    def __helpProcess(self):
        pass

    # 启动日志查看服务器
    def __serverProcess():
        pass
