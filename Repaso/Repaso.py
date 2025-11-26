import random
import math
#########
#Nivel 1#
#########

#Ejercicio 1
#Pide al usuario su nombre y edad, y muestra un mensaje
# nombre = input("Introduce tu nombre: ")
# edad = int(input("Introduce tu edad: "))
# print(f"Hola {nombre}, tienes {edad} años y dentro de un mes tendras {edad + 1}")

#Ejercicio 2
#Pedir una nota y decir en que nivel esta, suficiente, notable....
# nota = int(input("Introduce tu nota: "))
# if nota > 10:
#     print(f"Nota no válida, introduce una nota del 0 al 10")
# elif nota >= 9:
#     print(f"Tu nota es {nota}, tienes sobresaliente")
# elif nota >= 7:
#     print(f"Tu nota es {nota}, tienes notable")
# elif nota >= 5:
#     print(f"Tu nota es {nota}, estas aprobado")
# elif nota < 0:
#     print(f"Nota no válida, introduce una nota del 0 al 10")
# elif nota < 5:
#     print(f"Tu nota es {nota}, estas suspenso")

#Ejercicio 3
#Escribe un programa que pida un número n y muestre todos los números del 1 al n
# n = int(input("Introduce un numero aleatorio: "))
# for i in range(1, n + 1):
#     print(i)

#Ejercicio 4
#Pide 5 números y guárdalos en una lista
# lista = []
# total = 0
# for i in range(1, 6):
#     numero = int(input(f"Introduce el numero {i}: "))
#     lista.append(numero)
# for i in range(len(lista)):
#     total += lista[i]
# print(f"El numero mas grande de la lista es {max(lista)}")
# print(f"El numero mas pequeño de la lista es {min(lista)}")
# print(f"La suma total es {total}")
# print(f"El promedio es {total / len(lista)}")

#########
#Nivel 2#
#########

#Ejercicio 1
#Crea una función es_par(numero) que devuelva True si el número es par, False si no
# eleccion = int(input("Introduce un numero para saber si es par o impar: "))
# def esPar(numero):
#     if numero % 2 == 0:
#         print(f"{numero} es par")
#     else :
#         print(f"{numero} es impar")
# esPar(eleccion)

#Ejercicio 2
#Crea una función promedio(lista) que devuelva el promedio de una lista de números
# lista = [1, 2, 3, 4, 5]
# def promedio(lista):
#     total = 0
#     for i in range(len(lista)):
#         total += lista[i]
#     print(total / len(lista))
# promedio(lista)

#Ejercicio 3
#El ordenador genera un número entre 1 y 10
#El usuario tiene que adivinarlo, y el programa le dice si su intento es mayor o menor
# numeroGenerado = math.trunc(random.random() * 10 + 1)
# while(True):
#     respuesta = int(input(f"Introduce un numero del 1 al 10: "))
#     if respuesta < numeroGenerado:
#         print(f"El numero {respuesta} es menor al numero generado")
#     elif respuesta > numeroGenerado:
#         print(f"El numero {respuesta} es mayor al numero generado")
#     elif respuesta == numeroGenerado:
#         print(f"Ganasta!! El numero era {numeroGenerado}")
#     

#########
#Nivel 3#
#########

#Ejercicio 1
#Crea una lista con 5 números aleatorios entre 1 y 10
#Pide un número al usuario y di si está o no en la lista
# listaAleatoria = []
# for i in range(5):
#     numeroGenerado = math.trunc(random.random() * 10 + 1)
#     listaAleatoria.append(numeroGenerado)
# print(listaAleatoria)
# numeroUsuario = int(input("Introduce un numero del 1 al 10: "))
# if numeroUsuario in listaAleatoria:
#     print(f"El numero {numeroUsuario} esta en la lista")
# else:
#     print(f"El numero {numeroUsuario} no esta en la lista")

#Ejercicio 2
#Simula el lanzamiento de un dado 100 veces y muestra
#Cuántas veces salió cada número

#Version con If
# listaNumeros = []
# contador1 = 0
# contador2 = 0
# contador3 = 0
# contador4 = 0
# contador5 = 0
# contador6 = 0
# for i in range(100):
#     numeroGenerado = math.trunc(random.random() * 6 + 1)
#     listaNumeros.append(numeroGenerado)

# for i in range(len(listaNumeros)):
#     if listaNumeros[i] == 1:
#         contador1 += 1
#     if listaNumeros[i] == 2:
#         contador2 += 1
#     if listaNumeros[i] == 3:
#         contador3 += 1
#     if listaNumeros[i] == 4:
#         contador4 += 1
#     if listaNumeros[i] == 5:
#         contador5 += 1
#     if listaNumeros[i] == 6:
#         contador6 += 1

# print("Los numeros han aparecido las siguientes veces: ")
# print(f"Numero 1: {contador1} veces")
# print(f"Numero 2: {contador2} veces")
# print(f"Numero 3: {contador3} veces")
# print(f"Numero 4: {contador4} veces")
# print(f"Numero 5: {contador5} veces")
# print(f"Numero 6: {contador6} veces")

#Version con Match Case
# listaNumeros = []
# contador1 = 0
# contador2 = 0
# contador3 = 0
# contador4 = 0
# contador5 = 0
# contador6 = 0
# for i in range(100):
#     numeroGenerado = math.trunc(random.random() * 6 + 1)
#     listaNumeros.append(numeroGenerado)

# for i in range(len(listaNumeros)):
#     match listaNumeros[i]:
#         case 1:
#             contador1 += 1
#         case 2:
#             contador2 += 1
#         case 3:
#             contador3 += 1
#         case 4:
#             contador4 += 1
#         case 5:
#             contador5 += 1
#         case 6:
#             contador6 += 1

# print("Los numeros han aparecido las siguientes veces: ")
# print(f"Numero 1: {contador1} veces")
# print(f"Numero 2: {contador2} veces")
# print(f"Numero 3: {contador3} veces")
# print(f"Numero 4: {contador4} veces")
# print(f"Numero 5: {contador5} veces")
# print(f"Numero 6: {contador6} veces")

#Ejercicio 3
#Pide al usuario una letra entre A, B, C o D
#Si introduce otra cosa, vuelve a preguntar hasta que lo haga bien
# letra = input("Introduce una letra de la A a la D: ")
# while(True):
#     if letra.upper() == "A" or letra.upper() == "B" or letra.upper() == "C" or letra.upper() == "D":
#         print(f"Letra registada correctamente: {letra}")
#         break
#     else:
#         letra = input("Por favor, introduce una letra válida (A-D): ")

#########
#Nivel 4#
#########

#Ejercicio 1
#
#