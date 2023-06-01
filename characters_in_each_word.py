a=input()
c=0
d=[]
for i in range(len(a)):
    if a[i]==" ":
        print(len(d),end=" ")
        d=[]
        c=c+1
    else:
        d.append(a[i])
if c==0:
    print(len(a))
else: print(len(d))