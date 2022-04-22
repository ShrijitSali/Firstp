numbers=[1,45,31,12,60]

for number in numbers:
    if number % 8==0:
        #reject
        print("Unexcepted numbers")
        break
else:
    print("All numbers are fine")

#for else loop... if the if (above block) runs unsucessfully.. then do else
#eg: if it didnt break.. meaning if not satisfied inturn: for is not satisfied..
#so else