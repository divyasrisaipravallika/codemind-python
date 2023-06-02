a=input()
b=[]
c=a.lower()
for i in range(len(c)):
    if c[i]!=" " and c.count(c[i])==1:
        b.append(c[i])
#d=list(dict.fromkeys(b))
b.sort()
for i in range(len(b)):
    print(b[i],end="")