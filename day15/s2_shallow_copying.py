a = ["Mercury", "Venus", "Earth"]

b = a

print("The value of a is: ", a)
print("The value of b is: ", b)


a.append("Mars")


print("-----After Changing a-----")

print("The value of a is: ", a)
print("The value of b is: ", b)

# Mutable datatypes are shallowly copied
# Shallow copying
# It will store only the address of the
# original variable instead of making a copy
# of the data.

# Changes made in the original variable will affect
# the copy of the variable.
