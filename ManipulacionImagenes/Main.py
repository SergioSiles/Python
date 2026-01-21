from Fondo import *
def main():
  print("1. Convertir JPG a PNG")
  print("2. Convertir PNG a SVG")
  print("3. Convertir JPG a PNG y luego a SVG")
  print("4. Salir")
  opcion = input("Introduce una opcion: ")
  while (True):
    match opcion:
      case "1":
        path_in = input("Introduce el nombre de la imagen (Sin extension): ")
        path_out = input("Introduce el nombre de la imagen de salida (Sin extension): ")
        jpg_a_png(path_in, path_out)
        exit()
      case "2":
        path_in = input("Introduce el nombre de la imagen (Sin extension): ")
        path_out = input("Introduce el nombre de la imagen de salida (Sin extension): ")
        png_a_svg(path_in, path_out)
        exit()
      case "3":
        path_in = input("Introduce el nombre de la imagen (Sin extension): ")
        path_out = input("Introduce el nombre de la imagen de salida (Sin extension): ")
        jpg_a_png(path_in, path_out)
        png_a_svg(path_out, path_out)
        exit()
      case "4":
        exit()
      case _:
        print("Opcion no valida")
        print("Introduce 1, 2 ó 3")
        opcion = input("Introduce una opcion: ")

if __name__ == "__main__":
  main()