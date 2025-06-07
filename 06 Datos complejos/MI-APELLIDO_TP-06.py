#Ejercicio 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

#Ejercicio 2
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

#Ejercicio 3
lista_frutas = list(precios_frutas.keys())
print(lista_frutas)

#Ejercicio 4
agendas = {}
for i in range(5):
    agendas[input("Ingrese el nombre del contacto: ")] = input("Ingrese el numero telefonico: ")

nombre = input("Ingrese el contacto a buscar: ")
if nombre in agendas:
    print(f"El numero es: {agendas[nombre]}")
else:
    print("El contacto no existe")

#Ejercicio 5
frase = input("Ingrese una frase: ")
palabras = frase.split()
palabras_set = set(palabras)
cuenta = {}
for palabra in palabras:
    if palabra in cuenta:
        cuenta[palabra] += 1
    else:
        cuenta[palabra] = 1

print(palabras_set)
print(cuenta)

#Ejercicio 6
alumnos = {}
for i in range(3):
    alumnos[input("Ingrese un nombre: ")] = (int(input("Nota 1: ")), int(input("Nota 2: ")), int(input("Nota 3: ")))
suma = 0
for key, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {key} es: {promedio}")

#Ejercicio 7
parcial1 = {'Ana', 'Bruno', 'Carlos', 'Diana', 'Elena'}
parcial2 = {'Carlos', 'Diana', 'Federico', 'Gabriela'}


print(f"Aprobaron los dos parciales: {parcial1 & parcial2}")
print(f"Aprobaron solo un parcial: {parcial1 ^ parcial2}")
print(f"Aprobaron al menos uno: {parcial1 | parcial2}")

#Ejercicio 8
stock = {'Harina': 20,'Galletitas': 10,'Caramelos':40}

opcion = int(input("Ingrese una opción: \n1.Consultar stock \n2.Agregar stock \n"))

if opcion == 1:
    print(f"El Stock es de: {stock[input("Ingrese el producto: \n")]}")
elif(opcion == 2):
    producto = input("Ingrese el nombre del producto: \n")
    if producto in stock:
        stock[producto] += int(input("Ingrese el stock: \n"))
    else:
        stock[producto] = int(input("Ingrese el stock: \n"))
    print(f"Stock actualizado: {stock[producto]}")

#Ejercicio 9
agenda = {
    ("Lunes", "10:00"): "Reunión",
    ("Martes", "15:00"): "Clase ingles"
}
dia = input("Ingrese el dia a consultar: ")
hora = input("Ingrese la hora a consultar: ")
print(agenda[(dia, hora)])

#Ejercicio 10
original = {"Argentina": "Buenos Aires", "Uruguay": "Montevideo"}
invertido = {}
for pais, ciudad in original.items():
    invertido[ciudad] = pais
print(original)
print(invertido)
