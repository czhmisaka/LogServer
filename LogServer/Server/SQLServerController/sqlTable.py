'''
Date: 2022-02-10 15:05:07
LastEditors: Please set LastEditors
LastEditTime: 2022-02-10 23:04:27
FilePath: \LogServer\LogServer\Server\SQLServerController\sqlTable.py
'''


from venv import create
import pymysql


class sqlTable:
    def __init__(self):
        self.DB = pymysql.connect(
            host='120.77.144.232', user='logServer', password='DfhMztCE5NkC867T', database='logServer')
        self.cursor = self.DB.cursor()
        pass

    def _getCursor(self):
        return self.cursor

    def _execute(self, sql):
        self.cursor.execute(sql)

    def createTable(self, tableName, typeMap):
        # try:
        if not tableName:
            print('表格名称不得为空')
        self.cursor.execute("drop table if exists "+tableName)
        sql = "create table "+tableName+"("
        for x in typeMap:
            sql = sql + " " + x + " " + typeMap[x]['type']
            if 'mark' in typeMap[x]:
                sql = sql + " " + typeMap[x]['mark']
            sql = sql
        sql += ') ENGINE=InnoDB DEFAULT CHARSET=utf8'
        self._execute(sql)
        # except Exception:
        #     print('createTable 失败')
