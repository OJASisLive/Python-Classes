# String slicing and index concept

# "Computer science"

#  0123456789

sub = "Computer" # Cmue

age = 19

#               -1     -(len+1)    -1
#                0      len()       1
# variable_name[start  :stop:    step] ( the actual stop index+1)
# Whenever it reaches the stop position it will stop printing

#print(sub[0:50:-1]) # 0 3 6 Cpe

#print(sub[-1:-9:-1]) # 8 7 6 5 4 3 2 1 0

print(sub[::])
print(sub[0:8:1])

print(sub[::-1])
print(sub[-1:-9:-1])

