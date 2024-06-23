"""
#
# Part: Python Operators
# Arithmetic Operators
#
"""
x = 4 + 5
print(x)

x = 4
y = 5
z = x + y + 1
print(z)

z = x / y
v = x % y
print(z , v) 

z = x + y
v = x - y
print(z , v) 

"""
#
# Part: Python Operators
# Assignment Operators
#
"""
a = 1
a += 5
print(a)
# a = a + 5

"""
#
# Part: Python Operators
# Comparison Operators
#
"""
a = 10
b = 15
print(a == b)#False
print(a != b)#True
print(a > b)#False
print(a < b)#rue
print(a >= b)#False
print(a <= b)#True

a = 15
b = 15
print(a == b)#True
print(a != b)#False
print(a > b)#False
print(a < b)#False
print(a >= b)#True
print(a <= b)#True

"""
#
# Part: Python Operators
# Logical Operators
#
"""
a = 10
b = 15

print( (a < 5) and (b < 20) )#False
print( (a == 10) or (a <= 9) )#True
print( not (a == 10) or (a <= 9) )#False

print( (a < 5) & (b < 20) )#False
print( (a == 10) | (a <= 9) )#True
print( not (a == 10) | (a <= 9) )#False