class Student:
    
    def __init__(self, age, location):
        # self.__name = None
        # self.__age = None
        self.age = age
        self.location = location
        

    @property
    def age(self):
        print("Inside")
        return self._age
    
    @age.setter
    def age(self,value):

        self._age = value


# std1 = Student( 23 , 'LHR')
# print(std1.age)



        
    


class Courses:
    def __init__(self, name):
        self.name = name
        location = Student() #Assocaition -Composition



c = Courses('ML')
print(c.location)