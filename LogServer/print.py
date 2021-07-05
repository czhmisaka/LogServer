import logging
import time
from uvicorn.main import main
import os


class logPrint:
    def __init__(self, logPath="", mainName="", nodeName=""):
        if mainName == "":
            return False
        self.mainName = mainName
        self.nodeName = nodeName
        self.logPath = logPath
        self.logClass = mainName + '.' + nodeName
        self.logObj = logging
        self.logFormat = self.logObj.Formatter(
            fmt='%(levelname)s-%(name)s【%(asctime)s】:%(message)s',
            datefmt='%Y-%m-%d %H:%M:%S')
        self.Filehandler = ''
        self.log = False
        if self.log is False:
            self.log = self.__newFileHandler()

    # 各种打印
    def info(self, word):
        print(word,self.logClass)
        self.log.info(word)

    def err(self, word):
        self.log.error(word)

    def warn(self, word):
        self.log.warn(word)

    # 创建新的写入机
    def __newFileHandler(self, logPath=False):
        if logPath == False:
            logPath = self.logPath
        else:
            self.logPath = logPath
        if self.Filehandler == '':
            self.Filehandler = self.logObj.FileHandler(filename=logPath +
                                                   '/index.log',
                                                   encoding="UTF-8")
        self.Filehandler.setFormatter(self.logFormat)
        log = self.logObj.getLogger(self.logClass)
        log.addHandler(self.Filehandler)
        log.setLevel(self.logObj.INFO)
        return log

    # 设置新的分块文件记录
    def checkBlock(self):
        logPath = self.logPath
        self.Filehandler = self.__newFileHandler(logPath=logPath)
        return 0

    # 检查文件夹
    def __checkFile(self, path):
        try:
            if os.path.exists(path):
                return True
            else:
                f = open(path, 'w')
                f.close()
                return True
        except IOError:
            self.log.info('IOError in __checkFile[' + str(path) + ']')
            return False
