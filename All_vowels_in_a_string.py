n=input()
b=set(n)
c=0
for i in b:
    if i in 'aeiou':
        c+=1
if c==5:
    print(True)
else:
    print(False)