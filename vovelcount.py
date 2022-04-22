'''
we will find number of vowels in this string
also try multi line comments
'''
# this is the string
#should i get input from user too?
stri=('i have to find vovels')
str2=input('Enter a string to find vowels')
vow=['a','e','i','o','u']
v=0
v2=0
c=[]
c1=[]
for i in stri:
    if i in vow:
        v+=1
        c.append(i)
print(f"total {v} vowels found")
print(f"the vowels are {c}")
c2={}
for i in stri:
    if i in vow:
        if i in c2:
            c2[i]+=1
        else:
            c2[i]=1
print(c2)
# to check if this counts every letter
c3={}
for i in stri:
    if i in c3:
        c3[i]+=1
    else:
        c3[i]=1
print(f"all letters counted are {c3}")


for i in str2:
    if i.lower() in vow:
        v2+=1
        c1.append(i)
print(f"{v2} vowels found, those are {c1}")