# elif or (else-if)
import datetime

time = datetime.datetime.now()
print(time)

a=4

#a=int(input("Enter an integer: "))
if (a>0):
    print ("a is positive")   
elif (a<0):
    print ("a is negative")    
else:
    print("a is Zero")
    
time2 = datetime.datetime.now()
print(time2)

print(time2-time)
