#continue statement

stu = ["Bhavesh", "Lathika", "Jayashree",
       "Praveen", "Chirag"]
age = [13,20,17,18,15]

for x in range(0,len(stu)):
    if age[x] == 17:
        continue

    print(stu[x],"->",age[x])
    print("Hello")


# break - ends the loop
#continue- ends the current iteration only
