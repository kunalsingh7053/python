#for loop
# n = int(input("Enter a number: "))
n=5
for i in range(n):
    print("Iteration:", i)
 
print(" ")

for i in range(1,n):
    print("Iteration:", i)


#iterate over a list
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)


#iterate over a string
name = "Alice"
for char in name:
    print(char)

#iterate over a tuple
numbers = (1, 2, 3, 4, 5)
for num in numbers:
    print(num)        

#iterate over a dictionary
person = {"name": "John", "age": 30, "city": "New York"}
for key in person:
    print(key, ":", person[key])    

#iterate over a set
colors = {"red", "green", "blue"}
for color in colors:
    print(color)    

#iterate with index
animals = ["cat", "dog", "rabbit"]
for ani in range(len(animals)):
    print(ani, animals[ani])    

 #while loop
count = 1
while count <= 5:
    print("Count:", count)
    count += 1   