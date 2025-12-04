#break
for i in range(10):
    if i == 5:
        break
    print(i)
#continue
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
#pass
for i in range(5):
    pass # Placeholder loop, does nothing
print("Loop completed.")    