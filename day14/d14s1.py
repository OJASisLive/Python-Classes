# Any immutable datatype can be used as a key
# tuple, int, string, bool, float, None

#di = {1:"Apple", 2:"Mango", 2:"Jack"}

#print(di[2])

dj = {True:"Mango", 1:"Apple", 2:"Jack"}
#                  1: Mango

print(dj[1])

print(dj)










# KEY               VAL
#  True            Mango
#  1               Apple (Latest val will be selected)


# In case of duplicacy
# Oldest key is preserved/selected
# Newest Value will be selected

# True:"Apple"





















