age = int(input("Enter your age: "))

if age>=18:
    print("You are a major")

    li = input("Do you have a 2w driving licence (y/n): ")

    if li == 'n':
        print("You can apply for one")
        
    elif li == 'y':
        
        li2 = input("Do you have a 4w driving licence (y/n): ")
        
        if li2 == 'n':
            print("You can apply for one")
            
    else:
        print("Wrong input")

else:
    print("You are a minor, you cannot drive vehicles")
        

# if inside another if is called nested if
