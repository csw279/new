def x2(a,b=2):
    s=1
    while b>0:
        b=b-1
        s=s*a
    return s

def zhuce(a,b,age=20,weigh=50):
    print('name:',a)
    print('sex:',b)
    print('age',age)
    print('weigh',weigh)

'''a=eval(input())
b=eval(input())
x=x2(a,b)
print(x)'''

zhuce('陈思维','男',age=23,weigh=60)  #  return 后面一般不和 print 连用，因为 print 本身就是 None
zhuce('贺丹','女')                    #  return 后面一般不和 print 连用, 因为 print 本身就是 None
