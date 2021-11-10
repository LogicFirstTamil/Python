# Recursion - a function calling itself

def fact(num):
    if num==0:
        return 1
    return num*fact(num-1)

print(fact(4))
