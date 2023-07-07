print("Legal age of marriage in India")

gender = input("Enter Male (m) or Female (f): ")
age = int(input("Enter age: "))

if gender == "m":
    if age >= 21:
        print("Legal age of marriage")
    else:
        print("Child Marriage")

elif gender == "f":
    if age >= 18:
        print("Legal age of marriage")
    else:
        print("Child Marriage")

else:
    print("Enter m for male and f for female")
