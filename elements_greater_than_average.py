n=int(input())
a=list(map(int,input().split()))
s=0
c=0
for i in a:
    s+=i
d=s//n
for i in a:
    if i>=d:
        c+=1
print(c)