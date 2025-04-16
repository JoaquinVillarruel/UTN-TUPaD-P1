sumatoria = 0

valor_1 = int(input("Ingrese el primer valor: "))
valor_2 = int(input("Ingrese el segundo valor: "))

for i in range(valor_1 + 1,valor_2):
    sumatoria += i

print(f"La sumatoria de todos los valores enteros entre {valor_1} y {valor_2} es: {sumatoria}.")
