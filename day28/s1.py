# For loops
# A for loop is used to repeat a task for specific no. of times

#for i in range(0,10):
#    print(i)

print("Using while loop")


i = 0
while i<10:
    print(i)
    i += 1
    
'''
name = None
while name == None:
    print("You have not given a name")
    name = eval(input("Enter Name: "))
'''    

print("Using for loop")


#for i in range(0,10):
#    print(i)





x = [24, 56, 74, 35, 91, 34]


n=0
while n<5:
    print(x[n])
    n+=1

z = 0
while z < len(x):
    print(x[z])
    z = z+1

for z in range(0,len(x)):
    print(x[z])

for z in x: # For each loop
    print(z)

    

print(x[0])
print(x[1])
print(x[2])
print(x[3])
print(x[4])

print("\n","-"*40)





print(x[0:5])


for i in x:
    print(i)














'''
while True:
    print("Hi")
    print("Om")
    break
    # This will be ignored
    print('Example will be ignored')

print("I am outside the loop")
'''
