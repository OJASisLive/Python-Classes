a = 10 #Global
b = 15


def fun():#local
    global a
    a = a+5
    print("Value of a inside the function:",a)


fun()

print("Value of a outside the function:",a)











'''
table_num = int(input("Enter a number to print table"))
table_limit = int(input("Enter the limit: "))
#Formal parameters
def table(n):
    for i in range(1,x):
        print(n, "x", i, "=", n*i)

#calling function table
table(table_num)
#Actual parameter
'''
