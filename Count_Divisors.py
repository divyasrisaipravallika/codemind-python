a,b,c=map(int,input().split())
t=0
for i in range(a,b+1):
    if i%c==0:
        t=t+1
print(t)