class Uni_Person:
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def make_attendence(self):
        print("Attendence marked as present...")

    def leave_application(self):
        print("leave application submitted")


class Teacher(Uni_Person):

    def __init__(self, n, a, s):
        super().__init__(n, a)
        self.salary = s

    def upload_test(self):
        print("test uploaded")

    def leave_application(self):
        super().leave_application()
        print("wating for approval")


class Student(Uni_Person):

    def upload_answer(self):
        print("answer uploaded")


class clerk(Uni_Person):

    def upload_data(self):
        print("data uploaded")


teacher1 = Teacher("vishwajeet", 24, 30000)

teacher1.leave_application()

student1 = Student("ajit", 18)
student1.leave_application()
