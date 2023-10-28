### Exception Handling ###

number_one = 5
number_two = 1
number_two = "1"

# ! Try except

try: # Obligatorio
    print("Hola")
    print(number_one + number_two)
    print("No se ha producido un error")
except: # Obligatorio
    # Se ejecuta si se ha producido un error
    print("Se ha producido un error")

# ! Try except else

try: # Obligatorio
    print("Hola")
    print(number_one + number_two)
    print("No se ha producido un error")
except: # Obligatorio
    print("Se ha producido un error")
else: # Opcional
    # Se ejecuta si no se ha producido un error
    print("La ejecución continúa correctamente")

# ! Try except else finally

try: # Obligatorio
    print("Hola")
    print(number_one + number_two)
    print("No se ha producido un error")
except: # Obligatorio
    print("Se ha producido un error")
else: # Opcional
    # Se ejecuta si no se ha producido un error
    print("La ejecución continúa correctamente")
finally: # Opcional
    # Se ejecuta siempre
    print("La ejecución continua")

# ! Errores específicos

try:
    print("Hola")
    print(number_one + number_two)
    print("No se ha producido un error")
except ValueError:
    print("Se ha producido un error de tipo ValueError")
except TypeError:
    print("Se ha producido un error de tipo TypeError")

# ! Captura la información exacta del error

try:
    print("Hola")
    print(number_one + number_two)
    print("No se ha producido un error")
except ValueError as e:
    print(e)
except Exception as e:
    print(e)