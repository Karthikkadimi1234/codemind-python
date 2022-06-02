n=int(input())
s=0
a=list(map(int,input().split()))
for i in a:
    s+=i
A=s//n
if A in a:
    print(True)
else:
    print(False)