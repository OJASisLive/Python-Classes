'''
Create a dictionary consisting of 3 items,
Append an item to the dictionary
change an item in the dictionary
modify value for the existing key, and
delete an item from it
print...
1. just the keys
2. just the values
3. The whole dictionary
clear the dictionary and make it an empty one
'''

#creating an empty dictionary
a={}
print(a)

#create a dictionary consist of items
a={"a":"Nithya", "b":"Nila", 3:"Deekshika", True:"Nilani",
   False:"dakshu", 7:"srihaan", 7.5:"nilan", None:"sai"}
print(a)

#append an item to dictionary
a[9]="sri"
print(a)

#modify value for existing key
a[0]="Rashmita"
print(a)

a[1]="priya"
print(a)

#delete an item from it
a.pop(1)
print(a)


#print jus the keys
a.keys()
print(a)


#print jus the keys
print(a.keys())

#print jus the values
print(a.values())

#print the whole dictionary
print(a)

#clear the dictionary and make it an empty one
a.clear()
print(a)








