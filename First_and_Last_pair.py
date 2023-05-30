a=int(input())
b=list(map(int,input().split()))
t=-1
#print(a//2+1)
if a%2!=0:
    for i in range(a//2+1):
        if t!=-1*(a//2+1):
            print(b[i],b[t],end=" ")
        else:
            print(b[i],0)
        t=t-1
else:
    for i in range(a//2):
        print(b[i],b[t],end=" ")
        t=t-1