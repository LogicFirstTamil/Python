
#Loop - repeats a set of code - while,for

letter = ' '
while not letter.isalpha():
    letter = input("Enter an alphabet: ")

print("You have entered " + letter)

#print 1 to 100

num = 1
while num <= 100:  # 1 2 3 4 ...... 100
    print(num)
    num += 1   # num = num + 1

print("Bye")

for i in range(1, 100+1):
    print(i)
else:
    print("over")

#pattern printing
list = [6, 7, 4, 1, 9]

for i in list:
    print(i*i)

for i in range(1, 7): #rows
    for j in range(1, 11): #cols
        print('&', end='')
    print('')

#walrus operator :=

print(name := "Varun")

# break - breaks the execution of current block
# Get a list of numbers from the user and add to a list


# print("Enter list of numbers. Enter z to exit. ")
# list_num = []
# while True:
#     inp = input()
#     if inp == 'z':
#         break
#     list_num.append(int(inp))
# else:
#     print("done")
# print(list_num)

print("Enter list of numbers. Enter z to exit. ")
list_num = list()
while (inp := input()) != 'z':
    list_num.append(int(inp))
print(list_num)


# continue - continues to the next Iteration
# Remove , from a string

str_in = "A,B,V,C,E,R"
str2 =''

for i in str_in:
    if i == ',':
        continue
    str2 = str2 + i  # AB

print(str2)


# pass - do nothing
str_in = "A,B,V,C,E,R"
str2 = ''

for i in str_in:
    if i == ',':
        pass
    else:
        str2 = str2 + i  # AB
print(str2)




    
























