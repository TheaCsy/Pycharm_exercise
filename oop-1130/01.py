########

class PythonStudent():
    name = None
    age = 18
    course = "Python"

    def Homework(self):
        print("I am working")
        return None

xiaohong = PythonStudent()
print(xiaohong.name)
print(xiaohong.age)
xiaohong.Homework()
print(xiaohong.course)

print(PythonStudent.__dict__)
