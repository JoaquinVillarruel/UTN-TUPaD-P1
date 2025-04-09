nombre = input("Ingrese su nombre: ")
num = int(input("Ingrese un numero: "))

if num == 1:
   nombre = nombre.upper()
elif num == 2:
    nombre = nombre.lower()
else:
    nombre = nombre.title()

print(nombre)