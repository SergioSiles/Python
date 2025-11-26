nombre = str(input("Introduce tu nombre: \n"))
while True:
    try:
        edad = int(input("\nIntroduce tu edad: \n"))
        altura = float(input("\nIntroduce tu altura en metros: \n"))
        break
    except:
        print("Por favor, introduce un numero valido")


print(f"\nHola {nombre}, tienes {edad} años y mides {altura}m\n")

print(f"La variable nombre es: {type(nombre)}")
print(f"La variable edad es: {type(edad)}")
print(f"La variable altura es:  {type(altura)}")
