'''
Date: 2022-02-10 15:05:07
LastEditors: Please set LastEditors
LastEditTime: 2022-02-23 21:37:54
FilePath: \LogServer\LogServer\Server\SQLServerController\sqlTable.py
'''


from venv import create
import pymysql


class sqlTable:
    def __init__(self,host = "120.77.144.232",user = 'logServer',password='DfhMztCE5NkC867T',database = 'logServer'):
        self.DB = pymysql.connect(
            host=host, user=user, password=password, database=database)
        self.cursor = self.DB.cursor()
        pass

    def _getCursor(self):
        return self.cursor

    def _execute(self, sql):
        self.cursor.execute(sql)
        return self.cursor

    '''
    name: createTable
    description: 创建表格
    authors: CZH
    Date: 2022-02-11 11:06:46
    param {*} self
    param {*} tableName
    param {*} typeMap
    '''
    def createTable(self, tableName, typeMap):
        if not tableName:
            print('表格名称不得为空')
        self.cursor.execute("drop table if exists "+tableName)
        sql = "create table "+tableName+"("
        if 'id' not in typeMap:
            sql +=  'id INT UNSIGNED AUTO_INCREMENT,'
        for x in typeMap:
            sql = sql + " " + x + " " + typeMap[x]['type']
            if 'mark' in typeMap[x]:
                sql = sql + " " + typeMap[x]['mark']
            sql = sql + ','
        sql += 'PRIMARY KEY ( `id` )) ENGINE=InnoDB DEFAULT CHARSET=utf8'
        print(sql)
        return self._execute(sql)
    
    
class SqlCodeMaker:
    def __init__(self,tableName):
        self.tableName = tableName
        
    