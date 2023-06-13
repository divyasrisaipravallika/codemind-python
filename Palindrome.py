a=int(input())
p=a
c=0
v=0
while a!=0:
    v=a%10
    c=c*10+v
    a=a//10
if p==c:
    print("True")
else:
    print("False")