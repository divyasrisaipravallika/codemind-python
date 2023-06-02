a=input()
c=[]
for i in range(len(a)):
    if a[i]!=" ":
        c.append(a[i])
print(min(c),end=" ")
print(c.count(min(c)),end=" ")
print(max(c),end=" ")
print(c.count(max(c)))