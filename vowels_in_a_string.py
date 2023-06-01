b=list(input())
c=input()
n=0
v=['a','e','i','o','u']
d=['A','E','I','O','U']
for i in range(len(b)):
    if c==b[i]:
        print("True")
        print(i)
        n=n+1
        break
if n==0:
    print("False")