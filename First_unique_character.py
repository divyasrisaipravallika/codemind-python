a=input()
c=a.lower()
v=0
for i in range(len(c)):
    if c.count(c[i])==1:
        print(c[i])
        v=v+1
        break
if v==0:
    print(-1)