def pan(n):
    c=0
    rev=0
    while n!=0:
        c=n%10
        rev=rev*10+c
        n=n//10
    return rev
a=int(input())
b=list(map(int,input().split()))
v=0
for i in range(a):
    if pan(b[i])==b[i]:
        v=v+1
print(v)
        