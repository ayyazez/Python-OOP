#Instance Attributes Encapsulation .
#Encapsulation => Data/Attributes Security / Protection /Hiding.

class Employee:
    
    

    def __init__(self, name,age):
        self.__e_name = None
        self.__age = None
        self.set_name(name)
        self.set_age(age)

    def set_name(self, name):
        for s in name:
            if s.isdigit():
                raise Exception('Digits are not allowed in name.')
            else:
                self.__e_name=name
        
    def get_name(self):
        return self.__e_name
    def set_age(self,age):
        if(age <0):
            raise ValueError('Invalied Age')
        else:
            self.__age = age

    def get_age(self):
        if self.__age >=18:
            return self.__age

    
