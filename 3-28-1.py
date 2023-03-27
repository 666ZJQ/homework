# 第一题
import re

def isNum(s):
    # 匹配整数、浮点数或复数的正则表达式
    pattern = r'^[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?[jJ]?$'
    
    # 判断字符串是否符合正则表达式
    return bool(re.match(pattern, s))
