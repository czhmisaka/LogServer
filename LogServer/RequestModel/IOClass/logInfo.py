'''
Date: 2022-02-10 10:23:16
LastEditors: CZH
LastEditTime: 2022-02-14 08:41:50
FilePath: /LogServer/LogServer/RequestModel/IOClass/logInfo.py
'''
from json import JSONEncoder
from tokenize import Double
from typing import Optional
from pydantic import BaseModel


# nodeInfo 节点信息模板
class nodeInfo(BaseModel):
    '''
        'nodeId': '节点ID',
        'nodeName': '节点名称',
        'nodeIP': '节点IP',
        'nodePort': '节点端口',
        'mainServerName': '主机名称',
        'mainServerIP': '主机IP',
        'mainServerPort': '主机端口',
        'tick': "访问间隔"
    '''
    nodeId: Optional[str] = None
    nodeName: Optional[str] = None
    nodeIp: Optional[str] = '0.0.0.0'
    nodePort: Optional[int] = 0
    mainServerName: Optional[str] = None
    mainServerIP: Optional[str] = None
    mainServerPort: Optional[int] = 0
    tick:Optional[int] = 1

# 节点traceIdBlock模板
class traceIdBlock(BaseModel):
    '''
        'blockSize': '区块大小',
        'nodeId': '分配的节点ID',
        'start': '区块起点',
        'mainServer': '主机名称',
        'mainServerPort': '主服务器端口'
    '''
    blockSize: int = 10000
    nodeId: Optional[str] = '0.0.0.0'
    start: int = 0
    mainServer: Optional[str] = '主机'
    mainServerPort: Optional[str] = '0.0.0.0'
    pass


# saveLog 行为接收类
class saveLogReq(BaseModel):
    nodeInfo: nodeInfo 
    traceId: Optional[str] = 'not traceId back'
    logType: Optional[str]
    logData: Optional[str] = None



