students = [
    ("vishwajeet", 92),
    ("ajeet", 97),
    ("raju", 60),
    ("shaym", 72)
]


# def sort_students(stu):
#     return stu[1]


# students.sort(key=sort_students)

# students.sort(key=lambda parameter:statement)
students.sort(key=lambda stu: stu[1])
print(students)
