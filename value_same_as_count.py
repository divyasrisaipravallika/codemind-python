a=int(input())
b=list(map(int,input().split()))
c=[]
v=0
for i in range(a):
    if b.count(b[i])==b[i]:
        c.append(b[i])
mylist = list(dict.fromkeys(c))
for i in range(len(mylist)):
    v=v+1
print(v)