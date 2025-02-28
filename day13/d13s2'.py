att = {562:"Bhanu", 123:"Chirag", 700:"Om", 456:"Yashwanth B", 145:"Aakash", 145:"Dhun"}
print(att[145])
print(att)


# li = ["AAA", "CCC", "BBB"]
# print(li[1])


# Rollno        Name
#   1          Aakash
#   2          Bhanu
#   3          Chirag
#   4          Om
#   5          Yashwanth B
#   6          Yashwanth K


# Properties of a dictionary
'''
    1. It is unordered
    2. It is not indexed
    3. It is mutable
    4. Cannot contain duplicate keys (it considers the latest key value pair)
    for ex: {1:"AAA", 2:"BBB", 3:"CCC", 2: "DDD"} then python will
            overwrite the value of 2 from BBB to DDD
            and BBB will be forgotten forever...

            final dictionary will look like {1:"AAA", 3:"CCC", 2: "DDD"}
'''

temps = [31, 30, 31, 32, 32, 34]
print(temps)
