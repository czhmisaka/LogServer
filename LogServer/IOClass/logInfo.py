from typing import Optional
from pydantic import BaseModel
from LogServer.main import typeOfLog


# saveLog 行为接收类
class saveLogReq(BaseModel):
    nodeInfo: Optional[object] = None
    traceId: Optional[str] = 'not traceId back'
    logType: Optional[str] = typeOfLog[0]
    logData: Optional[str] = None


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
    nodePort: int
    mainServerName: Optional[str] = None
    mainServerIP: Optional[str] = None
    mainServerPort: int
    tick:int

# 节点traceIdBlock模板
class traceIdBlock(BaseModel):
    pass  
