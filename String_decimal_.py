t=int(input())
for i in range(t):
    n=input()
    c=0
    for j in n:
        if ord(j)>=48 and ord(j)<=57:
            c+=1
    if c==len(n):
        print(True)
    else:
        print(False)