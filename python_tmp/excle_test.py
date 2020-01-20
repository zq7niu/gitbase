import xlwings as xw
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#建立excel表连接
wb = xw.Book("e:\example.xlsx")
#实例化工作表对象
sht = wb.sheets["sheet1"]
#返回工作表绝对路径
wb.fullname
#返回工作簿的名字
sht.name
#在单元格中写入数据
sht.range('A1').value = "xlwings"
#读取单元格内容
sht.range('A1').value
#清除单元格内容和格式
sht.range('A1').clear()
#获取单元格的列标
sht.range('A1').column
#获取单元格的行标
sht.range('A1').row
#获取单元格的行高
sht.range('A1').row_height
#获取单元格的列宽
sht.range('A1').column_width
#列宽自适应
sht.range('A1').columns.autofit()
#行高自适应
sht.range('A1').rows.autofit()
#给单元格上背景色，传入RGB值
sht.range('A1').color = (34,139,34)
#获取单元格颜色，RGB值
sht.range('A1').color
#清除单元格颜色
sht.range('A1').color = None
#输入公式，相应单元格会出现计算结果
sht.range('A1').formula='=SUM(B6:B7)'
#获取单元格公式
sht.range('A1').formula_array
#在单元格中写入批量数据，只需要指定其实单元格位置即可
sht.range('A2').value = [['Foo 1', 'Foo 2', 'Foo 3'], [10.0, 20.0, 30.0]]
#读取表中批量数据，使用expand()方法
sht.range('A2').expand().value
#其实你也可以不指定工作表的地址，直接与电脑里的活动表格进行交互
xw.Range("E1").value = "xlwings"# 读取
xw.Range("E1").value
#支持写入numpy array数据类型
np_data = np.array((1,2,3))
sht.range('F1').value = np_data
#支持将pandas DataFrame数据类型写入excel
df = pd.DataFrame([[1,2], [3,4]], columns=['a', 'b'])
sht.range('A5').value = df
sht.range('A5').options(pd.DataFrame,expand='table').value
#将matplotlib图表写入到excel表格里
%matplotlib inline
fig = plt.figure()
plt.plot([1, 2, 3, 4, 5])
sht.pictures.add(fig, name='MyPlot', update=True)