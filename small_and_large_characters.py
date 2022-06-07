a=input()
a=a.split(' ')
b=list(a)
for i in range(len(b)):
    print(min(b[i]),max(b[i]),end=' ')
