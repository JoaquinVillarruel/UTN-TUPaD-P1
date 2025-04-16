#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene
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



