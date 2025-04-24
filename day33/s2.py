#*args and **kwargs

def add(*om):
    x = 0
    addition = 0 #199
    while x<len(om):#7
        addition += om[x] 
        x=x+1

    print("The sum is",addition)

#add(3,4,5,21,45,67,54)
#add(2,3)
#add(7,65,45)
#add()
#add(3)



















def add_for(*om):#om = (3,4,5,21,45,67,54)
    addition = 0
    for i in om:
        addition = addition + i

    print("The sum is",addition)


while True:
    x = int(input("Enter the number: "))



add_for(x)


    
    

    













