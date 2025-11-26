numeros = []

for i in range(1, 5):
    numero = int(input(f"\nIntroduce el numero {i}\n"))
    numeros.append(numero)
print(numeros)


def suma(lista):
    numero = 0
    for i in range(len(lista)):
        numero += lista[i]
    return numero


def promedio(lista):
    numero = 0
    for i in range(len(lista)):
        numero += lista[i]
    numero = numero / len(lista)
    return numero


def maximo(lista):
    return max(lista)


def minimo(lista):
    return min(lista)


print(f"La suma es {suma(numeros)}, el promedio es {promedio(numeros)}, el maximo es {maximo(numeros)}, el minimo es {minimo(numeros)}")