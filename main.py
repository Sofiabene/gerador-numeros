import random

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
print("Antes:", numeros)
random.shuffle(numeros)
print("Depois:", numeros)
print("Resultado:", sorted(numeros[0:15]))
