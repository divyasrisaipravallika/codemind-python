a,b=map(int,input().split())
c=list(map(int,input().split()))
d=list(map(int,input().split()))
m=list(dict.fromkeys(c))
n=list(dict.fromkeys(d))
for i in range(len(m)):
    if m[i] in n:
        print(m[i],end=" ")