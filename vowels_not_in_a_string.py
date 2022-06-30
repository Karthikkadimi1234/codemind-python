n=input()
b='aeiou'
c=[]
for i in b:
    if i in b and i not in n:
        c.append(i)
if c==[]:
    print("0")
else:
    print(*c)
    