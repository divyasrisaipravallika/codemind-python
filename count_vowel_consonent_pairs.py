a=input()
c=0
d=[]
l=len(a)
mid=l//2
v='aeiouAEIOU'
for i in range(mid):
    if a[i].isspace() or a[l-i-1].isspace():
        continue
    if a[i] in v and a[l-i-1] not in v:
        c=c+1
    if a[i] not in v and a[l-i-1] in v:
        c=c+1
            
print(c)
    