a=int(input())
b=list(map(int,input().split()))
mylist = list(dict.fromkeys(b))
for i in range(len(mylist)):
    print(mylist[i],end=" ")
