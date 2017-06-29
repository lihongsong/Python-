# -*- coding:utf-8 -*-

import re


# python中的正则表达式拓展符号
# 通过使用(?iLmsux)系列选项，可以指定多个标记

# re.I/IGNOPRECASE 忽略大小写的匹配
result = re.findall(r"(?i)th\w+","This that those")
print("re.I/IGNOPRECASE: ",result)

# re.M/MULTILINE 多行混合,能够把每行都当做起始位置^进行匹配
result = re.findall(r"(?m)(^th[\w ]+)","""
this line is the first,
ahthor line,
that line, it"s the best
""")
print("re.M/MULTILINE: ",result)

# re.S/DOTALL 表示.可以用来匹配\n字符
result = re.findall(r"(?s)(th.+)","""
this first line
this second line
this third line
""")
print("re.S/DOTALL: ",result)

# re.X/VERBOSE 使其re能够识别填充空格和换行的正则表达式
result = re.search(r"""(?x)
    \((\d+)\)       # 区号
    [ ]             # 空格
    (\d{3})         # 前缀
    -               # 横线
    (\d{4})         # 终点数字
""","(4444) 123-1234")
print("re.X/VERBOSE: ",result.groups())

# (?P<name>) (?P = name) (\g<name>)
# 使用(?P<name>)组内的正则匹配做标记，通过(\g<name>)来调用这个标记
result = re.sub(r"(?P<lastname>\w+)\.(?P<firstname>\w+)","\g<firstname>.\g<lastname>","hongsong.li")
print("?P<name> \g<name>: ",result)
# 通过(?P=name)来重用之前的正则标记  (ps:等号左右不能有空格)
result = re.search(r"(?P<lastname>\w+)\.(?P<firstname>\w+) (?P=firstname)\.(?P=lastname)","hongsong.li li.hongsong")
print("?P<name> ?P=name: ",result.group())

# 条件正则表达式
print('bool(re.search(r"(?:(x)|y)(?(1)y|x)","yy"))',bool(re.search(r"(?:(x)|y)(?(1)y|x)","yy")))
print('bool(re.search(r"(?:(x)|y)(?(1)y|x)","xy"))',bool(re.search(r"(?:(x)|y)(?(1)y|x)","xy")))
print('bool(re.search(r"(?:(x)|y)(?(1)y|x)","yx"))',bool(re.search(r"(?:(x)|y)(?(1)y|x)","yx")))
