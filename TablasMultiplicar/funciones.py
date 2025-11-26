import sys
numeroUsuario = 0

def pedirNumero():
  global numeroUsuario
  while numeroUsuario < 1 or numeroUsuario > 10:
    print("Los valores válidos son del 1 al 10")
    try:
      numeroUsuario = int(input("¿Qué tabla de multiplicar quieres?: "))
    except ValueError:
      print("Solo valores del 1 al 10.")
    except:
      print("Se ha producido un error.")

def pintarTablas(numero):
  for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

def ejecutarConArgumento():
  if len(sys.argv)<1 and len(sys.argv)>1:
    print("El programa solo recibe 1 argumento")
  else:
    pintarTablas(int(sys.argv[1]))
    