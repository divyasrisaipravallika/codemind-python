a=input()
c=0
for i in range(len(a)):
    if ord(a[i])>=65 and ord(a[i])<=90:
        c=c+1
print(c)
