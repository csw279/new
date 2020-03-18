'''print('%2d-%02d' % (3, 1))
print('%2d'%(3))
print('%.2f' % 3.1415926)'''
# % 的格式化用法
a=input('请输入姓名:')
b=eval(input('请输入身高:'))
print('我的名字叫做%s,我身高%d'%(a,b))

#.format()的用法,他会传入参数依次替换占位符{}

a=input('请输入姓名:')
b=eval(input('请输入身高:'))
print('我的名字叫{},我身高{}'.format(a,b))