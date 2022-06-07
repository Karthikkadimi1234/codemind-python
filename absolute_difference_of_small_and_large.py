n=input()
n=n.split(' ')
b=list(n)
for i in b:
    a=min(i)
    b=max(i)
    print(abs(ord(a)-ord(b)),end=' ')