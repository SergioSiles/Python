import sys


def main():
    print("Argumentos recibidos:", sys.argv)

    if len(sys.argv) > 1:
        nombre = sys.argv[1]
        edad = sys.argv[2]
        ciudad = sys.argv[3]
        print(f"Hola, {nombre} 👋, tienes {edad} años, y vives en {ciudad}")
    else:
        print("No se proporcionó ningún argumento")


if __name__ == "__main__":
    main()