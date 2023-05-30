a=int(input())
b=list(map(int,input().split()))
m=list(dict.fromkeys(b))
c=0
for i in range(len(m)):
    if m[i]%2!=0:
        c=c+m[i]
print(c)