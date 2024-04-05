students = [
    ("vishwajeet", 92),
    ("ajeet", 97),
    ("raju", 60),
    ("shaym", 72)
]

# map function
names = list(map(lambda x: x[0], students))

# new_names = [statement for x in list]
new_names = [x[0] for x in students]

print(new_names)

# filter function
new_list = list(filter(lambda x: x[1] > 90, students))

# list1 = [statement for x in list condition]
list1 = [x for x in students if x[1] > 90]

print(list1)
