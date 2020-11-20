import xlrd
#应用xlrd这个第三方读取excle的包
excle=xlrd.open_workbook('C:\\Users\\Administrator\\Desktop\\测试用例.xlsx')
#打开't.xlsx'这个表格名
table=excle.sheet_by_name('Sheet1')
#打开'Sheet1'这个表名
value=table.cell_value(1,0)         #一个值一个值的获取
#这里面的数字遵循python的下标，，，所以excle表的 第一列第一行 在python中输入为(0,0)，所以这里是对应excle中的(2,1)
print(value)

#一行一行的读取row           以列表的形式读取出来
row0=table.row_values(0)    #里面的数字为python的下标，加1对应表格的行列号
print(row0)

#一列一列的读取
col0=table.col_values(0)    
print(col0)

##更新
x=table.nrows  #一共多少行
y=table.ncols  #一共多少列
print(x,y)
print('--------------')
for i in range(x):
    print('---------------------------------------------------')
    rowlist=table.row_values(i)
    for j in rowlist:
        print(j,end='\t|')        #\t为制表符号,以 | 进行制表
    print('')
    #print(rowlist)