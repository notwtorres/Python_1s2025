#Escribe un programa que recorra una lista de cadenas y 
#elimine los espacios en blanco al principio y al final de cada cadena.

list1 = list()

def add_string_text():
    list1.append(input("Inserte la cadena de texto => "))

def delete_white_spaces(list_of_strings):
    for i in range(len(list_of_strings)):
        list_of_strings[i] = list_of_strings[i].strip()

while True:
    add_string_text()
    delete_white_spaces(list1)
    print(list1)
    if input(str("Desea agregar otra cadena de texto ('n' para salir / cualquier tecla para continuar) => ")).lower() != "n":
        continue
    print("Gracias por usar")
    break