import math
import random
import time


#🔶  Math Module (built-in)
print(math.pi)
print(math.sqrt(16))
print(math.ceil(4.3))
print(math.floor(4.3))
print(math.factorial(5))


#🔶  Random Module (built-in)


print(random.random())
print(random.randint(1, 10))
x = [1, 2, 3, 4, 5]
print(random.choice(x))
print(random.shuffle(x))
print(x)


#🔶  Time Module (built-in)
print(time.time())
print(time.ctime())
time.sleep(2)
print("Awake after 2 seconds")