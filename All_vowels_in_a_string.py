b=list(input())
c=0
v=['a','e','i','o','u']
d=['A','E','I','O','U']
for i in range(len(b)):
    if b[i] in v:
        v.remove(b[i])
    elif b[i] in d:
        d.remove(b[i])
if len(v)==0 or len(d)==0: 
    print("True")
else:
    print("False")
