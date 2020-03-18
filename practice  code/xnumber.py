def FC(*a):
    sum=0
    for i in a :
        sum=sum+i*i
    return sum
number=[1,2,3,4,5]
a=FC(*number)       #  *符号表示直接取用该  list  或者  tuple  的元素     当然前提number是列表或者元组   如果是输入  输入的时候就应该是输入列表
print(a)