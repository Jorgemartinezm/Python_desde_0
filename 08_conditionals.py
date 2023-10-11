### Conditionals ###

my_condition = False

if my_condition:
    print("Se ejecuta la condición del if")

my_condition = 5 * 3

if my_condition == 10:
    print("Se ejecuta la condición del segundo if")

if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10")
elif my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
elif my_condition == 1:
    print("Es igual a 1")
else:
    print("Es menor o igual que 10")

print("Mi ejecución continua")

my_string = ""

if not my_string:
    print("Mi cadena de texto no es vacía")

if my_string == "Mi cadena de textooooooooo":
    print("Estas cadenas de texto coinciden")