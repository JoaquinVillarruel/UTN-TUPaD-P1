#Estudiante: VILLARRUEL Joaquin

#Ejercicio 1
print("Hola Mundo!")

#Ejercicio 2
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

#Ejercicio 3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido:")
edad = input("Ingrese su edad:")
residencia = input("Ingrese su lugar de residencia:")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#Ejercicio 4
radio = int(input("Ingrese el radio del circulo: "))
area = 3.14*(radio**2)
perimetro = 2*3.14*radio
print(f"El area es: {area}")
print(f"El perimetro es: {perimetro}")

#Ejercicio 5
segundos = int(input("Ingrese los segundos: "))
segundos = segundos/3600
print(f"Equivale a {segundos}")

#Ejercicio 6
numero = int(input("Ingrese un numero: "))
print(f"{numero*1}, {numero*2}, {numero*3}, {numero*4}, {numero*5}, {numero*6}, {numero*7}, {numero*8}, {numero*9}, {numero*10}")

#Ejercicio 7
num1 = int(input("Ingrese un numero distinto de cero: "))
num2 = int(input("Ingrese otro numero distinto de cero: "))
print(f"la suma es: {num1 + num2}, resta{num1 - num2}, division: {num1/num2}, multiplicación {num1 * num2}")

#Ejercicio 8
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros"))
imc = peso/(altura**2)
print(f"Su IMC es: {imc}")

#Ejercicio 9 
tempC = float(input("Ingrese una temperatura en grados Celsius: "))
tempF = ((9/5)*tempC) + 32
print(f"La temperatura en Fahrenheit es: {tempF}")

#Ejercicio 10
num1 = float(input("Ingrese tres numeros: "))
num2 = float(input())
num3 = float(input())
promedio = (num1 + num2 + num3)/3
print(f"El promedio es: {promedio}")