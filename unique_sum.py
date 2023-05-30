a=int(input())
b=list(map(int,input().split()))
c=list(dict.fromkeys(b))
print(sum(c))