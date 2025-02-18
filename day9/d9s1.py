# List methods and functions

# Sorted(list_name) - this temporarily sorts the list
# list_name.sort() - this permanently sorts the list

names = ['Om', 'Punya', 'Ishanth', 'Vineeth', 'Sankar']

print(names)

# names = sorted(names, reverse=True)

'''
names.sort()

print(names)

names.reverse()

print(names)
'''

# Append method

names.append("Dinesh") # value

print(names)

names.insert(2, "Surya") # Arguments index value(object)

print(names)

# Pop method

names.pop(2) # arguments are index(optional, default -1)

print(names)

# Index method

print(names.index("Ishanth"))


# Slicing [] defining list []

print(names) # args value

print(names.count("Om")) # Returns the count of occurences of "Om" in the list

print(len(names))

names2 = ['Nandhini', "Ishita"]

names.extend(names2)

print(names)

print(type(names))

names.clear()

print(names)


# Append, Insert, Extend

# pop - Takes index
# remove - Takes the value (removes the first occurance)
# clear - empties the list

