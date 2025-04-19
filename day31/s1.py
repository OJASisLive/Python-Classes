a = 10
#Global variable: once declared, it can be accessed in any part of my program
#It is declared outside of any block

def fun():
    x = 10
    print("Hello")
    print("How was your exam?")
    print(x)
    y = x+5
    print(y)
    #Local variable:
    # It is a varible declared inside a function
    # And it is only accessible inside that function
    # It's scope is only limited to the function in which it was declared

fun()
print("Outside the function")
print(y)
