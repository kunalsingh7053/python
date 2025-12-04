x = [1,2,"hello",5.5, True]
y = [10,20,30]
#  List concatenation
c = x + y
print(c)
print(x[2])
#  Last element negative indexing
print(x[-1])

#modifying list
x[1] = "world"
print(x)

#add element to list
x.append("new element")
x.insert(1, "inserted element at index 1")
print(x)


#remove element from list
x.remove(5.5)
print(x)
# remove last element and return it
x.pop()
print(x)
#remove by index
x.pop(2)
print(x)

#length of list
print(len(x))

#max and min
num_list = [10, 5, 30, 2, 50]
print(max(num_list))  # 50
print(min(num_list))  # 20

#sorting list
y = [30, 10, 50, 20, 40]
y.sort()
print(y)

#reverse list
y.reverse()
print(y)

# remove all elements
x.clear()
print(x)