import fastapi
from fastapi.applications import FastAPI
import uvicorn
from LogServer.main import LogStorageMain


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




