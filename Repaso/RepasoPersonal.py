#Escribe una función que reciba una cadena y devuelva cuántas vocales tiene
def contarVocales(cadena):
  contador = 0
  for i in cadena:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
      contador = contador + 1
  print(f"La cadena tiene {contador} vocales")

cadena = input("Introduce una frase: ")
cadena = cadena.lower()
contarVocales(cadena)


#Escribe una función que diga si un número es primo o no
def calcularPrimo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True
num = int(input("Introduce un numero: "))
if calcularPrimo(num):
    print(f"El numero {num} es primo")
else:
    print(f"El numero {num} no es primo")


#Escribe una función que diga si una palabra se lee igual al derecho y al revés



def comprobarPalindromo(frase):
    frase = frase.lower().replace(" ", "")
    fraseReverse = ""
    for i in range(len(frase)-1, -1, -1):
        fraseReverse += frase[i]
    return fraseReverse == frase

frase = input("Introduce una frase: ")

if comprobarPalindromo(frase):
    print(f"La frase '{frase}' es palíndromo")
else:
    print(f"La frase '{frase}' no es palíndromo")



