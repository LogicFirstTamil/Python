from user import *
import guessTheNum
from abstractDemo import Car,Bike,Vehicle
guessTheNum.guess_the_num_game()
# user1 = User("Kavitha", "abc123")
# user2 = User("Mahesh", "abcd123")
# user3 = User("Meena", "zyx123")
#
# user1.register()
# user2.login()
# print(user1.user_name)
# print(user2.user_name)
# print(User.users)

# User.users = 100
# print(User.users)
#
# stud1 = Student()
# stud1.greet()
#
# fac1 = Faculty()
# fac1.greet()
#
# tempfact1 = TempFaculty()
# tempfact1.greet()


# user1 = User("xyz",'abc')
# user1.login().greet().


# stud1.login()
# fac1.register()

# sf1 = StudentFaculty()
# sf1.greet_faculty()

# stud1 = Student("Ravi","2387","CS",78000)
# stud1.greet()
# sf1 = StudentFaculty("Radha","abcd","CS",78000)
# sf1.greet()

# car1 = Car()
# car1.start()
#
# bike1 = Bike()

num  = 10
list1 = [7,8,9]

def set_color(obj,color):
    obj.color = color
    obj.start()
    #duck typing - importance to methods than the objects
    #“If it looks like a duck and quacks like a duck, it’s a duck”

car1 = Car()
bike1 = Bike()

set_color(car1,'blue')
set_color(bike1,'black')

print(car1.color)
print(bike1.color)




















