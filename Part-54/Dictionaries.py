dic1 = {"x": 20, "y": 10}

student = {
    "name": "vishwajeet",
    "reg no": 22303938,
    "course": "M.Tech"
}

dic2 = dict(name="vishwajeet", branch="AI")

# print(dic2)
student["name"] = "ajit"
student["contact no"] = 987654345

if "sfs" in student:
    print(student["fgdf"])

print(student.get("mobile", 100000))

del student["name"]
print(student)
