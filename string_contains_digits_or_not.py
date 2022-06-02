t=int(input())
for i in range(t):
    n=input()
    c=0
    for i in n:
        if i.isdigit():
            c+=1
    if(c>=1):
        print("Yes")
    else:
        print("No")