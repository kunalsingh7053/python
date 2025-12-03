my_tuple = (10, 20, 30,30)

print(my_tuple.count(30))  # Counting occurrences of element 20
print(my_tuple.index(20))  # Finding index of element 20
print(my_tuple[0])  # Accessing first element
print(my_tuple[-1]) # Accessing last element

#covert to list
my_list = list(my_tuple)
print(my_list)

#length of tuple
print(len(my_tuple))

#max and min
num_tuple = (10, 5, 30, 2, 50)
print(max(num_tuple))  # 50
print(min(num_tuple))  # 2

#tuple concatenation
t1 = (1, 2, 3)
t2 = (4, 5, 6)
t3 = t1 + t2
print(t3)

#tuple repetition
t4 = t1 * 3
print(t4)


