a=input()
b=input()
n=a.lower()
m=b.lower()
v=0
o=[]
c=list(dict.fromkeys(n))
d=list(dict.fromkeys(m))
if len(c)>=len(d):
    for i in range(len(c)):
        if c[i]!=" " and c[i] in d:
            v=v+1
            o.append(c[i])
else:
    for i in range(len(d)):
        if d[i]!=" " and d[i] in c:
            v=v+1
            o.append(d[i])
if v==0:
    print(-1)
else:
    o.sort()
    for i in range(len(o)):
        print(o[i],end="")