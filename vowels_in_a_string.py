n=input()
m=input()
f=0
a=list(n)
for i in range(len(a)):
    if m is a[i]:
        f=1
        break
if f==1:
    print(True)
    print(i)
else:
    print(False)