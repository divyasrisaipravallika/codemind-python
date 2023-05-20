a=int(input())
b=list(map(int,input().split()))
c=1
for i in range(len(b)):
    if b[i]%2==0:
        c=i
print(c)