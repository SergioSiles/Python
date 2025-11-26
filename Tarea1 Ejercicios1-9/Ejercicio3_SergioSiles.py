nombre = str(input("Introduce tu nombre: \n"))
edad = int(input("Introduce tu edad: \n"))
aficiones = []
print("Introduce 3 aficiones: \n")
for i in range(3):
    respuesta = str(input())
    aficiones.append(respuesta)


def presentar_persona(nombre="Usuario", edad=None, *aficiones):
    return print(
        f"{nombre} tiene {edad} años y le gusta: {aficiones[0]}, {aficiones[1]}, {aficiones[2]}"
    )


presentar_persona(nombre, edad, *aficiones)
