#递归    自己不断调用自己

def chufa(x):
    x=x/2

    if x >10:
        return chufa(x)
    else:
        return x


b=100
a=chufa(b)
print(a)