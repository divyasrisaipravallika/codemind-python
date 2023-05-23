a=int(input())
b=list(map(int,input().split()))
v=[]
for i in range(a):
    if b[i]%2==0:
        print(b[i],end=" ")
    else:
        v.append(b[i])
for i in range(len(v)):
    print(v[i],end=" ")