import data
from Attributes_Ensacpsulation import Employee
from model import User
from Abstraction import Professor
from Encap_cstom_method import Teacher
from Abstraction import Administrator

if __name__== '__main__':
    # std1 = data.Enroll('Farhan')
    # std1.add_course('AI')
    # std2 = data.Enroll('Noor')
    # std2.add_course('ML')

    # print()
    # print(std1.print_course())
    # print()
    # print(std2.print_course())

    try:
        # name = input("Enter your name: ") 
        # age = int(input("Enter your age:"))
        # empl1 = Employee(name,age)
        # em2 = User(name, age)
        # teach = Teacher(name, age)
        pass
        # pro = Professor('Kamran')
        # admin = Administrator()  #can't create abstract class object
    except (AttrbuteError,IndexError, ValueError) as err:
        print(err)
    else:
        # eage = teach.teach_age
        # print(eage)
        # name = en.name
        # pro.method_1()
        # pro.method_2()
        # pro.method_3()
        # pro.method_4()
        # Professor.method_4()
        # print(pro.method_2())
        # print(en.method_3())
        # print(en.method_4())
        print('........')
        admin = Administrator()
        admin.method_4()
        
 

    finally:
        pass

    
    