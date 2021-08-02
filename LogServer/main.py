from enum import Enum, unique
from os import name
import socket
from inspect import BlockFinder, isfunction
import psutil
from time import daylight, time

from uvicorn.main import main
from LogServer.util import Util

# 节点信息模板
nodeInfoTemplate = {
    'nodeId': '节点ID',
    'nodeName': '节点名称',
    'nodeIP': '节点IP',
    'nodePort': '节点端口',
    'mainServerName': '主机名称',
    'mainServerIP': '主机IP',
    'mainServerPort': '主机端口',
    'tick': "访问间隔",
    'nodeStatus':''
}

# 节点traceIdBlock模板
traceIdBlockTemplate = {
    'blockSize': '区块大小',
    'nodeId': '分配的节点ID',
    'start': '区块起点',
    'mainServer': '主机名称',
    'mainServerPort': '主服务器端口'
}
# 目前可用的log类型
typeOfLog = ['info', 'err', 'warn']
'''
czh家庭服务器的日志模块
主机
'''


class LogStorageMain:
    def __init__(self,
                 storageName="LogStorage",
                 mainServerName='root',
                 port='8050'):
        ''' 初始参数
            port                : 默认启动端口
            storageName         : 日志保存地址(搭配Util使用)
            status              : 日志模块服务状态
            tickRange           : txt日志文件分时保存
            cmdShow             : 控制台输出
            nodeMap             : 节点 - 
            logMap              : 日志服务 -
            nodeTemplate        : 节点数据模板
            mainServerName      : 主服务器名
            mainLog             : 主服务器 节点名称
            traceIDBlockMap     : traceID区块管理map
            traceIDBlockSign    : traceID区块ID
            traceIDBlockSize    : traceID区块大小
            traceIDBlockTemplate: traceID区块模板
        '''
        self.port = port
        self.storageName = storageName
        self.status = 'init'
        self.tickRange = 24 * 60 * 60
        self.cmdShow = False
        self.nodeMap = {}
        self.logMap = {}
        self.nodeTemplate = nodeInfoTemplate
        self.mainServerName = mainServerName
        self.mainserverIP = self.getIPConifg()['ip']
        self.mainLog = 'mainLogNode'
        self.traceIDBlockMap = {}
        self.traceIDBlockSign = 0
        self.traceIDBlockSize = 10 * 1000
        self.traceIDBlockTemplate = traceIdBlockTemplate
        pass

    # 获取配置
    def getConfig(self):
        data = {
            'mainServerName': self.mainServerName,
            'mainServerIP': self.mainserverIP,
            'mainServerPort': self.port
        }
        return data

    # 添加主节点打印服务
    # 这边需要用户手动操作防止日志重复写入的问题 （留个坑）
    def addMainLogNode(self):
        self.addNode({
            'nodeName': self.mainLog,
            'nodeIP': '127.0.0.1',
            'nodePort': self.port,
            'nodeId': '0',
            'mainServerIP': '127.0.0.1',
            'mainServerPort': self.port,
            'tick': '10'
        })

    # 启动日志模块守护线程
    def __helpProcess(self):
        pass

    # 启动日志查看服务器
    def __serverProcess(self):
        
        pass

    # 启动心跳服务查看节点状态
    def __beatCheckProcess(self,nodeId):
        nodeInfo = self.getNodeInfoByNodeName(nodeId=nodeId)
        return nodeInfo

    # 保存日志
    def setLog(self, logs:object):
        return self.saveLog(nodeName=logs['nodeName'],
                            data=logs['data'],
                            traceId=logs['traceId'],
                            type=logs['type'])

    def saveLog(self, nodeName:bool=False, data=False, type='info', traceId=False):
        if not data:
            return False
        if not nodeName:
            lp = self.getLogClassByNodeName(nodeName=self.mainLog)
        else:
            lp = self.getLogClassByNodeName(nodeName=nodeName)
        # print(nodeName)
        if lp is not False:
            return lp.addNewRecordInTxtStorage(data='【' + str(traceId) + '】' +
                                               str(data),
                                               type=type)
        else:
            return False

    # 通过节点Name或id获取保存在主机的节点信息
    def getNodeInfoByNodeName(self, nodeName=False, nodeId=False):
        if nodeId:
            for x in self.nodeMap:
                if self.nodeMap[x]['nodeId'] == nodeId:
                    return self.nodeMap[x]
        if nodeName:
            for x in self.nodeMap:
                if x == nodeName:
                    return self.nodeMap[x]
        return False

    # 通过节点ID获取对应节点操作类
    def getLogClassByNodeId(self, nodeId):
        if nodeId in self.logMap:
            return self.logMap[nodeId]
        return False

    # 通过节点名称获取对应节点操作类
    def getLogClassByNodeName(self, nodeName):
        if nodeName in self.nodeMap:
            nodeId = self.nodeMap[nodeName]['nodeId']
            return self.getLogClassByNodeId(nodeId)
        else:
            return self.getLogClassByNodeName(self, self.mainLog)

    # 使用节点名称获取节点ID
    def __getNodeIdByName(self, nodeName=''):
        if nodeName != '':
            id = hash(nodeName)
            while True:
                if id in self.logMap:
                    return False
                else:
                    return id
        else:
            return ''

    # 获取traceID_Block(traceId 区块)
    def getTraceIdBlock(self, nodeName):
        nodeInfo = self.getNodeInfoByNodeName(nodeName)
        if nodeInfo is False:
            return False
        traceIdBlock = {}
        traceIdBlock['blockSize'] = str(self.traceIDBlockSize - 1)
        traceIdBlock['nodeId'] = nodeInfo['nodeId']
        traceIdBlock['start'] = str(self.traceIDBlockSign)
        traceIdBlock['mainServer'] = self.mainServerName
        traceIdBlock['mainServerPort'] = self.port
        if nodeInfo['nodeId'] not in self.traceIDBlockMap.keys():
            self.traceIDBlockMap[nodeInfo['nodeId']] = []
        self.traceIDBlockMap[nodeInfo['nodeId']].append({
            'min':
            self.traceIDBlockSign,
            'max':
            self.traceIDBlockSize + self.traceIDBlockSign - 1
        })
        self.traceIDBlockSign = self.traceIDBlockSign + self.traceIDBlockSize
        return traceIdBlock

    # 添加一个节点
    def addNode(self, nodeInfo):
        nodeId = ''
        if 'nodeId' not in nodeInfo:
            nodeId = self.__getNodeIdByName(nodeInfo["nodeName"])
        else:
            nodeId = nodeInfo["nodeId"]
        if nodeId == '':
            return False
        nodeInfo["mainServerName"] = self.mainServerName
        lp = Util(path='test',
                  mainServerName=nodeInfo["mainServerName"],
                  nodeServerName=nodeInfo["nodeName"])
        self.logMap[nodeId] = lp
        try:
            node = {
                'nodeId': nodeId,
                'nodeName': nodeInfo["nodeName"],
                'nodeIP': nodeInfo["nodeIP"],
                'nodePort': nodeInfo["nodePort"],
                'mainServerName': nodeInfo["mainServerName"],
                'mainServerIP': nodeInfo["mainServerIP"],
                'mainServerPort': nodeInfo["mainServerPort"],
                'tick': nodeInfo["tick"],
            }
        except:
            return False
        self.nodeMap[nodeInfo["nodeName"]] = node
        return True

    # 获取ip配置
    def getIPConifg(self):
        IPConfig = {}
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            IPConfig['ip'] = s.getsockname()[0]
        finally:
            s.close()
        return IPConfig

    # 移除一个节点信息
    # 此处仍然会保留nodeId防止日志混写，但需要在Util中注销写入日志的服务
    def removeNode(self, nodeName, nodeId):

        pass


