a=int(input())
b=list(map(int,input().split()))
c=sorted(b)
d=sorted(b,reverse=True)
if c==b or d==b:
    print("yes")
else:
    print("no")