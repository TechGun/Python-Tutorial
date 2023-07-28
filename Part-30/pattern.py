# *
# * *
# * * *
# * * * *
# * * * * *

# for x in range(1, 6):
#     for y in range(1, x+1):
#         print("*", end="")
#     print("")

line = 1

while line <= 5:
    star = 1
    while star <= line:
        print("*", end="")
        star = star + 1
    print("")
    line = line+1
