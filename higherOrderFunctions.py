# # higher order functions
# #  - takes function as parameter or returns a function
#
# def calm_down():
#     print("Calm down.")
#
# def happy():
#     print("Jumping....")
#
# def sad():
#     print("Crying....")
#
# def feeling(func):  #func = happy  func = sad
#     func()
#     return calm_down
#
# func = feeling(happy)
# func()
# func2 = feeling(sad)
# func2()
# print(happy)
#
# joy = happy
# joy()
#
# sorrow = sad
# sorrow()
#
# lambda

def add_ten(num):
    return num+10

add_10 = lambda x:x+10  #  lambda par1,par2..parn: return exprn
product = lambda a, b, c: a*b*c
tall_enough = lambda h: h > 180
strong_enough = lambda w:  "yes" if w > 55 else "no"

print(strong_enough(73))

