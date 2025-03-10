# If a certain condition is true, only then the code will be executed
import datetime

time = datetime.datetime.now()
print(time)

a=int(input("Enter an integer: "))

if (a%2==0):
    print ("a is even")
    time = datetime.datetime.now()
    print(time)
    
else:
    print ("a is odd")
    time = datetime.datetime.now()
    print(time)


