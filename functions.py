# functions - performs well defined
# i/p to function - arguments or parameters
# output of the function - return

def greet(fname, lname=''):  # name - parameter
    """ takes a string name as input. Says hello + name - docstring """
    print("hello " + fname + " " + lname)
    print("how are you?")


n = "Ram"
greet("Latha")
greet(fname="Ram", lname="Kumar")  # passing arguments
print("********")
name = "Ganesh"
greet(lname="Logic", fname="First")


# sum of first n natural numbers

def sum(num):
    """ Finds the sum of first num natural numbers """
    return num * (num + 1) / 2


result = sum(11)
print(result)
print(sum(20))

# Variable Scope
num = 10  # Global variable


def welcome(name):  # name - local variable
    num = 20
    print("Welcome " + name)
    print(str(num))


welcome("Radha")
print("The val of num is " + str(num))
while num <= 100:
    print(num)
    num += 10


# Sum of numbers
def total(*arg):  # *arg - packs all arguments into a tuple
    sum = 0
    for i in arg:
        sum = sum + i
    return sum


print(total(4, 5, 9, 10, 4, 3))


# kwargs

def print_addr(**kwargs):  # packs all keyword arguments into a dictionary
    for key, val in kwargs.items():
        print(val)


print_addr(door_no="93", street_name="RR Nagar", addr_line2="Adyar", city="Chennai")



#Passing List
def print_list(list):  #list = names
    for i in range(0,len(list)):
        list[i] = list[i].title()
        print(list[i])

names = ["Priya","Venu","nisha","kavitha"]
print_list(names[:])
print(names)

#Returning Dictionaries

def get_user_info():
    ''' Returns name and age in dictionary '''
    user = {'name': 'vishnu', 'age': 42}
    return user


user = get_user_info()
print(user)




