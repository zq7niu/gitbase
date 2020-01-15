size = 8
array = [[0]*size]
#得到一个size*size二位列表
for i in range(size-1):
	array+=[[0]*size]


#控制方向
#0代表向下，2代表向右，
orient = 0

#j控制行，k控制列
j,k=0,0
#控制程序将1~SIZE*SIZE的书填入二维数组

for i in range(1,size*size+1):
	array[j][k] = i
	
	#1号转弯线
	if j+k == size - 1:
		if j>k:
			orient=1
		else:
			orient=2
	#位于2号转弯线
	elif j == k and j>=size/2:
		orient =3
	#位于3号转弯线
	elif j+1==k and k<=size/2:
		orient=0
		

	if orient == 0:	#0代表向下
		j+=1
	elif orient == 1:	#1代表向右
		k+=1
	elif orient == 2:	#2代表向左
		k-=1	
	elif orient == 3:	#3代表向上
		j-=1

for ele in array:
	for e in ele :
		print('%02d' % e,end=' ')
		
	print('')
	

	