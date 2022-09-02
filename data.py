class Enroll:
    courses =[]
    def __init__(self,name):
        self.name = name
        self.courses = []
    def add_course(self ,sbj_name):
        self.courses.append(sbj_name)
    def print_course(self):
        print(f"Name: {self.name} | Courses: {self.courses}" )

