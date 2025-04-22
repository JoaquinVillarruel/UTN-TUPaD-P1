#Ejercicio 1
#Funciones
def imprimir_hola_mundo():
    print("Hola mundo.")

#Codigo principal
imprimir_hola_mundo()

#Ejercicio 2
#Funciones
def saludar_usuario(nombre):
    print(f"Hola {nombre}")

#Programa principal
nombre = input("Ingrese su nombre: ")
saludar_usuario(nombre)

#Ejercicio 3
#Funciones
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#Codigo principal
informacion_personal(input("Ingrese su nombre: "),input("Ingrese su apellido: "), int(input("Ingrese su edad: ")),input("Ingrese su lugar de residencia: "))

#Ejercicio 4
from math import pi
#Funciones
def calcular_area_circulo(radio):
    return pi * (radio**2)

def calcular_perimetro_circulo(radio):
    return pi * (2*radio)

#Programa principal
radio = int(input("Ingrese el radio del circulo: "))

print(f"Area = {calcular_area_circulo(radio)}")
print(f"Perimetro = {calcular_perimetro_circulo(radio)}")

#Ejercicio 5
#Funciones
def segundos_a_horas(segundos):
    return segundos/3600

#Programa principal
segundos = int(input("Ingrese los segundos: "))

print(f"{segundos} segundos equivalen a {segundos_a_horas(segundos)} horas.")

#Ejercicio 6
#Funciones
def tabla_multiplicar(numero):
    print(f"La tabla de {numero} es: ")
    for i in range(1,11):
        print(i*numero)

#Programa principal
numero = int(input("Ingrese un numero: "))
tabla_multiplicar(numero)

#Ejercicio 7
#Funciones
def operaciones_basicas(a,b):
    return(a+b,a-b,a*b,a/b)

#Programa principal
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

resultados = operaciones_basicas(num1,num2)

print(f"{num1} + {num2} = {resultados[0]}\n{num1} - {num2} = {resultados[1]}\n{num1} * {num2} = {resultados[2]}\n{num1} / {num2} = {resultados[3]}")

#Ejercicio 8
#Funciones
def calcular_imc(peso, altura):
    return peso / (altura**2)

#Programa principal
peso = float(input("Ingrese el peso en kg: "))
altura = float(input("Ingrese la altura en metros: "))

print(f"El IMC es: {calcular_imc(peso,altura)}")

#Ejercicio 9
#Funciones
def celsius_a_fahrenheit(celsius):
    return (celsius * (9/5)) + 32

#Programa principal
celsius = float(input("Ingrese la temperatura en celsius: "))
print(f"{celsius}C° = {celsius_a_fahrenheit(celsius)}F°")

#Ejercicio 10
#Funciones
def calcular_promedio(a,b,c):
    return (a + b + c) / 3

#Programa principal
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))

print(f"El promedio entre los numeros es: {calcular_promedio(num1,num2,num3)}")
