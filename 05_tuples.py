### Tuples ###

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (15, 1.78, "Jorge", "Martínez", "Jorge")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[4]) IndexError
# print(my_tuple[-6]) IndexError

print(my_tuple.count("Jorge"))
print(my_tuple.index("Martínez"))
print(my_tuple.index("Jorge"))

# my_tuple[1] = 1.80 'tuple' object does no support item assignment

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "R3dlight"
my_tuple.insert(1, "Azul")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

# del my_tuple[2] TypeError: 'tuple' object doesn't support item deletion

del my_tuple
# print(my_tuple) NameError: name 'my_tuple' is not defined
