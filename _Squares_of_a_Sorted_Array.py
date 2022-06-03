n=int(input())
a=list(map(int,input().split()))
a.sort()
b=[]
for i in a:
    c=i*i
    b.append(c)
b.sort()
print(*b)