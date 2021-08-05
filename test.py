import sys, os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from logging import log
from os import O_TRUNC
import time
import random
import threading

from uvicorn.main import print_version
from LogServer.main import LogStorageMain, LogStorageNode, NodeStatus

def printList(xx):
    for x in xx:
        print(x)

NodeServer = LogStorageNode(nodeName='node1', port='8020')
NodeServer2 = LogStorageNode(nodeName='fuck test', port='1234')

logServer = LogStorageMain(mainServerName='mainServer', storageName='test')
logServer.traceIDBlockSize = 202

NodeServer2.setMainServerConfig(logServer.getConfig())
NodeServer.setMainServerConfig(logServer.getConfig())

logServer.addNode(NodeServer.getConfig())
logServer.addNode(NodeServer2.getConfig())

block = logServer.getTraceIdBlock(nodeName=NodeServer.nodeName)
NodeServer.setTraceIdBlock(block)

block1 = logServer.getTraceIdBlock(nodeName=NodeServer2.nodeName)
block11 = logServer.getTraceIdBlock(nodeName=NodeServer2.nodeName)
block2 = logServer.getTraceIdBlock(nodeName=NodeServer.nodeName)

NodeServer.setTraceIdBlock(block2)
NodeServer2.setTraceIdBlock(block1)
NodeServer2.setTraceIdBlock(block11)

for x in range(400):
    y = random.randrange(1, 20, 1)
    logServer.setLog(
        NodeServer.log('随便说了点什么' + '[' + str(y) + ']', ['err', 'warn',
                                                        'info'][x % 3]))
    logServer.setLog(
        NodeServer2.log('随便说了1231点什么' + '[' + str(y) + ']',
                        ['err', 'warn', 'info'][x % 3]))

print(logServer.traceIDBlockMap)


