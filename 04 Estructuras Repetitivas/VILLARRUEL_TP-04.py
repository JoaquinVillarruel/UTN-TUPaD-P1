#Ejercicio 1
for i in range(101):
    print(i)

#Ejercicio 2
contador = 0
num = int(input("Ingrese un numero entero: ")) #Solicito un número

num = abs(num) #Obtengo el valor absoluto por si se ingresa un negativo

if num == 0: #En caso de que se ingrese un cero se asigna uno al contador
    contador = 1
else:
    while num > 0: #Utilizo un bucle para contar los digitos
        num //= 10 #Elimino el ultimo digito
        contador += 1 #Sumo uno al contador

#Imprimo la cantidad de digitos
print(f"El numero tiene {contador} digitos")

#Ejercicio 3
sumatoria = 0
#Solicito al usuario los dos valores
valor_1 = int(input("Ingrese el primer valor: "))
valor_2 = int(input("Ingrese el segundo valor: "))

#Realizo las sumas con ayuda de un for
for i in range(valor_1 + 1,valor_2): 
    sumatoria += i

#Imprimo el resultado
print(f"La sumatoria de todos los valores enteros entre {valor_1} y {valor_2} es: {sumatoria}.")

#Ejercicio 4
sumatoria = 0

num = int(input("Ingrese un número: ")) #Solicito un número al usuario para poder empezar el bucle

while num != 0: #Mientras el usuario no ingrese cero el bucle continua
    sumatoria += num #Sumo el valor anterior con el nuevo
    num = int(input("Ingrese un número: ")) #Pido un valor al usuario para continuar o terminar el bucle

#Imprimo el resultado
print(f"El resultado es: {sumatoria}.")

#Ejercicio 5
from random import randint

intentos = 1

num_aleat = randint(0,9) #Genero un numero aleatorio entre 0 y 9

num = int(input("Ingrese un numero: ")) #Solicito un numero
while num != num_aleat: #Mientras el numero ingresado sea distinto al numero aleatorio continua el bucle
    num = int(input("Ingrese un numero: ")) #Solicito un numero al usuario
    intentos += 1 #Incremento el total de intentos

#Imprimo los intentos
print(f"Necesitaste {intentos} intentos.")

#Ejercicio 6
for i in range(98,0,-2):
    print(i)

#Ejercicio 7
num = int(input("Ingrese un numero: "))

sumatoria = 0

for i in range (0,num):
    sumatoria += i

print(sumatoria)

#Ejercicio 8
pares = 0
impares = 0
pos = 0
neg = 0

#Mediante un for pido los 100 numeros al usuario
for i in range(100):

    num = int(input("Ingrese un número: "))

    #Verifico si el numero es par o impar y sumo al contador correspondiente
    if num %2 == 0:
        pares += 1
    else:
        impares += 1
    
    #Verifico si el numero es positivo o negativo y sumo al contador correspondiente
    if num > 0:
        pos += 1
    else:
        neg += 1

#Imprimo los resultados
print(f"{pares} de los numeros son pares y {impares} son impares.")
print(f"{neg} numeros negativos y {pos} numeros positivos.")

#Ejercicio 9
numeros = 0
cont = 0

#Pido los 100 numeros con ayuda de un for
for i in range(100):
    numeros += int(input("Ingrese un número: ")) #Mientras se ingresan los numero los sumo
    cont += 1 #Cuento cuantos numeros se ingresaron

#Imprimo el resultado
print(f"La media de los valores es: {numeros/cont}")

#Ejercicio 10
num = int(input("Ingrese un numero: "))

negativo = num < 0 #Verifico si el numero es negativo

num = abs(num)

invertido = 0

while num > 0:
    digito = num % 10 #Guardo el ultimo digito
    invertido = invertido * 10 + digito #Muevo el ultimo digito a la primera posición
    num //= 10 #Elimino el ultimo digito

if negativo:
    invertido = -invertido #Si el numero ingresado es negativos hago negativo el invertido

#Imprimo el numero invertido
print(f"Numero invertido: {invertido}")