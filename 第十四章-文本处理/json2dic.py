# -*- coding:utf-8 -*-

import json

# 字典转JSON
dic = {"1":"a","2":"b","3":"c"}

jsonDic = json.dumps(dic, indent=4)

print(jsonDic)

# JSON转字典
tempDic = json.loads(jsonDic)
print(tempDic)
