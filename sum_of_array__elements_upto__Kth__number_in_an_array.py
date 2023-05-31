a=int(input())
b=list(map(int,input().split()))
c=0
d=int(input())
for i in range(a):
    if b[i]!=d:
        c=c+b[i]
    else:
        c=c+b[i]
        break
print(c)