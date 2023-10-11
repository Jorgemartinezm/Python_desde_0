### Loops ###

# While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 1
else: # Es opcional
    print("Mi condicion es menor o igual a 10")

print("La ejecución continúa")

while my_condition < 20:
    my_condition += 2
    if my_condition == 15:
        print("Mi condición es 15")
        break

    print(my_condition)

print("La ejecución continúa")

# For

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

my_tuple = (15, 1.78, "Jorge", "Martínez", "Jorge")

for element in my_tuple:
    print(element)

my_set = {"Jorge", "Martinez", 15}

for element in my_set:
    print(element)
    
my_dict = {"Nombre":"Jorge", "Apellido":"Martínez", "Edad":15, 1:"Python"}

for element in my_dict:
    print(element)
    if element == "Edad":
        continue
    print("Se ejecuta")
else:
    print("El bucle para diccionario ha finalizado")