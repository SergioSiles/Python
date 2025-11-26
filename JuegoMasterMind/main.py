import funciones
from colorama import Fore, init

print(f"{Fore.GREEN}Bienvenido a MasterMind!!{Fore.RESET}")

funciones.generarColores()
while True:
    print(f"{Fore.RESET}Colores introducidos:", *funciones.pedirColores())
    funciones.contarAciertos()
    if funciones.comprobacionFinal():
        print(f"{Fore.RESET}La combinacion era", *funciones.generarListaEmojis())
        break
