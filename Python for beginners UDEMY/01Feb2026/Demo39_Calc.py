def calc(a,b):
    w = a+b
    x = a-b
    y = a*b
    z = a/b
    return w,x,y,z

result = calc(10,5)
print(result)
for i in result:
    print(i)