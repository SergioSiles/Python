import random
import os
import emoji
from colorama import Fore, init

init()

intentos = 0
listaColores = ["R", "V", "A", "N"]
listaColoresAleatorios = []
listaColoresUsuario = []
listaColoresUsuarioEmojis = []
listaColoresAleatoriosEmojis = []


def limpiarConsola():
    os.system("cls" if os.name == "nt" else "clear")


def generarColores():
    for i in range(4):
        color = random.choice(listaColores)
        listaColoresAleatorios.append(color)
        print(listaColoresAleatorios)
    return listaColoresAleatorios

def generarListaEmojis():
    for i in range(4):
        if listaColoresAleatorios[i] == "R":
            listaColoresAleatoriosEmojis.append(emoji.emojize(":red_circle:"))
        elif listaColoresAleatorios[i] == "V":
            listaColoresAleatoriosEmojis.append(emoji.emojize(":green_circle:"))
        elif listaColoresAleatorios[i] == "A":
            listaColoresAleatoriosEmojis.append(emoji.emojize(":blue_circle:"))
        elif listaColoresAleatorios[i] == "N":
            listaColoresAleatoriosEmojis.append(emoji.emojize(":black_circle:"))
    return listaColoresAleatoriosEmojis

def pedirColores():
    global intentos
    intentos += 1
    listaColoresUsuario.clear()
    listaColoresUsuarioEmojis.clear()
    listaColoresAleatoriosEmojis.clear()

    while len(listaColoresUsuario) < 4:
        colorIntroducido = input(
            emoji.emojize(
                f"{Fore.RESET}Introduce el color {len(listaColoresUsuario) + 1} "
                f"({Fore.RED}:red_circle: R {Fore.GREEN} :green_circle: V {Fore.BLUE} :blue_circle: A {Fore.BLACK} :black_circle: N): "
            )
        ).upper()

        if colorIntroducido not in listaColores:
            print(
                emoji.emojize(
                    f"{Fore.RED}:warning: Por favor, introduce un color válido"
                )
            )
        else:
            listaColoresUsuario.append(colorIntroducido)
            if colorIntroducido == "R":
                listaColoresUsuarioEmojis.append(emoji.emojize(":red_circle:"))
            elif colorIntroducido == "V":
                listaColoresUsuarioEmojis.append(emoji.emojize(":green_circle:"))
            elif colorIntroducido == "A":
                listaColoresUsuarioEmojis.append(emoji.emojize(":blue_circle:"))
            elif colorIntroducido == "N":
                listaColoresUsuarioEmojis.append(emoji.emojize(":black_circle:"))

    return listaColoresUsuarioEmojis

def contarAciertos():
    aciertosPosicion = 0
    aciertosLista = 0
    aleatoriosTachados = []

    for color in listaColoresAleatorios:
        aleatoriosTachados.append(color)

    for i in range(4):
        if listaColoresUsuario[i] == aleatoriosTachados[i]:
            aciertosPosicion += 1
            aleatoriosTachados[i] = None

    for i in range(4):
        if listaColoresUsuario[i] != listaColoresAleatorios[i]:
            for j in range(4):
                if listaColoresUsuario[i] == aleatoriosTachados[j]:
                    aciertosLista += 1
                    aleatoriosTachados[j] = None
                    break

    print(
        f"{Fore.YELLOW}Hay {aciertosPosicion} colores en la posición correcta "
        f"y {aciertosLista} en la lista"
    )

def comprobacionFinal():
    if listaColoresUsuario == listaColoresAleatorios:
        limpiarConsola()
        print(
            emoji.emojize(
                f"{Fore.GREEN}Has acertado todos los colores!! :party_popper: :party_popper:"
            )
        )
        print(f"Te ha costado {intentos} intentos.")
        return True
    return False
