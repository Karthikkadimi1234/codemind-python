n=input()
b='aeiou'
c=0
for i in b:
    if i in n:
        c+=1
if c==5:
    print(True)
else:
    print(False)