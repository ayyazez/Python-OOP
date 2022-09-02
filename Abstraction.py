from abc import   abstractmethod,ABC
class Professor(ABC):

    def __init__(self,name):
        self.__name =None
        self.name = name

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value

    #Instance method / member
    def method_1(self):
        print("Instance Method -1")

    #class method / member
    @classmethod
    def method_2(self):
        print("Class Method -2")

    #Static method / member
    @staticmethod
    def method_3():
        print('Static Method -3')

    #Abstract Method / member
    @abstractmethod
    def method_4(self):
        pass


    # -------------------------...........................................-------------------------
class Administrator(Professor):

    def __init__(self):
        # self.__name = None
        # self.name = name
        print('Admin constr...')

        # @abstractmethod    #Abstract property
        @property
        def abs_prop(self, name):
            pass
        # @property
        # def name(self):
        #     return self.__name

        # @name.setter
        # def name(self, value):
        #     self.__name = value
        
    def method_4(self):
        
        print("Abstract member implementation")
            # print(self.name)


