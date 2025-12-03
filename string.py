x="kunal"
y="patel"
print(type(x))
print(len(x))
print(x[0])  # Accessing first character
print(x[-1]) # Accessing last character

#concatenation
print(x+y)

#uppercase
print(x.upper())
#lowercase
print(y.lower())

#title case
print(x.title())

#remvoving whitespace
z="   hello world   "
print(z.strip())  # removes leading and trailing whitespace

a="hello world"
print(a.replace("world", "there"))  # replacing substrings in a string

#splitting string
b="apple,banana,cherry"
fruits=b.split(",")
print(fruits)

#list to string
fruit_string = ", ".join(fruits)
print(fruit_string)