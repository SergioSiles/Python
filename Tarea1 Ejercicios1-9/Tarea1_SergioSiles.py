import emoji
import sys

###############
# Ejercicio 1 #
###############
# nombre = str(input("Introduce tu nombre: \n"))
# edad = int(input("\nIntroduce tu edad: \n"))
# altura = float(input("\nIntroduce tu altura en metros: \n"))

# print(f"\nHola {nombre}, tienes {edad} años y mides {altura}m\n")

# print(f"La variable nombre es: {type(nombre)}")
# print(f"La variable edad es: {type(edad)}")
# print(f"La variable altura es:  {type(altura)}")


###############
# Ejercicio 2 #
###############
# nombre = input("Introduce tu nombre: \n")


# def saludar(nombre):
#     return print(f"Hola {nombre}!! \n")


# saludar(nombre)


# peso = float(input("Introduce tu peso: \n"))
# altura = float(input("Introduce tu altura: \n"))


# def calcular_imc(peso, altura):
#     total = peso * altura
#     return print(f"Tu IMC es: {total}")


# calcular_imc(peso, altura)


###############
# Ejercicio 3 #
###############
# nombre = str(input("Introduce tu nombre: \n"))
# edad = int(input("Introduce tu edad: \n"))
# aficiones = []
# print("Introduce 3 aficiones: \n")
# for i in range(3):
#     respuesta = str(input())
#     aficiones.append(respuesta)


# def presentar_persona(nombre="Usuario", edad=None, *aficiones):
#     return print(
#         f"{nombre} tiene {edad} años y le gusta: {aficiones[0]}, {aficiones[1]}, {aficiones[2]}"
#     )


# presentar_persona(nombre, edad, *aficiones)

###############
# Ejercicio 4 #
###############
# nombre = str(input("Introduce tu nombre: \n"))
# while True:
#     try:
#         edad = int(input("\nIntroduce tu edad: \n"))
#         altura = float(input("\nIntroduce tu altura en metros: \n"))
#         break
#     except:
#         print("Por favor, introduce un numero valido")


# print(f"\nHola {nombre}, tienes {edad} años y mides {altura}m\n")

# print(f"La variable nombre es: {type(nombre)}")
# print(f"La variable edad es: {type(edad)}")
# print(f"La variable altura es:  {type(altura)}")

###############
# Ejercicio 5 #
###############
# print(emoji.emojize("¡Bienvenido! :smile:", language="alias"))


# def calcular_imc_con_emoji(peso, altura):
#     imc = peso / (altura**2)
#     if imc < 18.5:
#         estado = "Bajo peso " + emoji.emojize(":warning:", language="alias")
#     elif imc < 25:
#         estado = "Normal " + emoji.emojize(":smile:", language="alias")
#     else:
#         estado = "Sobrepeso " + emoji.emojize(":exclamation:", language="alias")
#     return imc, estado


###############
# Ejercicio 7 #
###############
# numeros = []

# for i in range(1, 5):
#     numero = int(input(f"\nIntroduce el numero {i}\n"))
#     numeros.append(numero)
# print(numeros)


# def suma(lista):
#     numero = 0
#     for i in range(len(lista)):
#         numero += lista[i]
#     return numero


# def promedio(lista):
#     numero = 0
#     for i in range(len(lista)):
#         numero += lista[i]
#     numero = numero / len(lista)
#     return numero


# def maximo(lista):
#     return max(lista)


# def minimo(lista):
#     return min(lista)


# print(f"La suma es {suma(numeros)}, el promedio es {promedio(numeros)}, el maximo es {maximo(numeros)}, el minimo es {minimo(numeros)}")

###############
# Ejercicio 8 #
###############
# def main():
#     print("Argumentos recibidos:", sys.argv)

#     if len(sys.argv) > 1:
#         nombre = sys.argv[1]
#         edad = sys.argv[2]
#         ciudad = sys.argv[3]
#         print(f"Hola, {nombre} 👋, tienes {edad} años, y vives en {ciudad}")
#     else:
#         print("No se proporcionó ningún argumento")


# if __name__ == "__main__":
#     main()

###############
# Ejercicio 9 #
###############
# def calculadora(numero1, simbolo, numero2):
#     try:
#         if simbolo == "+":
#             return numero1 + numero2
#         elif simbolo == "-":
#             return numero1 - numero2
#         elif simbolo == "*":
#             return numero1 * numero2
#         elif simbolo == "/":
#             return numero1 / numero2
#         else:
#             print(f"Operador {simbolo} no válido, usa +, -, * o /")
#             return None
#     except TypeError:
#         print(emoji.emojize(":prohibited: Introduce un numero valido"))
#         return None
#     except ZeroDivisionError:
#         print(emoji.emojize(":prohibited: No se puede dividir entre cero"))
#         return None


# if len(sys.argv) != 4:
#     print("Uso: python calculadora.py 'numero1' 'operador' 'numero2'")
#     sys.exit(1)

# try:
#     num1 = float(sys.argv[1])
#     op = sys.argv[2]
#     num2 = float(sys.argv[3])
# except ValueError:
#     print(emoji.emojize(":prohibited: Introduce numeros validos"))
#     sys.exit(1)

# resultado = calculadora(num1, op, num2)
# if resultado is not None:
#     print(f"Resultado: {resultado}")
