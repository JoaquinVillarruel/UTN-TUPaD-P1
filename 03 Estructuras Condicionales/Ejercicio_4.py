edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Sos niño/a")
elif edad < 18:
    print("Sos adolescente")
elif edad < 30:
    print("Sos adulto/a joven")
else:
    print("Sos adulto/a")