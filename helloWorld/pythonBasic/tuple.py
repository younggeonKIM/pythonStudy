t1 = ()
t2 = (1,)
t3 = (1, 2, 3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'), 6, 8)

print(t1)
print(t2)
print(t3)
print(t4)
print(t5)

""" t1[0] = 2       #TypeError
del(t3[1])          #TypeError    """


print(t5[2])
print(t5[1:3])


