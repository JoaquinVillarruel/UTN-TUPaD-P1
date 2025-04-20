#Funciones
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#Codigo principal
informacion_personal(input("Ingrese su nombre: "),input("Ingrese su apellido: "), int(input("Ingrese su edad: ")),input("Ingrese su lugar de residencia: "))