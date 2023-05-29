a=int(input())
b=list(map(int,input().split()))
s = [str(i) for i in b]
binary = int("".join(s))
decimal, i = 0, 0
while(binary != 0):
    dec = binary % 10
    decimal = decimal + dec * pow(2, i)
    binary = binary//10
    i += 1
print(decimal)