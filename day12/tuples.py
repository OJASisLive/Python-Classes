# I want to create an empty tuple
# Method-1
a = ()
print("Type of a",type(a))

# Method-2
b = tuple()
print("Type of b",type(b))


# I want a single valued tuple
c = "Om"
c = tuple(c)
print("Type of c",type(c))

d = ("Om",)
e = (12,)
f = ("Om")
g = tuple(f)

print("Type of f",type(f))
# When we want to make a single valued tuple
# tip: do not forget to add a comma
print("Type of d",type(d))


#print("Value of f:", f)
#print("Value of g", g)
# Precedence and Associativity (we'll discuss in further classes)

# I want to make a multivalued tuple

h = ("A", "BBB", "CC")
print("Type of h",type(h))

str1 = "Computer"
i = tuple(str1)


j = ["Alpha", "Beta", "Gamma"]
k = tuple(j)
print(k)
print("Type of k",type(k))


