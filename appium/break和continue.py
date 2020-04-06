# n = 1
# while n <= 100:             # n 开始进入while循环    
#     if n > 10:              # 当n = 11时，条件满足，执行break语句
#                             # break 语句配合 if 判断满足条件则跳出循环
#         break               # break语句会结束当前循环
#     print(n)
#     n = n + 1
# print('END')

# sum=0
# n=0
# while n<10:
#     sum=sum+n
#     n=n+1
#     if n==5:
#         continue
#     print(n)
# print(sum)

sum=0
n=0
while n<10:
    sum=sum+n
    n=n+1
    if n==5:
        break
    print(n)
print(sum)


    
