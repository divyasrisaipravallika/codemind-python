b=list(input())
c=0
v=['a','e','i','o','u']
for i in range(len(b)):
    if b[i] in v:
        v.remove(b[i])
        c=c+1
if len(v)==0: 
    print(0)
else:
    for i in range(len(v)):
        print(v[i],end=" ")
