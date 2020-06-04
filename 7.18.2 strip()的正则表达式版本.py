'''
思路：在正则表达式里面使用format()函数来替代传入的参数字符。
如果正则表达式{0}跟format的{0}冲突，正则表达式可以改为{{0}}
format()语法：
>>> "{0} {1}".format("hello", "world")  # 设置指定位置
'hello world'
'''
import re

def fakeStrip(longStr, string):
    stripRex = re.compile(r'^{0}*|{0}*$'.format(string))
    return stripRex.sub('',longStr)

inputStr1 = input("请输入原字符串：")
inputStr2 = input("请输入要去除的字符：")
if inputStr2 == '':
    inputStr2 = '\s'
print("去除后的字符串为:",fakeStrip(inputStr1,inputStr2))