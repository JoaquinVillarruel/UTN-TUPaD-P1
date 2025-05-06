#Ejercicio 1
multiplos_4 = list(range(4, 101, 4))
print(multiplos_4)

#Ejercicio 2
lista = [1, "hola",3,"mundo"]
print(lista[-2])

#Ejercicio 3
lista_vacia = []
lista_vacia.append("hola")
lista_vacia.append("mundo")
lista_vacia.append("Joaquin")
print(lista_vacia)

#Ejercicio 4
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print(animales)

#Ejercicio 5
"""
Se crea una lista con cinco numeros, mediante la funcion max() se obtiene el valor mas alto de la lista,
la funcion max() va a devolver 22 entonces quedaria numeros.remove(22) de esta forma eliminando el valor
Mas alto de la lista, finalmente se muestra como quedo la lista.
"""

#Ejercicio 6
numeros = list(range(10, 31, 5))
print(numeros[:2])

#Ejercicio 7
autos = ["sedan", "polo", "suran", "gol"]
autos[1:2] = ["focus", "etios"]
print(autos)

#Ejercicio 8
dobles = []
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)

print(dobles)

#Ejercicio 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
["agua"]]

compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)

#Ejercicio 10
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

print(lista_anidada)

