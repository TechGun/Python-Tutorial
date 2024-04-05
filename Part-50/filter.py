students = [
    ("vishwajeet", 92),
    ("ajeet", 97),
    ("raju", 60),
    ("shaym", 72)
]

# new_list = []

# for x in students:
#     if x[1] > 90:
#         new_list.append(x)

new_list = filter(lambda x: x[1] > 90, students)
new_list = list(new_list)
print(new_list)
