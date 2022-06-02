n=input()
a=list(n)
s=0
for i in a:
    if i.isdigit():
        s+=int(i)
print(s)