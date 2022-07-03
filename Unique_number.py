n=int(input())
m=str(n)
c=0
for i in m:
    if m.count(i)==1:
        c+=1
if c==len(m):
    print("Unique Number")
else:
    print("Not Unique Number")