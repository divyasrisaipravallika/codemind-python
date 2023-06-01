b=list(input())
c=0
v=['a','e','i','o','u']
d=['A','E','I','O','U']
for i in range(len(b)):
    if b[i] in v:
        c=c+1
    elif b[i] in d:
        c=c+1
print(c)