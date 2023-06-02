a=input()
b=list(a.split())
c=[]
d=[]
for i in range(len(b)):
    c.append(max(b[i]))
    d.append(min(b[i]))
m=list(map(ord,c))
n=list(map(ord,d))
for i in range(len(m)):
    print(abs(m[i]-n[i]),end=" ")