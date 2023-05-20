a=int(input())
while a!=0:
    b=int(input())
    c=b
    t=0
    while b!=0:
        v=b%10
        t=t*10+v 
        b=b//10
    if c==t:
            print("True")
    else:print("False")
    a=a-1