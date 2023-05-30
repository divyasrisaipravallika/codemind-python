a=int(input())
b=list(map(int,input().split()))
t=-1
for i in range(a):
    if a%2==0:
        print(b[i],end=" ")
    else:
        print(b[i],end=" ")
if a%2!=0:print(0)