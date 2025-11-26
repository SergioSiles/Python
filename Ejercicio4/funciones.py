listaGrados = []

def menu():
    i = True
    while i:
        print("\nQue desea hacer? ")
        print("1. Introducir nuevo valor")
        print("2. Salir")
        respuesta = int(input())
        match respuesta:
            case 1:
                i = False
                pedirGrados(listaGrados)
            case 2:
                i = False
            case _:
                print("Opcion no válida. ")

def pedirGrados(listaGrados):
    listaGrados
    grados = float(input("Introduce un numero en ºC: "))
    listaGrados.append(grados)
    calcularMedia(listaGrados)

def calcularMedia(lista):
    total = 0
    for i in range(len(lista)):
        total = total + lista[i]
    total = total / len(lista)
    maxima = int(max(lista))
    minima = int(min(lista))
    print(f"\nLa media es {total}")
    print(f"La temperatura maxima es {maxima}")
    print(f"La temperatura minima es {minima}")
    menu()