'''
Author: czh
Date: 2021-08-02 10:14:54
'''

import sys

from sqlalchemy import VARCHAR
from LogServer.RequestModel.BaseModel import Request
from LogServer.Util.util import getPropertyList, typeof
sys.path.append("..")
sys.path.append("../..")
sys.path.append("../../..")
from SQLServerController import sqlTable
from LogServer.RequestModel.IOClass import BlockInfo
from LogServer.RequestModel.IOClass.logInfo import nodeInfo
from LogServer.RequestModel.IOClass.logInfo import traceIdBlock
from LogServer.RequestModel.IOClass.logInfo import saveLogReq as SaveLogReq
from LogServer.main import LogStorageMain, LogStorageNode
from fastapi.applications import FastAPI
from LogServer.Util import sqlTableCellMaker
import uvicorn

Req = Request()

if __name__ == '__main__':
    uvicorn.run(app='mainServer:app',
                host="0.0.0.0",
                port=3000,
                reload=True,
                debug=True)
    '''初始化必要数据库'''
    sql = sqlTable()
    sql.createTable("Node",getPropertyList(LogStorageMain))
    sql.createTable("TraceIdBlock",getPropertyList(traceIdBlock))

'''
主机服务
'''

app = FastAPI()
mainLogServer = LogStorageMain(mainServerName='mainServer',
                               storageName='LogServer',
                               port='3000')

NodeServer = LogStorageNode(nodeName='node1', port='8080')

@app.post('/saveLog/')
async def saveLog(saveLogReq: SaveLogReq):
    mainLogServer.saveLog(nodeName=saveLogReq.nodeInfo)
    pass


@app.post('/getTraceIdBlock')
async def getTraceIdBlock(blockInfo: BlockInfo):
    NodeServer.setTraceIdBlock(BlockInfo)
    return Req.success('获取区块成功')


@app.post('/searchNodeList')
async def searchNodeList():
    pass

@app.get('/getConfig')
async def getIndex():
    return Req.success(mainLogServer.getConfig())
    
class mainServer:
    def __init__(args):
        pass
