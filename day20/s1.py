'''
input 2numbers and store in 2 variables,
ask user for choice,to add sub mul or div.
and execute their choice on two numbers
if choice is div, adn denominator is 0, print that
denominator cannot be zero, do not perform div
this pgm shld never return error
'''

a=int(input("ener the 1st number: "))
b=int(input("ener the 2nd number: "))
print ("1 for Add\n2 for Sub\n3 for mul\n4 for Div")

c=int(input("Enter your choice of operation:" ))

if (c==1): #"enter integer for c or make if as c=="1"
    print("addition is:",a+b)

elif (c==2):
    print("subtraction is:",a-b)

elif (c==3):
    print("multiplication is:",a*b)
    
elif (c==4):
    if b==0:
        print("denominator cannot be zero, enter 2nd number other than 0")
    else:
        print("Division is", a/b)
        
#
