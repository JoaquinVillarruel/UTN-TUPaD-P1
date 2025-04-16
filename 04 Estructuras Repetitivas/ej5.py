from random import randint

intentos = 1

num_aleat = randint(0,9)

num = int(input("Ingrese un numero: "))
while num != num_aleat:
    num = int(input("Ingrese un numero: "))
    intentos += 1

print(f"Necesitaste {intentos} intentos.")
