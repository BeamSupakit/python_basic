"""
#Part: Python Variables

 ┌─┐　─┐
│▒│ /▒/
│▒│/▒/
│▒ /▒/─┬─┐
│▒│▒▒│▒│
┌┴─┴─┐-┘─┘
│▒┌──┘▒▒▒│ 
└┐▒▒▒▒▒▒┌┘
└┐▒▒▒▒┌┘
＼____/
"""

# This is a commant
print("Hello World 1")#ข้อความ
print("Hello World 2")#ข้อความ

x = 5
y = "Hey Bro"
print(x, y)

x = str(3)
y = int(3)
z = float(3)
print(type(x), type(y), type(z))

"""
#
#Part: Variables Names
#
"""
myvar = "John"#ชื่อตัวแปล
my_var = "John"#ชื่อตัวแปล
_my_var = "John"#ชื่อตัวแปล
myVar = "John"#ชื่อตัวแปล
MYVAR = "John"#ชื่อตัวแปล
myvar2 = "John"#ชื่อตัวแปล
# 2myvar = "John" ชื่อตัวแปลผิด
# my-var = "John" ชื่อตัวแปลผิด
# my var = "John" ชื่อตัวแปลผิด
# a = "John" ไม่ควรตั้ง
# a2 = "John" ไม่ควรตั้ง

# Camel Case
myVarinbleName = "John"
# Pascal Case
MyVarinbleName = "John"
# Snake Case
my_varinble_Name = "John"

"""
Python Data Types
Text Type:
str
Numeric Types:
int, float, complex
Sequence Types:
list, tuple, range
Mapping Type:
dict
Set Types:
set, frozenset
Boolean Type:
bool
Binary Types:
bytes, bytearray, memoryview
None Type:
NoneType
"""

"""
#
#Part: Python String
#
"""

x = "Hey Bro"
print(x)

y = """1 Hey Bro
2 Hey Bro
3 Hey Bro 4 Hey Bro 
5 Hey Bro"""
print(y)

x = "Hey Bro"
print(x[2])
print(len(x))#เอาใว้นับตัวอักษรณ์

#แต่งคำ
print("Hey" in x)
print("What sup" not in x)
print(x.upper())
print(x.lower())
print(x.replace("Bro", "Sis"))#แทนที่ข้อความ
print(x.split(" "))

#ต่อคำ
a = "Apple"
b = "Banana"
print(a + " " + b)

#จัด Formate
price = 20
word = f"price: {price:.2f}"
print(word)