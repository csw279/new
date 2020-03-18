# # x={'a':1,'b':2}

# # for i in x:
# #     print("{} {}".format(i,x[i]),end='@@\n')

# # x=[1,2,3,45,6]  ##  打印的时候本来就是换行打印
# # for i in x:
# #     print(i,end=' ')

# x=[1,2,3,4,5,6,7,8,9]
# for i in x:
#     while i >5:
#         print('{}该数字大于5'.format(i))
#         break

# ##请0-100之间的奇数之和
sum=0
for i in range(10):
    while i % 2!=0:
        sum=sum+i
        break
print(sum)

# while是死循环，不满足则一直循环下去，需要搭配 for 以及 break 断掉该循环然后再去用 for 的值去做循环 





