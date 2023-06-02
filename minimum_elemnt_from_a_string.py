a=input()
b=list(a.split())
v=min(b[-1])
if v.lower() not in b[-1]:
    print(v)
else:
    print(v.lower())