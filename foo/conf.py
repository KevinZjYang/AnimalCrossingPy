import time
# 数据库文件的名字
def dbName():
    return f"""Animals{time.strftime("%Y/%m/%d", time.localtime()) }.db"""

#dbName()