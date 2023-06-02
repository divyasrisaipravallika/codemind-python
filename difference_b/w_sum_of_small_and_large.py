a=input()
b=list(a.split())
c=[]
d=[]
for i in range(len(b)):
    c.append(max(b[i]))
    d.append(min(b[i]))
m=list(map(ord,c))
n=list(map(ord,d))
x=sum(n)
y=sum(m)
print(abs(x-y))