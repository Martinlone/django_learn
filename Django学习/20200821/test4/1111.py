# -*- coding: utf-8 -*-
# Time : 2020/9/22 20:18
# Author : yangzishuang
# Comments :
# dic1 = {"a":1,"b":2,"c":3}
# dic2 = {val:id for id,val in dic1.items()}
# print(dic2)

# dic1 = {"a": 11, "b": 22, "c": 33}
# dic2 = {"a": 1, "b": 2}
# if dic2:
#     dic1.update(dic2)
# print(dic1)

import yaml
data = ['Hello','YAML','World!']
status = 200
_headers = {'Content-Type':'application/x-yaml'}
print(yaml.safe_dump(data),status,_headers)
