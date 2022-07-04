n=int(input())
a=list(map(int,input().split()))
b=a[::-1]
j=0
c=0
for i in b:
    c+=i*10**j
    j+=1
d=c+1
e=str(d)
e=list(e)
print(*e)