def count(n):
    c=0
    if n<0:
        n=n*(-1)
    if(n>0):
        while n!=0:
            v=n%10
            c=c+1
            n=n//10
    return c
    
a=int(input())
b=list(map(int,input().split()))
c=[]
co=0
for i in range(len(b)):
    c.append(count(b[i]))
r=min(c)
for i in c:
    if i==r:
        co=co+1
print(co)