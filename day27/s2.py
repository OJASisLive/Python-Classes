while True:
    print("-"*35)
    n=float(input("Enter the value of n: "))
    
    if n>0:
        print("n is positive")
    elif n<0:
        print("n is negative")
    else:
        print("n is zero")

    print("\nDo you want to continue?")
    choice = input("Enter 'y' for yes and 'n' for no: ")
    choice = choice.lower()
    print("-"*35)
    if choice == 'n':
        break
    print("Hii")

   
    
    

    
