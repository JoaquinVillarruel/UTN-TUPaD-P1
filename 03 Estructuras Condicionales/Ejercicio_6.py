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
