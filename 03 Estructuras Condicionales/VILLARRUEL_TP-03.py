#Ejercicio 1
edad = int(input("Ingrese su edad: "))

if edad > 18:
    print("Es mayor de edad.")

#Ejercicio 2
nota = float(input("Ingrese su nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#Ejercicio 3
num = int(input("Ingrese un numero par: "))

if num % 2 == 0:
    print("Ha ingresado un número par.")
else:
    print("Por favor, ingrese un número par.")

#Ejercicio 4
edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Sos niño/a")
elif edad < 18:
    print("Sos adolescente")
elif edad < 30:
    print("Sos adulto/a joven")
else:
    print("Sos adulto/a")

#Ejercicio 5
contra = input("Ingrese una contraseña: ")

if len(contra) >= 8 and len(contra) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Ejercicio 6
import random
from statistics import mode,median,mean
numeros_alea = [random.randint(1, 100) for i in range(50)]

moda = mode(numeros_alea)
mediana = median(numeros_alea)
media = mean(numeros_alea)
print(moda)
print(mediana)
print(media)
if media > mediana and mediana > moda:
    print("Hay sesgo positivo")
elif media < mediana and mediana < moda:
    print("Hay sesgo negativo")
else:
    print("Sin sesgo")

#Ejercicio 7
texto = input("Ingrese una palabra o frase: ")

ult_letra = texto[-1]

if ult_letra.lower() in "aeiou":
    texto += '!'

print(texto)

#Ejercicio 8
nombre = input("Ingrese su nombre: ")
num = int(input("Ingrese un numero: "))

if num == 1:
   nombre = nombre.upper()
elif num == 2:
    nombre = nombre.lower()
else:
    nombre = nombre.title()

print(nombre)

#Ejercicio 9
magnitud = int(input("Ingrese la magnitud: "))

if magnitud < 3: 
    print("Muy leve")
elif magnitud >= 3 and magnitud < 4:
    print("Leve")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte")
elif magnitud >= 6 and magnitud < 7:
    print("Muy fuerte")
else:
    print("Extremo")

#Ejercicio 10
emis = input("En que emisferio se encuentra?: ")
mes = int(input("Ingrese el mes: "))
dia = int(input("Ingrese el dia: "))

if emis == 'n':
    if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
        print("Invierno")
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
        print("Primavera")
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
        print("Verano")
    elif (mes == 9 and dia >= 21) or (10 <= mes <= 11) or (mes == 12 and dia <= 20):
        print("Otoño")
else:
    if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
        print("Verano")
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
        print("Otoño")
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
        print("Invierno")
    elif (mes == 9 and dia >= 21) or (10 <= mes <= 11) or (mes == 12 and dia <= 20):
        print("Primavera")
    