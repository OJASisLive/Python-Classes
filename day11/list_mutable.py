'''
alist = ["Om", "Ishanth", "Punya", (1,2,3), ['a','b','c'], 12, 5.5 ]
print(alist)

alist.append("Vino")
print(alist)

alist[1] = "Anuj"
print(alist)

alist.pop(0)
print(alist)

alist.pop()
print(alist)
'''
# List are mutable












atuple = ("Om", "Ishanth", "Punya", (1,2,3), ['a','b','c'], 12, 5.5)
print(type(atuple))

atuple = list(atuple)

print(type(atuple))

# Immutability
# tuples are immutable
