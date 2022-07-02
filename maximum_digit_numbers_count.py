n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    c=len(str(i))
    b.append(c)
for i in a:
    if max(b)==len(str(i)):
        print(i,end=' ')
