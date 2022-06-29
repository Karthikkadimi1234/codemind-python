n=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    s+=i
d=s//n
if d in a:
    print(True)
else:
    print(False)