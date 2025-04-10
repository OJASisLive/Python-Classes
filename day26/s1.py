a=float(input("Enter the 1st variable:")) # 5.0
b=float(input("Enter the 2nd variable:")) # 3.0
print("Original value of a =",a) # a = 5.0
print("Original value of b =",b) # b = 3.0

temp=a # temp = 5.0 , a = 5.0, b = 3.0
a=b # temp = 5.0 , a = 3.0 , b = 3.0
b=temp # temp = 5.0 , b = 5.0 , a = 3.0

print("After swapping, a is now",a) # a = 3.0
print("After swapping, b is now",b) # b = 5.0


