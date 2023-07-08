# Logical AND: True if both the operands are true x and y
# Logical OR: True if either of the operands is true  x or y
# Logical NOT: True if operand is false   not x

ssc = 50
hsc = 65


if ssc >= 60 and hsc >= 60:
    print("Eligible")
else:
    print("Not Eligible")

if ssc >= 60 or hsc >= 60:
    print("Eligible")
else:
    print("Not Eligible")

criminal = False

if not criminal:
    print("Eligible")
else:
    print("Not Eligible")
