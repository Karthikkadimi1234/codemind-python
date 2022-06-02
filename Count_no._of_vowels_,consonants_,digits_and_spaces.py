n=input()
cv=0
co=0
cd=0
cw=0
for i in n:
    if i in 'aeiou':
        cv+=1
    if i.isalpha() and i not in 'aeiou':
        co+=1
    if i.isdigit():
        cd+=1
    if i==' ':
        cw+=1
print("Vowels:",cv)
print("Consonants:",co)
print("Digits:",cd)
print("White spaces:",cw)