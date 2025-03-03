# Dictionary methods
di = {False:"Cricket", 2:"Football", 3:"Badminton", 1:"Hockey"}
dj = {8:["Mars","Jupiter","Earth"], 7:"Saturn"}

#print(dj[8][0::2])

print(di)

#di.clear() # It removes all the key-value pairs from the dictionary
#                making it an empty dictionary

#print(di)

print(di.get(2)) # Java programmers are used to it
print(di[2])

print(di.keys()) # Returns just the keys of the dictionary (return type: list)

print(di.values()) # Returns just the values of the dictionary as a list

print(di.items())
# This returns a list consisting of tuples
# each tuple in the returned list represents a key:value pair
# the 0th index of any tuple is a key and 1st index is the corresponding value

di[0] = "Soccer"
print(di)


di = {False:"Cricket", 2:"Football", 3:"Badminton", 1:"Hockey"}
dj = {8:["Mars","Jupiter","Earth"], 3:"Saturn"}

di.update(dj)
print(di)
print(dj)
