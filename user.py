## public - can be accessed by any class
## private - cannot be accessed outside the class
## protected - can be accessed by inherited classes

class User:
    users = 0  # class variable

    def __init__(self, user_name, pwd):
        self._user_name = user_name  # instance variable
        self.__pwd = pwd ## Dunder
        User.users += 1

    def register(self):
        print("Registering " )
    def login(self):
        print("Logging in ")
        return self
    def greet(self):
        print(" Hello user....")


class Student(User):  # Student class inherits User Class
    # User - parent class, base class, super class
    # Student - child class, derived class, sub class
    def __init__(self,username, pwd, course, fee):
        # use super to access parent class methods
        super().__init__(username,pwd)
        self.course = course
        self.fee = fee
    def greet(self): #override
        super().greet()
        print("Hi " + self.user_name)


class Faculty(User):  # Faculty class inherits User Class
    def greet(self):
        print("Hello Teacher..")


class TempFaculty(Faculty):
    pass
    # def greet(self):
    #     # TempFaculty inherits Faculty which inherits User
    #     # Multi Level Inheritance
    #     print("Hello.. Nice to have you here..")


#Multiple Inheritance
class StudentFaculty(Student, Faculty):
    def greet(self):
        super().greet()
        print("Hello Student Faculty...")

