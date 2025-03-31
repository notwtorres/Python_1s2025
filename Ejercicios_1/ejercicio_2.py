#Escribe un programa que recorra una lista de cadenas y calcule la longitud
#de cada cadena, almacenando el resultado en una nueva lista.

list1 = list()
list_of_lengths = list()
def add_string_text():
    list1.append(input("Inserte la cadena de texto => "))

def length_calculator(list_of_strings):
    list_of_lengths.clear()
    for string in list_of_strings:
        list_of_lengths.append(len(string))
        
while True:
    add_string_text()
    length_calculator(list1)
    print(list_of_lengths)
    if input(str("Desea agregar otra cadena de texto ('n' para salir / cualquier tecla para continuar) => ")).lower() != "n":
        continue
    print("Gracias por usar")
    break