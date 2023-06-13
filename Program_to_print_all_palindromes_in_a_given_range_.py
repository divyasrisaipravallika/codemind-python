o=int(input())
b=int(input())
for i in range(o,b):
    p=i
    c=0
    v=0
    while i!=0:
        v=i%10
        c=c*10+v
        i=i//10
    if c==p:
        print(c,end=" ")