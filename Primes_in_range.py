def primes(n):
    if n==1:
        return False
    else:
        for i in range(2,int(n**0.5+1)):
            if n%i==0:
                return 0
                break
        return 1
a=int(input())
b=int(input())
p=0
for i in range(a,b+1):
    if(primes(i)):
        p=p+1
print(p)
       