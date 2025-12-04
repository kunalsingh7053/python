def greeting(name):
    print(f"Hello, {name}!")
greeting("Alice")    


#types of arrguments

#1. Positional Arguments
def greet(name, message):
    print(f"{message}, {name}!")
    
greet("Alice", "Good morning")
greet("Bob", "Welcome")

#2. Keyword Arguments
def greet(name, message):
    print(f"{message}, {name}!")
greet(message="Good morning", name="Alice")    

#@3. Default Arguments  
def greet(name, message="Hello"):
    print(f"{message}, {name}!")
greet("Alice", "Good morning")    

#4. Variable-length Arguments
#1) Using *args
def greet(*names):
    print("Hello,",names, end=" ")

greet("Alice", "Bob", "Charlie")   
#2) Using **kwargs
def greet(**person):
       print(person)  

greet(name="Alice", city="New York")

#Scope of Variables
#1. Local Scope
def my_function():
    x = 10  # Local variable
    print("Inside function:", x)
my_function()    
#global variable
x = 20  # Global variable
print("Outside function:", x)
def xyz():
    global x
    x = 30  # Modifying the global variable
    print("Inside function:", x)
xyz()


#lambda function
square = lambda x: x * x
print(square(5))  # Output: 25