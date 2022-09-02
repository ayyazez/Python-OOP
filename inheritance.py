class Person:
    
    def simple_method(self):
        print("Base class simple method calling")
        
    def print_f(self):
        print('From base class')
    
class Student(Person):
    
    def simple_method(self):
        pass
        # super().simple_method()  # Extend 
        super().simple_method() #Extend
        print("Derrived class simple method calling") 
class Teacher(Person):

    def print_f(self):
        super().print_f() #extend
        print("From child class")

std_1 = Student()
# std_1.simple_method()
tch1 = Teacher()
tch1.print_f()