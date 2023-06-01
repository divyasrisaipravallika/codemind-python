a=input()
c=0
for i in range(len(a)):
    if ord(a[i])>=97 and ord(a[i])<=122:
        c=c+1
print(c)
