sumatoria = 0

num = int(input("Ingrese un número: "))

while num != 0:
    sumatoria += num
    num = int(input("Ingrese un número: "))

print(f"El resultado es: {sumatoria}.")