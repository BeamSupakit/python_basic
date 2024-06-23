"""
#
# Part : Python Function
#
"""

def my_function():
    print("Hello World1")
    print("Hello World2")

my_function()
my_function()

# parameter
# 1ฟังก์ชั่น มีแค่ 1 เท่านั้น
def my_name(fname):
    print("my name is", fname)
my_name("Anya")

def my_name2(fname, lname):
    print("my name is", fname, lname)

my_name2("Anya","Roger")
my_name2(lname = "Roger", fname = "Anya")

def my_name3 (lname):
    print("My last name is", lname)

my_name3("Paul")

def my_friuts(fruits):
    for fruit in fruits:
        print(fruit)

friuts = ["Apple", "Banana", "Coconut"]
my_friuts(friuts)

def red_potion(hp):
    return hp + 50 
print(" HP: ",red_potion(100))
print(" HP: ",red_potion(70))
