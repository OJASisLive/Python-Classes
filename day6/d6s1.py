# String methods and functions

a = "computer science is a good subject"

length = len(a) # Length function

print(length)

print(a.endswith("gsg")) # Checks whether it ends with provided suffix or not


print(a.count('e')) # Counts the no. of occurances of given parameter

print(a)
print(a.capitalize()) # Capitalizes the first letter of the first word


print(a.find("sc")) # It returns the index of the beginning of the first occurance of
                    # the given parameter
                    
print(a.replace("good","bad"))

b = 'PYTHOn'
print(b.isupper())

b = 'pyThon'
print(b.islower())

print(b.upper())

print(b.lower())

c = "admin123"

print(c.isalnum())

c = "admin"

print(c.isalnum())

c = "123"

print(c.isalnum())

c = "#^%,."

print(c.isalnum())

c = "         "

print(c.isalnum())

c = "admin cse 123"

print(c.isalnum())

c = "   d    "

print(c.isspace())

d = "     Om Shah      "

print("\n\n")

print(d)
print(d.lstrip())
print(d.rstrip())
print(d.strip())

name = input("Enter your name")
print(name.capitalize())

c = "admin cse 123"
c_list = c.split(" ") # ["admin", "cse", "123"]
print(c_list)






