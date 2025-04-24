def task1(a,b):
    print("THis is from task1")
    print(a+b)


def task2(a,b,c):
    c(a,b)
    print("This is in task2")
    print(a-b)
    print(a*b)
    print(a/b)


task2(6,7,task1)

