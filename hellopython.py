# coding: utf-8
a=123

print (a)

b='abcde'

print(b)

c="123"


var1="我爱北京’去北京玩"

f=var1+c
print(f)
longstr='''
明天去旅游嘛
去呗
去哪里呢
去三亚吧
'''
d=b+c

e=b+repr(a)

print(d)
print(c)
print(e)
print(longstr)

#转换成字节串
var2="我爱中国".encode()
print(var2)

#字节串转换成字符串
var4=b'\xe6\x88\x91\xe7\x88\xb1\xe4\xb8\xad\xe5\x9b\xbd'
print(var4.decode("utf-8"))

#原始字符串
var3=r'我们都/n是好人'
print(var3)