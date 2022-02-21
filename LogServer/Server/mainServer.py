'''
Author: czh
Date: 2021-08-02 10:14:54
'''

import sys
sys.path.append("..")
sys.path.append("../..")
sys.path.append("../../..")
from SQLServerController import sqlTable
from LogServer.RequestModel.IOClass import BlockInfo
from LogServer.RequestModel.IOClass.logInfo import nodeInfo
from LogServer.RequestModel.IOClass.logInfo import traceIdBlock
from LogServer.RequestModel.IOClass.logInfo import saveLogReq as SaveLogReq
from LogServer.main import LogStorageMain
from fastapi.applications import FastAPI
from LogServer.Util import sqlTableCellMaker
import uvicorn


if __name__ == '__main__':
    uvicorn.run(app='mainServer:app',
                host="0.0.0.0",
                port=3000,
                reload=True,
                debug=True)
'''
主机服务
'''

app = FastAPI()
mainLogServer = LogStorageMain(mainServerName='mainServer',
                               storageName='LogServer')

'''初始化必要数据库'''
sql = sqlTable()
sql.createTable("Node",{
    "name":sqlTableCellMaker('maxString'),
    "ip":sqlTableCellMaker("string"),
    ""
})



@app.post('/saveLog/')
async def saveLog(saveLogReq: SaveLogReq):
    mainLogServer.saveLog(nodeName=saveLogReq.nodeInfo)
    pass


@app.post('/getTraceIdBlock')
async def getTraceIdBlock(blockInfo: BlockInfo):
    pass


@app.post('/searchNodeList')
async def searchNodeList():
    pass


# @app.get('/createTable')
# async def createTable():
#     sql = sqlTable()
#     sql.createTable(tableName='newTable', typeMap={
#                     'name': {'type': 'varchar(20)'}})
#     return 'success'


@app.get('/')
async def getIndex():
    return {}


class mainServer:
    def __init__(args):
        pass
