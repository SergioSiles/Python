import sys
import emoji


def calculadora(numero1, simbolo, numero2):
    try:
        if simbolo == "+":
            return numero1 + numero2
        elif simbolo == "-":
            return numero1 - numero2
        elif simbolo == "*":
            return numero1 * numero2
        elif simbolo == "/":
            return numero1 / numero2
        else:
            print(f"Operador {simbolo} no válido, usa +, -, * o /")
            return None
    except TypeError:
        print(emoji.emojize(":prohibited: Introduce un numero valido"))
        return None
    except ZeroDivisionError:
        print(emoji.emojize(":prohibited: No se puede dividir entre cero"))
        return None


if len(sys.argv) != 4:
    print("Uso: python calculadora.py 'numero1' 'operador' 'numero2'")
    sys.exit(1)

try:
    num1 = float(sys.argv[1])
    op = sys.argv[2]
    num2 = float(sys.argv[3])
except ValueError:
    print(emoji.emojize(":prohibited: Introduce numeros validos"))
    sys.exit(1)

resultado = calculadora(num1, op, num2)
if resultado is not None:
    print(f"Resultado: {resultado}")
