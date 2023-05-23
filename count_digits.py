def count(n):
    c=0
    if n<0:
        n=n*(-1)
    if n==0:
        d=1
        return d
    else:
        while n!=0:
            v=n%10
            c=c+1
            n=n//10
    return c
a=int(input())
b=list(map(int,input().split()))
for i in range(a):
    print(count(b[i]),end=" ")