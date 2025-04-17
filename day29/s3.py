# A prime no can only be divided by 1 and itself

# 7 is a prime no
# 7%1 = 0, 7%7 = 0
# 7%2 7%3 7%4 7%5 7%6
# 7%8


# naive approach

#m = int(input("Enter a number: "))
#while m <= 1 :
#    print("Not applicable")
#    m = int(input("Enter a number: "))

m = 83

for i in range(2,m):
    if m%i == 0:
        print(i)
        print("It is not a prime no")
        break
else:
    print("It is a prime no.")

print("Control comes here")

    
    
#it 1: i = 2
#it 2: i = 3
#it 3: i = 4
#it 4: i = 5
#it 5: i = 6
#it 6: i = 7

        

'''
if m%2 == 0:
    print("Not a prime no: ")
elif m%3 == 0:
    print("Not a prime no: ")
elif m%4 == 0:
    print("Not a prime no: ")
elif m%5 == 0:
    print("Not a prime no: ")
elif m%6 == 0:
    print("Not a prime no: ")
else:
    print("It is a prime no")
'''













'''
m=float(input("Enter the dividend number:"))

if n>0 or n<0:
    if (m%n)!=0 and (m%1)==0:
        print("m is a prime number")
    else:
        print("m is not a prime number")
else:
    print("The divisor cannot be zero")
'''
