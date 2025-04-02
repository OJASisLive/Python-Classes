#WAP to find whether a student is pass or fail, if it requires total 40%
#and at least 33% in each subject to pass
#3 subject marks as input from user

sc = float(input("Enter Science mark:"))

while sc > 100 or sc < 0:
    print("The maximum mark is 100 min is 0")
    sc = float(input("Enter Science mark:"))

ma = float(input("Enter Maths mark:"))

while ma > 100 or ma < 0:
    print("The maximum mark is 100 min is 0")
    ma = float(input("Enter Maths mark:"))
    
en = float(input("Enter English mark:"))

while en > 100 or en < 0:
    print("The maximum mark is 100 min is 0")
    en = float(input("Enter English mark:"))

total = float((sc+ma+en)/300)*100

if sc < 33:
    print ("student failed")  
elif ma < 33:
    print ("student failed")        
elif en < 33:
    print ("student failed")  
elif total < 40:
    print ("Student Failed")
else:
    print ("Passed in all subjects",round(total,2),"%")













    
