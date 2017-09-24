i = 0
x = 1

while i < 1000:
    if i % 3 == 0 or i % 5 == 0:
        x = i + x
        print(x)

    i = 1 + i


print("Total is " + str(x))
