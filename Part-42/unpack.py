names = ["vishwajeet", "ajit", "techgun", 1, 2, 3, "india", "youtube"]

# first = names[0]
# second = names[1]
# third = names[2]

# print(first)
# print(second)
# print(third)

first, second, third, *list2, fourth, fifth = names

print(first)
print(second)
print(third)
print(list2)
print(fourth)
