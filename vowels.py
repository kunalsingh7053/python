name = "aeiou"
check = ['a', 'e', 'i', 'o', 'u']
count = 0

for char in name:
    if char in check:
        count +=1 
    else:
        continue
print("Number of vowels in the name:", count)    