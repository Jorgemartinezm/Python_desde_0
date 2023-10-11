### Functions ###

def my_fuction():
    print("Esto es una función")

my_fuction()
my_fuction()
my_fuction()

def sum_two_values(first_number, second_number):
    print(first_number + second_number)

sum_two_values(5, 7)
sum_two_values(54545, 74541)
sum_two_values("5", "7")
sum_two_values(1.4, 5.2)

def sum_two_values_with_return(first_value, second_value):
    my_sum = first_value + second_value
    return my_sum

my_result = sum_two_values_with_return(10, 5)
print(my_result)

my_result = sum_two_values(1.4, 5.3)
print(my_result)

def print_name(name, surname):
    print(f"{name} {surname}")

print_name(surname = "Jorge", name = "Martínez")

def print_name_with_default(name, surname, alias = "Sin alias"):
    print(f"{name} {surname}, {alias}")

print_name_with_default("Jorge", "Martínez", "R3dlight")
print_name_with_default("Jorge", "Martínez")

def print_texts(*texts):
    for text in texts:
        print(text.upper())

print_texts("Hola", "Buenas", "Python")
print_texts("Hola")

