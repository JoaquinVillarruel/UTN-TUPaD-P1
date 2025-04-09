texto = input("Ingrese una palabra o frase: ")

ult_letra = texto[-1]

if ult_letra.lower() in "aeiou":
    texto += '!'

print(texto)





