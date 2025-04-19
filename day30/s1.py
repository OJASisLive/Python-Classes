import math

m = int(input("Enter a number: ")) #127

while m<2:
    m = int(input("Enter a number: "))

upper_limit = math.sqrt(m) #It is the sq root of input
upper_limit += 1
upper_limit = int(upper_limit)



for i in range(2,upper_limit):
    print(i)
    if m%i == 0:
        print(i)
        print("It is not a prime no")
        break
else:
    print("It is a prime no.")

