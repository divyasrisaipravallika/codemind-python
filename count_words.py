a=list(map(str,input().split()))
c=0
d=[]
v=['a','e','i','o','u','A','E','I','O','U']
for i in range(len(a)):
    if a[i][0] in v and a[i][-1] not in v:
        c=c+1
print(c)