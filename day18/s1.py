a = [45, 79, 52]

b = a # Default : Shallow ,  b = address of a

b = list(a) # Deep,  b = [45, 79, 52]

a.append(100)

print(a)
print(b)


x = {'Rollno':[1,2,3],'Name':['A','b','c']}
y = x # Default: Shallow
y = dict(x) # Deep 

x['Marks'] = [100,80,90]

print(x)
print(y)
