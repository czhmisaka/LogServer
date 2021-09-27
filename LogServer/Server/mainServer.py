'''
Author: czh
Date: 2021-08-02 10:14:54
'''
from fastapi.applications import FastAPI
import uvicorn
from LogServer.main import LogStorageMain
from LogServer.IOClass.logInfo import saveLogReq as SaveLogReq
from LogServer.IOClass.logInfo import traceIdBlock
from LogServer.IOClass.logInfo import nodeInfo
from LogServer.IOClass import BlockInfo


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
async def saveLog(saveLogReq:SaveLogReq):
    mainLogServer.saveLog(nodeName=saveLogReq.nodeInfo)
    pass


@app.post('/getTraceIdBlock')
async def getTraceIdBlock(blockInfo:BlockInfo):
    pass

@app.post('/searchNodeList')
async def searchNodeList():
    pass

class mainServer:
    def __init__(args):
        pass
        