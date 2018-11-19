import numpy
# numpy创建一维数组的语法
# numpy.array([a,b,c,...,n])
arr1 = numpy.array([69,77,22,33,34,63,11])

# numpy创建二维数组的语法
# numpy.array([[a,b],[c,d,e],[f,g],...,[n]])
arr2 = numpy.array([[100,54,35],[33,55,44],[99,77,88]])

# 排序sort
arr1.sort()
arr2.sort()

# 取最值
max1 = arr1.max()
max2 = arr2.max()
min1 = arr1.min()
min2 = arr2.min()

# 切片运算
# 数组[起始下标:最终下标+1]
range1 = arr1[1:4]
print(range1)
range11 = arr1[:4]
print(range11)
range111 = arr1[1:]
print(range111)
