"""
#
# Part: Python Collections
# List, Tuple, Set and Dictionary
#
"""

"""
#
# Part: Python List เก็บได้หลายค่าซ้ำกันได้
#
"""
this_list = ["apple", "banana", "coconut", "apple", "banana"]
print(this_list)
print(type(this_list))#เช็คclass
print(len(this_list))#เช็คจำนวน
print(this_list[1])#แสดงตำแหน่งที่เราอยากแสดง01234
this_list.append("cherry")#เพิ่มสิ่งของลงตัวแปล
print(this_list, len(this_list))
this_list.insert(1, "orange")#เพิ่มสิ่งของลงตัวแปลที่ตำแหน่ง1
print(this_list, len(this_list))

this_list2 = ["apple", "banana", "coconut", "apple", "banana"]
this_list3 = ["mango", "pineapple", "grape"]
this_list2.extend(this_list3)#เอาตัวแปล2ตัวมาใว้ด้วยกัน
print(this_list2, len(this_list2))

this_list4 = ["apple", "banana", "coconut", "apple", "banana"]
this_list4.remove("banana")#ลบตัวแปล
print(this_list4, len(this_list4))
#แก้
this_list4 = ["apple", "banana", "coconut", "apple", "banana"]
while "banana" in this_list4:
    this_list4.remove("banana")
print(this_list4, len(this_list4))

this_list5 = ["apple", "banana", "coconut", "apple", "banana"]
this_list5.pop(0)#ลบตำแหน่งที่เลือก
print(this_list5, len(this_list5))

this_list6 = ["apple", "banana", "coconut", "apple", "banana"]
del this_list6[1]#ลบตำแหน่งที่เลือก
print(this_list6, len(this_list6))

this_list6.clear()#ลบทั้งหมด
print(this_list6, len(this_list6))

del this_list5#ตัวแปลไม่เหลือแล้ว
#print(this_list5, len(this_list5))

this_list7 = ["orange", "mango", "kiwi", "pineapple", "banana"]
this_list7.sort()#เลียงตามตัวอักษร
print(this_list7, len(this_list7))

this_list8 = ["orange", "mango", "kiwi", "pineapple", "banana"]
this_list8.reverse()#เลียงจากหลังมาหน้า
print(this_list8, len(this_list8))

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2 #เอามาต่อกันได้
print(list3)

"""
#
# Part: Python Tuple เก็บได้หลายค่า เลียงลำดับให้ ไม่สามารถเปลี่ยนแปลงค่าได้
# 
"""
this_tuple = ("apple", "banana", "coconut")
print(this_tuple)
print(type(this_tuple))
print(len(this_tuple))
print(this_tuple[2])

this_tuple2 = ("apple", "banana", "coconut")
this_tuple3_list = list(this_tuple2)#แปลงtupleให้กลายเป็นlist
print(this_tuple3_list)
print(type(this_tuple3_list))
this_tuple4 = tuple(this_tuple3_list)#แปลงกับให้เหมือนเดิม
print(this_tuple4)
print(type(this_tuple4))

this_tuple5 = ("apple", "banana", "coconut")
this_tuple6_list = list(this_tuple5)
this_tuple6_list.append("mango")#เพิ่มจำนวนหลังจากแปลงเป็นlist
this_tuple7 = tuple(this_tuple6_list)
print(this_tuple7)
print(type(this_tuple7))

this_tuple8 = ("apple", "banana", "coconut")
this_tuple9_list = list(this_tuple8)
this_tuple9_list.remove("banana")#ลบจำนวนหลังจากแปลงเป็นlist
this_tuple10 = tuple(this_tuple9_list)
print(this_tuple10)
print(type(this_tuple10))

del this_tuple10#เคลียไม่ได้แต่ลบได้
# print(this_tuple10)

tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2 #เอามาต่อกันได้
print(tuple3)

"""
#
# Part: Python Set เก็บได้หลายค่าซ้ำกันได้ ทำindexไม่ได้ เก็บค่าไม่ซ้ำกันดองใว้ ไม่เลี่ยงลำดับให้ แก้ไขไม่ได้
#
"""
this_set = {"apple", "banana", "coconut"}
print(this_set)
print(type(this_set))
print(len(this_set))

for x in this_set:
    print(x)

print("banana" in this_set)

this_set2 = {"apple", "banana", "coconut"}
this_set2.add("orange")#เพิ่มได้
print(this_set2, len(this_set2))
this_set2.remove("apple")#ลบได้
print(this_set2, len(this_set2))

this_set3 = {"apple", "banana", "coconut"}
this_set4 = {"pineapple", "grape"}
this_set3.update(this_set4)#ต่อกันได้
print(this_set3, len(this_set3))

#union (Euler)
this_set5 = {"apple", "banana", "coconut"}
this_set6 = {"pineapple", "grape"}
this_set7 = {1, 2, 3,}
this_set8 = this_set5 | this_set6 | this_set7#ต่อกัน
print(this_set8, len(this_set8))

this_set8.clear()#เคลี่ยได้
print(this_set8, len(this_set8))
del this_set8#ลบได้
# print(this_set8, len(this_set8))

"""
#
# Part: Python Dictionary เก็บค่าซ้ำไม่ได้ ตั้งชื่อindexได้ เลี่ยงลำดับได้ 
#
"""
this_dict = {
    "brand": "Ford",
    "model": "Rapter",
    "year": "2023"
}
print(this_dict)
print(type(this_dict))
print(len(this_dict))
print(this_dict["brand"])#เข้าถึงข้อมูล
print(this_dict.get("year"))#เข้าถึงข้อมูล
print(this_dict.keys())#เข้าถึงข้อมูล

this_dict["year"] = 2020 #แก้ไขข้อมูล
print(this_dict)
this_dict.update({"year": 2021})#แก้ไขข้อมูล
print(this_dict)

this_dict["color"] = "red"#เพิ่มindexหรือkeys
print(this_dict)

del this_dict["year"]#ลบ
print(this_dict)

this_dict.clear()#เคลียทั้งหมด
print(this_dict, len(this_dict))
del this_dict
# print(this_dict)

this_dict2 = {
    "brand": "Ford",
    "model": "Rapter",
    "year": "2023"
}

this_dict3 = {
    "brand": "Honda",
    "model": "Civit",
    "year": "2019"
}

this_dict4 = {
    "brand": "Toyota",
    "model": "Colora",
    "year": "2017"
}

mycar= {
    "car1": this_dict2,
    "car2": this_dict3,
    "car3": this_dict4,
}#เอารถมาใส่ใว้ตัวแปลเดียวคือmycar
print(mycar,len(mycar))
print(mycar["car2"]["model"])