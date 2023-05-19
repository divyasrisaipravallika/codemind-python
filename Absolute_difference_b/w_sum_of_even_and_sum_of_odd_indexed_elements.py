a=int(input())
b=list(map(int,input().split()))
c=0
v=0
for i in range(len(b)):
    if i%2==0:
        c=c+b[i]
    else:
        v=v+b[i]
if c>v:
    print(c-v)
else:
    print(v-c)