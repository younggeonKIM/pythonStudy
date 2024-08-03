numbers = [1, 2, 3, 4, 5]
print(numbers)
numbers.append(6)
print(numbers)
numbers.insert(0, 10)
print(numbers)
numbers.remove(3)
print(numbers)
numbers.clear()
print(numbers)
i = 1
while i<=4:
    numbers.append(i)
    i+=1
print(4 in numbers)
print(5 in numbers)
print(len(numbers))