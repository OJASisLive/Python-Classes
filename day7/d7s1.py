a = "Om_is_a#Good#boy" #0 2 4 6 8 10
                        # 12 14 16 18
print(len(a))
print(a[::])

#  0    20    1
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
# 17 18 19 

#print(a.find("  "))

#print(a[a.find("  ")::])

#print(a[a.find("  ")::].lstrip())

print(a[:a.find("  "):])

#   start, stop, step

#     0  ,len(a), 1

print(a.split()) # " "
# "Om_is_a_Good_boy"

#"Om is a Good boy"
# ["Om", "is", "a", "Good", "boy"]


