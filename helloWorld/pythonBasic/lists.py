names = ["John", "Bob", "Mosh", "Sam", "Mary"]
print(names)
print(names[0])
print(names[-1])
names[0] = "Jon"
print(names)

print(names[0:3])

odd = [1, 3, 5, 7, 9]
print(odd)
print(odd[:2])  #[1, 3]
print(odd[4:])  #[9]


a = [1, 2, 3]
b = [4, 5, 6, 7]
print(a+b)
print(b+a)
print(a * 5)

print(len(a+b))
del(b[3])
print(b)
b.append(6)
print(b)
b.insert(3,7)
print(b)
b = [4, 5, 6, 7]
b.insert(2,9)
print(b)