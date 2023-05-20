a=int(input())
c=0
t=a*a
while t!=0:
    v=t%10
    c=c+v 
    t=t//10
if c==a:print("Neon Number")
else:print("Not Neon Number")