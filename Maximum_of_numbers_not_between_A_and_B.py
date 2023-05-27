a=int(input())
b=list(map(int,input().split()))
c,d=map(int,input().split())
s=[]
for i in range(len(b)): 
    if b[i]<c or b[i]>d: 
        #print(b[i],end=" ")
        s.append(b[i])
if len(s)==0:
    print(-1)
else: print(max(s))