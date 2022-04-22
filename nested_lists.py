menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam", "spam"],
]
#
# for meal in menu:
#     if "spam" not in meal:  #those list that will not contain spam
#         print(meal)
#
#         for item in meal:
#             print(item)    #only selected above will be used or processed further
#
#     else:
#        print(f"{meal} has {meal.count('spam')} spam") #count will directly count the occurances of word in bracket

# remove spam word
# for meal in menu:
#     for index in range(len(meal) - 1,-1,-1):
#         # print(index,word)
#         if meal[index] == "spam":
#             del meal[index]
#     print(meal)

#remove spam word method 2

# for meal in menu:
#     for item in meal:
#         if item !="spam":
#             print(item)
#     print()

#use Generator

for meal in menu:
    item=", ".join((item for item in meal if item!="spam"))
    print(item)