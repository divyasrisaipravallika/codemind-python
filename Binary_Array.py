a=int(input())
b=list(map(int,input().split()))
c=0
for i in range(a):
    if b[i]==0 or b[i]==1:
        c=c+1
    else:
        break
if c==a: print("True")
else: print("False")