# 1. Crea una lista de cadenas de texto. Escribe un programa que recorra 
# esta lista y concatene todas las cadenas en una sola cadena, separadas 
# por un espacio.

list1 = list()

def add_string_text():
    list1.append(input("Inserte la cadena de texto => "))

def concatenate_list(list_of_strings):
    return " ".join(list_of_strings)

while True:
    add_string_text()
    print(concatenate_list(list1))
    if input(str("Desea agregar otra cadena de texto ('n' para salir / cualquier tecla para continuar) => ")).lower() != "n":
        continue
    print("Gracias por usar")
    break


