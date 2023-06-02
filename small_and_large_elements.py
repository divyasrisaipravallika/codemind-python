a=input()
b=list(a.split())
c=[]
d=[]
for i in range(len(b)):
    c.append(max(b[i]))
    d.append(min(b[i]))
print(d[0],c[-1])