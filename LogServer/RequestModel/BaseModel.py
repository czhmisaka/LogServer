'''
Date: 2022-02-13 16:12:11
LastEditors: Please set LastEditors
LastEditTime: 2022-02-23 22:29:25
FilePath: \LogServer\LogServer\RequestModel\BaseModel.py
'''
from asyncio.constants import SENDFILE_FALLBACK_READBUFFER_SIZE
from enum import Enum
from pydantic import BaseModel
from typing import Optional


class RequestType(Enum):
    SUCCESS = "Success"
    FAILED = "Fail"
    ERROR= "Error"
    WARNING = "Warning"
    

class BaseRequest(BaseModel):
    data: Optional[dict] = {}
    status: Optional[RequestType]
    



class Request(BaseModel):
    def success(self,data):
        return BaseRequest(data = data,status = RequestType.SUCCESS)

    def fail(self,data):
        return BaseRequest(data = data,status = RequestType.FAILED)

    def error(self,data):
        return BaseRequest(data = data,status = RequestType.ERROR)


    def warn(self,data):
        return BaseRequest(data = data,status = RequestType.WARNING)
