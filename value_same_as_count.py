n=int(input())
a=list(map(int,input().split()))
c=0
b=[]
for i in a: 
    
    if i==a.count(i) and i not in b:
       b.append(i)
print(len(b))