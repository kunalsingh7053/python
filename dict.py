student={
    "name":"kunal",
    "age":21,
    "courses":["maths","science"],
    "is_active":True
}

#accessing elements
print(student["name"])
print(student["age"])
print(student.get("age"))

#modifying elements
student["age"]=22
print(student["age"])

#removing elements
student.pop("age")
del student["courses"]
student.popitem()  # removes the last inserted item
print(student)

#length of dictionary
print(len(student))


car={
    "brand":"Toyota",
    "model":"Camry",
    "year":2020
}
#all keys
print(car.keys())

#all values
print(car.values())

#all items
print(car.items())

#updating dictionary
car.update({"year":2021, "color":"red"})
print(car)
