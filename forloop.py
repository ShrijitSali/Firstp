# number="9,223;234:948 678,893;833"
# seperators=""
# #string1=""
# str2=[]
# for x in number:
#     if not x.isnumeric():
#         seperators=seperators + x
# print(seperators)
#

#values="".join(x if x not in seperators else " " for x in number ).split()
#print(values)
#print([int(val) for val in values])
#    else:
#        string1=string1 + x
#print(seperators)
#print(string1)

quote = "Alright, but apart from the Sanitation, the Medicine, Education, Wine,Public Order, Irrigation, Road,the Fresh-Water System,and Public Health, what have the Romans ever done for us?"
stri=""
for c in quote:
    if c.isupper():
        stri=stri+" "+c
print(stri)

# Use a for loop and an if statement to print just the capitals in the quote above.
