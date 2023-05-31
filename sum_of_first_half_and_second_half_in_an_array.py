a=int(input())
b=list(map(int,input().split()))
c=0
v=0
if a%2==0: 
    for i in range(a//2): 
        c=c+b[i] 
    for i in range(a//2,a):
        v=v+b[i]
else: 
    b.append(0)
    for i in range(a//2):
        c=c+b[i] 
    for i in range(a//2,a):
        v=v+b[i]
print(c)
print(v)