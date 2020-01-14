a='a\tb\tc'
print(a)

b='我爱%s'
print(b % 'python')
#s先转换为字符串再替换，d先转换成十进制整数再替换
c='我最爱的图书是%s，价格为%d'
print(c % ('疯狂python讲义',128))
#最右侧字符不包括
print(c[2:6:2])