import time
# 数据库文件的名字
def dbName():
    name =f"Animals{time.strftime('%Y-%m-%d', time.localtime())}.db"
    return name

#dbName()