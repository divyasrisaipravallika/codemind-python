a=int(input())
n=a
c=0
for i in range(1,a):
    if a%i==0:
        c=c+i
if c==n:
    print("True")
else:
    print("False")