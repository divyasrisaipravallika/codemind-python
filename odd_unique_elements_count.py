a=int(input())
b=list(map(int,input().split()))
mylist = list(dict.fromkeys(b))
v=0
for i in range(len(mylist)):
    if mylist[i]%2!=0:
        v=v+1
print(v)