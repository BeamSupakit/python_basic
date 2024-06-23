"""
#
# Part : python Try Except
#
"""
# The "try" block lets you test a block of code for errors.
# The " Except" block lets you handle the error.
# The "else" block lets you execute code when there is no error.
# The "finally" block lets you execute code, regardlessof the result f the try- and except blocks.

try:
    print(x)
    # do something...
except NameError as e:
    print("Not defined! : ", e)
except:
    print("Something else went wrong!")

try:
    print("Hello Wold")
except: 
    print("Something else went wrong!")
else:
    print("Nothing went wrong!")

try:
    print("x")
except: 
    print("Something else went wrong!")
else:
    print("Finished!")

# x = -1
# if x <0:
# resise Exception("Sorry, no numbers below zero.")

x = "Hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed.")