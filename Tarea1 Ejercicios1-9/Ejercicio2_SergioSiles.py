nombre = input("Introduce tu nombre: \n")


def saludar(nombre):
    return print(f"Hola {nombre}!! \n")


saludar(nombre)


peso = float(input("Introduce tu peso: \n"))
altura = float(input("Introduce tu altura: \n"))


def calcular_imc(peso, altura):
    total = peso * altura
    return print(f"Tu IMC es: {total}")


calcular_imc(peso, altura)
