class Teacher:
    
    

    def __init__(self, name,age):
        self.__e_name = None
        self.__age = None
        self.set_name(name)
        self.teach_age = age

    def set_name(self, name):
        for s in name:
            if s.isdigit():
                raise Exception('Digits are not allowed in name.')
            else:
                self.__e_name=name
        
    def get_name(self):
        return self.__e_name

    def __get_age(self):
        if self.__age >=18:
            return self.__age


    def __set_age(self,value):
        if(value <0):
            raise ValueError('Invalied Age')
        else:
            self.__age = value

    teach_age = property(__get_age, __set_age)
    

    
