n=input()
m=int(n)
c=m
l=len(n)
r=m*m
x=r%(10**l)
if x==c:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")