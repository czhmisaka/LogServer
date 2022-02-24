


# 解析类 并创建参数map 用于搭配生成sql表格
def getPropertyList(targetClass):
    targetMap = {}
    for k, v in vars(targetClass()).items():
        print(typeof(v),k)
        if typeof(v) is not None:
            targetMap[k] = sqlTableCellMaker(typeof(v))
    return targetMap


# sql表格单元生成
def sqlTableCellMaker(typeStr, mark=""):
    typeList = {
        "str": "VARCHAR(100)",
        "string": "VARCHAR(100)",
        "maxString": "TEXT",
        "text": "LONGTEXT",
        "int": "INT",
        "bigInt": "BIGINT",
        "float":"FLOAT",
        "blob": "LONGBLOB",
        "ip": "TINYTEXT",
        "time": "DATETIME",
        "id": "INT",
        "dict":"LONGTEXT",
        "list":"LONGTEXT"
    }
    markList = {
        "id": "AUTO_INCREMENT"
    }
    cell = {
        "type": typeStr,
        "mark": mark
    }
    if typeStr in typeList:
        cell['type'] = typeList[typeStr]
    if mark in markList:
        cell['mark'] = markList[mark]
    return cell

# 判断变量类型的函数
def typeof(variate):
    back = None
    if isinstance(variate, int):
        back = "int"
    elif isinstance(variate, str):
        back = "str"
    elif isinstance(variate, float):
        back = "float"
    elif isinstance(variate, list):
        back = "list"
    elif isinstance(variate, dict):
        back = "dict"
    return back