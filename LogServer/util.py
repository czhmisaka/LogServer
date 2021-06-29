from Log.print import logPrint
import sqlite3 as sql
import os
from Log import logPrint as lp
import logging
import time
'''
日志服务 基础操作工具
1. 同步写入txt+sql
2. 分类提示
3. 提供错误枚举类型
4. 默认带入traceId，提供当前使用者标记
'''


class Util():
    def __init__(self,
                 storageName='',
                 path='',
                 mainServerName='',
                 nodeServerName=''):
        '''初始参数

        mainServerName      : 主机名称
        nodeServerName      : 节点名称
        sqlStorageName      : 数据库保存名称 
        txtStorageName      : txt格式日志保存标识名
        txtPath             : txt格式日志保存路径

        初始参数'''
        self.mainServerName = mainServerName
        self.nodeServerName = nodeServerName
        self.sqlLogStorage = storageName
        self.txtLogStorage = storageName
        self.txtPath = './'+path + '/Log/' + str(mainServerName)+'-'+str(nodeServerName)
        self.mkdirFile(self.txtPath)
        self.lp = logPrint(logPath=self.txtPath, mainName=self.mainServerName,nodeName=self.nodeServerName)
        pass

    # 添加一条新的记录
    def addNewRecordInTxtStorage(self, data, type='info'):
        try:
            data = str(data)
            if type == 'info':
                self.lp.info(data)
            elif type == 'err':
                self.lp.err(data)
            elif type == 'warn':
                self.lp.warn(data)
            else:
                self.lp.info(data)
        except:
            self.lp.err("AddNewRecode Error")
        return True

    # 通过traceID搜索 该模块下的记录
    def searchByTraceId(self, traceId=''):
        pass

    def mkdirFile(self,path):
        '''
        创建文件/多用于创建文件夹
        '''
        try:
            path = self.__pathDeal(path)
            if not os.path.exists(path):
                os.makedirs(path)
                return True
            else:
                return False
        except:
            self.lp.err("Error:"+str(time.time())+":mkdirFile:"+path) 

    def __pathDeal(self,path):
        '''
        下载路径处理
        '''
        path = path.strip()
        path = path.rstrip()
        return path

    # 判断文件是否存在，不存在则创建，可创建文件夹
    def checkFile(self, path):
        try:
            if os.path.exists(path):
                return True
            else:
                f = open(path, 'w')
                f.close()
                return True
        except IOError:
            self.lp.err('IOError in __checkFile[' + str(path) + ']')

    # 写入文档数据
    def writeTxt(self, path, data):
        try:
            with open(path, 'w') as f:
                f.writelines(str(data) + '\n')
        except IOError:
            self.lp.err('IOError in __writeTxt[' + str(path) + ',' +
                        str(data) + ']')
            return False
        except:
            self.lp.err('OtherError in __writeTxt[' + str(path) + ',' +
                        str(data) + ']')
            return False
        else:
            return True
