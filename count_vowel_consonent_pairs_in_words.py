a=list(map(str,input().split()))
c=0
v='aeiouAEIOU'
for i in range(len(a)):
    l=len(a[i])
    for j in range(len(a[i])):
        if a[i][j] in v and a[i][l-j-1] not in v:
            c=c+1
        if a[i][j] not in v and a[i][l-j-1] in v:
            c=c+1
print(c//2)