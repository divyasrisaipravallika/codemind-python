a=int(input())
b=list(map(int,input().split()))
c=sum(b)
e=c//a
#print(c)
d=0
for i in range(a):
    if b[i]<=e:
        d=d+1
print(d)
        