import pandas as pds

# Series方法
a = pds.Series([8,9,2,1])
b = pds.Series([8,9,2,1], index=["0001","0002","0003","0004"])
print(a)
print(b)

# DataFrame方法
c = pds.DataFrame([[5,6,2,3],[8,4,6,3],[6,4,31,2]])
d = pds.DataFrame([[5,6,2,3],[8,4,6,3],[6,4,31,2]], columns=["0001","0002","0003","0004"], index=["0001","0002","0003"])
print(c)
print(d)

e = pds.DataFrame({
    "01": 4,
    "02": [6,2,3,7],
    "03": list(str(9825))
    })
print(e)

# head与tail方法
print(d.head())
print(d.head(2))
print(d.tail())
print(d.tail(2))

# describe方法以列为单位进行统计
print(d.describe())

# T参数转置
print(d.T)









