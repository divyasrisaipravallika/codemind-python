e=int(input())
c=0
for i in range(1,e,1):
     if e%i==0:
         c=c+i
#print(c)
if c==e:
    print("True")
else:
    print("False")