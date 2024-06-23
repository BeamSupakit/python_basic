"""
#
# Part: Python Conditions
#
"""

a = 200
b = 500
if a > b:
    print("a > b is True.")
elif a < b:
    print("a < b is True.1")
    print("a < b is True.1.1")
    print("a < b is True.1.2")
elif a <= b:
    print("a < b is True.2")
elif a == b:
    print("a < b is True.3")
else:
    print("Nothing.")#แบบยาว

if a < b: print("a < b is True.")#แบบย่อ ถูก

print("B") if a < b else print("A")#แบบย่อ ถูกและผิด

a = 200
b = 30
c = 500
if a > b and c > a:
    print("Both is True.")
if a > b or a > c:
    print("some cond is true.")
if not a > b:
     print("Not")
if b > a:
    print("pass")
    pass

x = 19
if x > 10:
    print("Let's go!")
    if x > 20:
        print("x > 20 is Ture.")
        if x > 20:
            print("x > 20 is Ture.1")
            if x > 20:
                print("x > 20 is Ture.2")
    else:
        print("x > 20 is false.")