a=int(input())
b=list(map(int,input().split()))
c,d=map(int,input().split())
v=[]
s=0
for i in range(len(b)):
    if b[i]>=c and b[i]<=d:
        v.append(b[i])
if len(v)!=0:
    print(max(v))
else:
    print(-1)