'''
节点
'''


class LogStorageNode:
    def __init__(self,
                 mainServerName='mainServer',
                 mainServerInfo={},
                 nodeName='node',
                 port='8020'):
        ''' 初始参数
            mainServerName      : 主机名
            nodeName            : 当前节点名称
            port                : 启动端口
            IPConfig            : ip信息
            traceIdBlockInfo    : 当前的traceId区块信息
            PreTraceIdBlockList : 预备可用的traceId区块（预先申请）
            traceID             : 当前可用的traceId
            traceIdLimit        : 当前可用的traceId上限
            tick                : 分钟验证频次
        初始参数'''
        self.mainServerName = mainServerName
        self.mainServerInfo = {}
        self.nodeName = nodeName
        self.port = port
        self.IPConfig = self.getIPConifg()
        self.traceIdBlockInfo = {}
        self.PreTraceIdBlockList = []
        self.traceID = 0
        self.traceIdLimit = 0
        self.tick = 1

    # 新建到主机的链接
    def linkToMainServer(self):
        pass

    # 通信验证服务
    def linkCheck(self):
        pass

    def getNodeEnvStatus(self):
        
        pass

    # 设定主机信息
    def setMainServerConfig(
        self,
        mainServerInfo={
            'mainServerName': 'mainServer',
            'mainServerIP': '30.117.24.206',
            'mainServerPort': '8050'
        }):
        self.mainServerName = mainServerInfo['mainServerName']
        self.mainServerInfo = mainServerInfo
        pass

    # 构建一条日志
    def log(self, word='', type="info"):
        data = {
            'nodeName': self.nodeName,
            'data': word,
            'traceId': self.getTraceId(),
            'config': self.getConfig(),
            'type': type
        }
        return data

    # 获取节点配置
    def getConfig(self):
        data = {
            'nodeName': self.nodeName,
            'nodeIP': self.IPConfig['ip'],
            'nodePort': self.port,
            'mainServerName': '',
            'mainServerIP': '',
            'mainServerPort': '',
            'tick': self.tick
        }
        for x in ['mainServerName', 'mainServerPort', 'mainServerIP']:
            if x in self.mainServerInfo:
                data[x] = self.mainServerInfo[x]
        return data

    # 从分配的区块中取出一个id
    def getTraceId(self):
        nextTraceId = int(self.traceID) + 1
        if nextTraceId > self.traceIdLimit or not self.traceIdBlockInfo:
            nextTraceId = self.__replaceTraceIdBlock()
        if nextTraceId == 0:
            return 0
        self.traceID = nextTraceId
        return nextTraceId

    # 获取ip配置
    def getIPConifg(self):
        IPConfig = {}
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            IPConfig['ip'] = s.getsockname()[0]
        finally:
            s.close()
        return IPConfig

    # 获取一个traceIdBlock到列表中
    def setTraceIdBlock(
        self,
        traceIdBlock={
            'blockSize': '区块大小',
            'nodeId': '分配的节点ID',
            'start': '区块起点',
            'mainServer': '主机名称',
            'mainServerPort': '主服务器端口'
        }):
        self.PreTraceIdBlockList.append(traceIdBlock)

    # 替换使用完的traceId区块
    def __replaceTraceIdBlock(self):
        if len(self.PreTraceIdBlockList) == 0:
            return 0
        else:
            self.traceIdBlockInfo = self.PreTraceIdBlockList[0]
            del self.PreTraceIdBlockList[0]
            self.traceIdLimit = int(self.traceIdBlockInfo['blockSize']) + int(
                self.traceIdBlockInfo['start'])
            return self.traceIdBlockInfo['start']


class NodeStatus(Enum):
    ReadyForLink = 0  # 节点上线，等待配置连接中
    Linking = 1  # 链接中
    Missing = 2  # 链接丢失
    ReLink = 3  # 尝试重新链接
    NotFound = 4  # 未找到对应节点or对节点的访问被拒绝
    OnLine = 10  # 节点在线
    OffLine = 20  # 节点离线or已登记的节点日志服务关闭
