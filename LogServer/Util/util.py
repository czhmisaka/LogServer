



# sql表格单元生成
def sqlTableCellMaker(type,mark=""):
    typeList = {
        "string":"VARCHAR(100)",
        "maxString":"TEXT",
        "text":"LONGTEXT",
        "int":"INT",
        "bigInt":"BIGINT",
        "blob":"LONGBLOB",
        "ip":"TINYTEXT",
        "time":"DATETIME",
        
    }
    if type in typeList:
        return {
            "type":typeList[type],
            "mark":mark
        }
    else:
        return {
            "type":type,
            "mark":mark
        }