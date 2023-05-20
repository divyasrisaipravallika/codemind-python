a=int(input())
l=a
c=0
t=1
while a!=0:
    v=a%10 
    c=c+v 
    t=t*v
    a=a//10
if c==t:print("Spy Number")
else:print("Not Spy Number")