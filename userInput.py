
name = input("whats your name: ")
print("Hello " + name)

height = float(input("Whats your height: "))
height_inches = "{:.2f}".format(height/2.54)
print(type(height))
print("You are " + str(height) + "cm")
print("You are " + height_inches + " inches tall")
