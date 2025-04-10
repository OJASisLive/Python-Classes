import random

x = 0
count = 0

while x < 20 :
    n = random.randrange(1, 21, 3)
    
    if n == 19:
        count = count+1

    x = x+1
   
print(count)


'''
1 => x =0 n = 17  x = 1

2nd ->  x = 1 n = 19 count = 1     x = 1

3rd ->  x = 1 n = 18 x = 2
'''
