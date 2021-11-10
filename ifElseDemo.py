
pwd_correct = False

if pwd_correct:  #conditional stmt
    print("Logged In")
    print("Have a Nice Day")
else:
    print("Incorrect Pwd")
    print("Try Again")

num = 35

if num % 10 == 0:
    print(str(num) + " is a multiple of 10")
else:
    print(str(num) + " is not a multiple of 10")

#elif ladder

ind_score = 360

if ind_score >= 350:
    print("India will win")
elif ind_score >= 250:
    print("India might win")
elif ind_score >= 150:
    print("Aus might win")
else:
    print("Aus will win")

#nested if
#check if the given num is a three digit even number
#logical operators - and or not
num = int(input("Enter a num: "))

if num > 99 and num < 1000 and num%2 == 0:
    print(str(num) + " is a three digit even number")
else:
    print(str(num) + " is a not three digit even number")


name = "Satya"
if name[0] == 'S' or name[0] == 's':
    print("the name starts with s")










































