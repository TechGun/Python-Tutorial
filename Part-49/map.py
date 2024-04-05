students = [
    ("vishwajeet", 92),
    ("ajeet", 97),
    ("raju", 60),
    ("shaym", 72)
]

names = list(map(lambda x: (x[0], x[1]+2), students))


# names = []

# for x in students:
#     names.append(x[0])

print(names)
