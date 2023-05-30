a=int(input())
b=list(map(int,input().split()))
d=int(input())
c=[]
v=0
for i in range(a):
    if b.count(b[i])==d:
        c.append(b[i])
mylist = list(dict.fromkeys(c))
if len(mylist)==0:print(-1)
for i in range(len(mylist)):
    print(mylist[i],end=" ")
