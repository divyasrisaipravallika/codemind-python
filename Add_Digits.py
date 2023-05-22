def num(n):
    
    while n>=10:
        c=0
        while n>0:
            v=n%10
            c=c+v
            n=n//10
        n=c
    return n
a=int(input())
print(num(a))
    
        
        