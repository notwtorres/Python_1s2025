#Escribe un programa que recorra una lista de cadenas y 
#divida cada cadena en subcadenas utilizando un delimitador 
#específico (por ejemplo, una coma o un espacio).

list1 = list()

def add_string_text():
    list1.append(input("Inserte la cadena de texto => "))

def convert_to_substrings(list_of_strings):
    character = input("Ingrese el delimitador deseado => ")
    new_list = []
    for string in list_of_strings:
        new_list.append(string.split(character, -1))
    return new_list

        
while True:
    if input(("Desea agregar una cadena de texto ('n' para salir / cualquier tecla para continuar) => ")).lower() != "n":
        add_string_text()
        modified_list = convert_to_substrings(list1)
        print(modified_list)
        continue
    print("Gracias por usar")
    break