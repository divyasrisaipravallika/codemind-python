a=input()
b=[]
c=a.lower()
for i in range(len(c)):
    if c[i]!=" ":
        b.append(c[i])
d=list(dict.fromkeys(b))
d.sort()
for i in range(len(d)):
    print(d[i],end="")