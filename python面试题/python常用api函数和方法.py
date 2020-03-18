len                 求列表，元组中'所有元素'的数量      len('python')=6   
count               计算列表，元组'某个元素'的数量      x='adaas'      x.count(a)=3
index               找到'某个元素'最早出现的'下标位置'  x='asdnmjd'    x.index(d)=2

list:
f=[1,2,3]

append       添加元素到列表的末端    f.append(4)  print(f)=[1,2,3,4]

insert       添加元素到指定位置      f.insert(0,'陈')  print(f)=['陈',1,2,3]

remove       删除某个指定的元素            f.remove('王')  print(f)=[1,2,3]

pop          移出某个元素，但是要拿另一个变量保存   x=f.pop()  空值则是清除最后一个值    y=f.pop(1)#用下标表明元素

clear        清除所有的元素，让它成为一个空的类型。  f.clear()  print(f)=[]  