import fastapi
from fastapi.applications import FastAPI
import uvicorn
from Log import LS_main


if __name__=='__main__':
    uvicorn.run(app='mainServer:app', host="0.0.0.0",port=8000,reload=True,debug=True)


'''
主机服务
'''

app = FastAPI()

