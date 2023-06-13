def pal(i):
    p=i
    c=0
    v=0
    while i!=0:
        v=i%10
        c=c*10+v
        i=i//10
    return c
a=int(input())
a=a+pal(a)
while pal(a)!=a:
    s=pal(a)
    a=a+s
print(a)