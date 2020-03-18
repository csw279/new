dic={'csw':'170','hd':'158'}

# del 删除字典中的某个元素
del dic['csw']

# update 合并两个字典
dic1={'aa':'130'}
dic.update(dic1)

# 字典的取值
#x=dic['csw']      #当字典没有这个键值对时，代码运行报错
y=dic['hd']       #通过键值对的方法取值
z=dic[1]          #因为字典是无序的，所以无法用下标的方法取值

print(dic)