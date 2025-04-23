'''
#Your code
x = [2,33,44,55]

for i in x:
    c = i-1
    print(c)
    '''

'''
#Method 1

x = [2,33,44,55]
y = []

for i in x:
    c = i-1
    y.append(c)
    #print(c)

print(y)
'''

#Method 2

x = [2,33,44,55]

for i in range(len(x)): # 0,1,2,3
    #x[i] -= 1
    
    #x[i] = x[i] - 1
    
    #print("Iteration",i+1)

print(x)

    
#1st iteration: i = 0
    # c = x[0] - 1
    #   =  2   - 1  = 1
    #x[0] = 1

#2nd iteration:
    #c = x[1] - 1
    # c = 32
    #x[1] = 32

#3rd it: i =2
    # c = x[2] -1 =44-1 =43
    # x[2] = 43

#4th it:
    # c = x[3] - 1 = 55-1 = 54
    # x[3] = 54
    










#print(x)
