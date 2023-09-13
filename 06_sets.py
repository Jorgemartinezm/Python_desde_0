### Sets ###

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicialmente es un diccionario

my_other_set = {"Jorge", "Martinez", 15}
print(type(my_other_set))

print(len(my_other_set))

# print(my_other_set[0]) TypeError: 'set' object is not subscriptable

my_other_set.add("R3dlight")

print(my_other_set) # Un set no es una estructura ordenada

my_other_set.add("R3dlight")

print(my_other_set) # Un set no admite repetidos

print("Jorge" in my_other_set)
print("Jorje" in my_other_set)

my_other_set.remove("Jorge")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

print(type(my_other_set))
del my_other_set
# print(my_other_set) NameError: name 'my_other_set' is not defined

my_set = {"Jorge", "Martinez", 15}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Python", "Java", "C++"}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#", "Java"}))

print(my_new_set.difference(my_set))