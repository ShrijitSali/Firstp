data = [4, 5, 6, 104, 105, 110, 120, 130, 150, 160, 170, 183, 185, 187, 188, 191, 350, 360]
min_valid = 100
max_valid = 200
#list2=[x, fr
# stop = 0
# for index, value in enumerate(data):
#     if value >= min_valid:
#         stop = index
#         break
# print(stop)
# del data[:stop]
# print(data)
#
# # high values
# start = 0
# for index in range(len(data) - 1, -1, -1):
#     if data[index] <= max_valid:
#         start = index + 1
#         break
#
#del data[start:]
# for reverse:
top_index=len(data)-1
for index,value in enumerate(reversed(data)):
    if value<min_valid or value>max_valid:
        print(top_index-index, value)
        del(data[top_index-index])
print(data)
