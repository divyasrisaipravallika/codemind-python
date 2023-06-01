a=input()
c=0
d=[]
n=[]
for i in range(len(a)):
    if a[i]==" ":
        n.append(len(d))
        d=[]
        c=c+1
    else:
        d.append(a[i])
if c==0:
    print(len(a))
else: n.append(len(d))
if len(n)!=0:print(min(n))