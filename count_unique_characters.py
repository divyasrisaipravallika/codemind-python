a=input()
b=0
c=a.lower()
for i in range(len(c)):
    if c.count(c[i])==1 and c[i]!=" ":
        b=b+1
if b!=0:
    print(b)
else:
    print(-1)