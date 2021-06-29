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
        self.log = self.logObj.getLogger(self.logClass)
        self.Filehandler = self.logObj.FileHandler(filename=logPath + '/index.log', encoding="UTF-8")
        self.Filehandler.setFormatter(self.logFormat)
        self.log.addHandler(self.Filehandler)
        self.log.setLevel(self.logObj.INFO)

    # 配置文件地址
    def baseConfig(self, logPath=""):
        self.logObj.basicConfig(filemode='a',
                                filename=logPath + '/index.log',
                                level=self.logObj.INFO)

    # 各种打印
    def info(self, word):
        self.log.info(word)

    def err(self, word):
        self.log.error(word)

    def warn(self, word):
        self.log.warn(word)

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
