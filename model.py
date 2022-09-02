#Instance Attributes Encapsulation .
#Encapsulation => Data/Attributes Security / Protection /Hiding.

class User:

    def __init__(self, name, age):
        self.__e_name = None
        self.__age = None
        self.set_name(name)
        self.emp_age = age

    
    def get_name(self):
        return self.__e_name

    
    def set_name(self, name):
        for s in name:
            if s.isdigit():
                raise Exception('Digits are not allowed in name.')
            else:
                self.__e_name = name

    @property
    def emp_age(self):
        if self.__age >= 18:
            return self.__age


    @emp_age.setter
    def emp_age(self, value):
        if(value < 0):
            raise ValueError('Invalied Age')
        else:
            self.__age = value

    