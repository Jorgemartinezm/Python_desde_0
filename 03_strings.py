### Strings ###

my_string = "Mi String"
my_other_string = "Mi otro String"

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un string \n con salto de línea"
print(my_new_line_string)

my_tab_string = "\t Este es un string con tabulación"
print(my_tab_string)

my_scape_string = "\\t Este es un String \\n escapado"
print(my_scape_string)

# Formateo

name, surname, age = "Jorge", "Martínez", 15

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}") # El mejor

# Desempaquetado de caracteres

language = "python"
a, b, c, d, e, f = language # Debe tener el mismo numero de letras que variables asignadas ya que se asignará una letra por variable
print(a)
print(f)

# División

language_slice = language[1:3] # El 0 es el primer caracter
print(language_slice)

language_slice = language[1]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[1:5:2]
print(language_slice)

# Reverse

reverse_language = language[::-1]
print(reverse_language)

print("\n")

# Funciones

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.upper().isupper())
print(language.startswith("py"))
print(language.startswith("Py"))