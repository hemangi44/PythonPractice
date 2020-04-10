a=int(input("enter a number"))
s=bin(a).replace('0b','')
b=0
for i in range(0,len(s)):
    if '1'== s[i]:
        b+=1
print(s)
print(b)
