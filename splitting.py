number = "9,223,372,036,854,775,807"
print(number.split(","))

separators = [" ", ","]
# values="".join(char if char not in separators else " " for char in number).split()
# print(values)
# for x in number:
x = ",".join(x for x in number)
print(x)
# print(number.split())
#n="".join(n for n in number).split()
#print(n)      # if u give space in between "" then too it will give generated list
print(list(number))  # this code will generate the bellow list
generated_list = [
    '9', ',', '2', '2', '3', ',', '3', '7', '2', ',', '0', '3', '6', ',', '8', '5', '4', ',', '7', '7',
    '5', ',', '8', '0', '7']

values="".join(generated_list).split() #.split converts to string in a list
value2= "".join(generated_list)
print(values)
print(value2+"value2")
#replace , with space
value3= "".join(x if x not in separators else " " for x in number).split()
print(value3)
print(list(value3))

value4="".join(generated_list)
value_list=value4.split()
print(value_list)
print("value list")
#replace values in place str to int
for index in range(len(value_list)):
#    value_list[index]=int(value_list[index])
print(value_list)

#another method to convert to int
integer_val=[]
for x in value_list:
    print(x)
    integer_val.append(int(x))
print(integer_val)