a=int(input())
b=list(map(int,input().split()))
for i in range(len(b)):
    for j in range(len(b)-1):
        if b[j]>b[j+1]:
            temp=b[j]
            b[j]=b[j+1]
            b[j+1]=temp
for i in range(len(b)):
    print(b[i],end=" ")