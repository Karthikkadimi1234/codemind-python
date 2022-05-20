import math
t=int(input())
for i in range(t):
    n=int(input())
    a=round(math.sqrt(n),2)
    if a*a==n:
        print(True)
    else:
        print(False)