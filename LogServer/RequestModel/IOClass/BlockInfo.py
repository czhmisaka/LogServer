'''
Author: czh
Date: 2021-08-31 17:32:19
'''

from typing import List, Optional
from pydantic.main import BaseModel
from .logInfo import traceIdBlock
from .logInfo import nodeInfo

class BlockInfo(traceIdBlock):
    nodeInfo:nodeInfo
    blockMap:Optional[List]
    pass