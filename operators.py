# arithmetic operators
a = 2
b = 3

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
print(a//b)

# comparison operators
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

# logical operators
x = True
y = False
print(x and y)
print(x or y)
print(not x)
print(not y)
# bitwise operators
p = 5  # 0b0101
q = 3  # 0b0011
print(p & q)  # bitwise AND
print(p | q)  # bitwise OR
print(p ^ q)  # bitwise XOR
print(~p)     # bitwise NOT
print(p << 1) # left shift
print(p >> 1) # right shift
# assignment operators
c = 10
c += 5
print(c)
c -= 3
print(c)
c *= 2
print(c)
c /= 4
print(c)
c %= 3
print(c)
c **= 2
print(c)
c //= 2
print(c)
# membership operators
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)
print(6 not in my_list)
print(1 in my_list)
# identity operators    
m = [1, 2, 3]
n = m
print(m is n)
o = [1, 2, 3]
print(m is o)
print(m is not o)
print(m is not n)

# ternary operator
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)
