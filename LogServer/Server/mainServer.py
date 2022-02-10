'''
Author: czh
Date: 2021-08-02 10:14:54
'''
from SQLServerController import sqlTable
from LogServer.IOClass import BlockInfo
from LogServer.IOClass.logInfo import nodeInfo
from LogServer.IOClass.logInfo import traceIdBlock
from LogServer.IOClass.logInfo import saveLogReq as SaveLogReq
from LogServer.main import LogStorageMain
from hashlib import new
from fastapi.applications import FastAPI
from sqlalchemy import VARCHAR
import uvicorn
import sys
sys.path.append("..")


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


@app.get('/createTable')
async def createTable():
    sql = sqlTable()
    fuck = sql.createTable(tableName='newTable', typeMap={
                    'name': {'type': 'varchar(20)'}})
    return fuck


@app.get('/')
async def getIndex():
    return {}


class mainServer:
    def __init__(args):
        pass
