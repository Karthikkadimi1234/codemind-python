n=input()
b='aeiouAEIOU'
c=0
for i in n:
    if i in b:
        c+=1
print(c)