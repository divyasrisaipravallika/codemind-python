def cou(n):
    c=0
    for i in range(2,n):
        if n%i==0:
            c=c+1
    if n==1:return 0
    elif n==2:return 1
    elif c>0: return 0
    else:return 1
a=int(input())
#print(a)
b=list(map(int,input().split()))
#print(b)
#c=int(input())
d=0
c=0
for i in range(a):
    if cou(b[i])==1:
        d=d+b[i]
        c=c+1
v=float(d/c)
print("%.2f"%v)

            