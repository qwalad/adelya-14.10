a = 87
c = a + b
print(c)
numbers = [i for i in range(a)]
for j in range(len(numbers)):
    if numbers[j] % 2 == 0:
        del numbers[j]

