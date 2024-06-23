"""
#
# Part: python class and object
#
"""

# Make a class

class MyClass:
    x = 5

# call a class
object1 = MyClass()
print("1:" , object1.x)
object2 = MyClass()
print("2:" , object2.x)

class Person:
    def __init__(self, name_p, age_p):
        self.name = name_p
        self.age = age_p

    def __str__(self) :
        return  f"{self.name}-{self.age}"

    def sayHi(self, lastname):
        print("Hey Yo What' sup" + "" +  self.name)

p1 = Person("John", 20)
print(p1.name, p1.age)
print(p1)
print(p1.sayHi("Son"))

p2 = Person("Joe", 30)
print(p2.name, p2.age)
print(p2)
print(p2.sayHi("Nathan"))

class Car:
    def __init__(self, body_color, engine_size):
        self.wheels = 4
        self.window = 4
        self.window_front = 1
        self.window_back = 1
        self.body_color = body_color
        self.engine_size = engine_size

    def push_window_button(self):
        # do some thing
        pass

    def pop_window_button(self):
        # do some thing
        pass

    def calSpeed(self):
        speed = self.engine_size * 1000

    def turn_on_front_light(self, status):
        if status == "on":
            # do some thing
            pass
        else:
             # do some thing
            pass