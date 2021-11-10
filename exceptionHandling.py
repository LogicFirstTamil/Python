#  Exception Handling

try:
    num = int(input("Enter numerator: "))
    den = int(input("Enter denominator: "))
    result = num/den

except ZeroDivisionError as e:
    print(e)
    print("You cannot divide by zero..")
except ValueError as e:
    print(e)
    print("Enter numbers only..")
except Exception as e:
    print(e)
    print("Some error occurred")
else: # executes only when no error occurs
    print(result)
finally: # always executes
    print("This always executes")

print("Bye")

