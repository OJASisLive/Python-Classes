# String
print("string (str)")
a = "Om"
b = a # Copying

print("The value of a is:",a)
print("The value of b is:",b)

print("\n-------After Changing--------\n")

a = "Aashish"
print("The value of a is:",a)
print("The value of b is:",b)

print("\nThis is deep copying\n")

# int
print("int")
a = 5
b = a # Copying

print("The value of a is:",a)
print("The value of b is:",b)

print("\n-------After Changing--------\n")

a = 8
print("The value of a is:",a)
print("The value of b is:",b)

print("\nThis is deep copying\n")

# float
print("float")
a = 7.5
b = a # Copying

print("The value of a is:",a)
print("The value of b is:",b)

print("\n-------After Changing--------\n")

a = 10.5
print("The value of a is:",a)
print("The value of b is:",b)

print("\nThis is deep copying\n")

# bool
print("bool")
a = True
b = a # Copying

print("The value of a is:",a)
print("The value of b is:",b)

print("\n-------After Changing--------\n")

a = False
print("The value of a is:",a)
print("The value of b is:",b)

print("\nThis is deep copying\n")

# None
print("bool")
a = None
b = a # Copying

print("The value of a is:",a)
print("The value of b is:",b)

print("\n-------After Changing--------\n")

a = 5.7
print("The value of a is:",a)
print("The value of b is:",b)

print("\nThis is deep copying\n")

# Tuple
print("tuple")
a = ("Apple","Mango","Jack")
b = a

print("The value of a is:",a)
print("The value of b is:",b)

print("\n-------After Changing--------\n")

a = ("Mercury", "Venus", "Earth")

print("The value of a is:",a)
print("The value of b is:",b)
print("\nThis is deep copying\n")

# List
print("list")
a = ["Apple","Mango","Jack"]
b = a

print("The value of a is:",a)
print("The value of b is:",b)

print("\n-------After Changing--------\n")

a.pop()

print("The value of a is:",a)
print("The value of b is:",b)
print("\nThis is shallow copying\n")

# Dictionaries
print("dict")
a = {"Names":["Om","Jay","Amit"], "Marks":[70,80,90]}
b = a

print("The value of a is:",a)
print("The value of b is:",b)

print("\n-------After Changing--------\n")

a.pop("Marks")

print("The value of a is:",a)
print("The value of b is:",b)
print("\nThis is shallow copying\n")


