#Ejercicio1
print("Ejercicio 1")
def fact(num):
    return 1 if num == 1 or num == 0 else num * fact(num -1)

num = int(input("Ingrese un numero: "))
for i in range(1,num+1):
    print(f"{i}! = {fact(i)}")

#Ejercicio2
print("Ejercicio 2")
def fibo(num):
    return 0 if num == 0 else 1 if num == 1 else fibo(num - 1) + fibo(num - 2)

limite = int(input("Ingrese la posicion que quiera mostrar: "))

for i in range(limite + 1):
    print(fibo(i))

#Ejercicio 3
print("Ejercicio 3")
def pote(bas,exp):
    if exp == 0:
        return 1
    else:
        return bas * pote(bas,exp - 1)
    
print(pote(2,4))

#Ejercicio 4
print("Ejercicio 4")
def binario(num):
    if num == 0 or num == 1:
        return str(num)
    else:
        print(num)
        print(num%2)
        return binario(num // 2) + str(num%2)

print(binario(13))

#Ejercicio 5
print("Ejercicio5")
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])

print(es_palindromo("reconocer"))  # True
print(es_palindromo("python"))     # False

#Ejercicio 6
print("Ejercicio 6")
def suma_digitos(num):
    if num < 10:
        return num
    else:
        return (num%10) + suma_digitos(num//10) 
    
print(suma_digitos(1234))

#Ejercicio 7
print("Ejercicio 7")
def contar_bloques(num):
    if num == 1:
        return num
    else:
        return num + contar_bloques(num - 1)

print(contar_bloques(4))

#Ejercicio 8
print("Ejercicio 8")
def contar_digitos(num,dig):
    if num < 10:
        return 1 if num == dig else 0
    else:
        return (1 if num%10 == dig else 0) + contar_digitos(num//10,dig)
    
print(contar_digitos(2222,2))