#Escribe un programa que recorra una lista de cadenas 
#y cuente cuántas veces aparece un carácter específico
#en cada cadena. Al final, muestra el conteo para cada cadena.

list1 = list()

def add_string_text():
    list1.append(input("Inserte la cadena de texto => "))

def search_character(list_of_strings):
    character = input("Ingrese un carácter => ")
    for string in list_of_strings:
        print(f"hay {string.count(character)} en {string}")

        
while True:
    if input(("Desea agregar una cadena de texto ('n' para salir / cualquier tecla para continuar) => ")).lower() != "n":
        add_string_text()
        search_character(list1)
        continue
    print("Gracias por usar")
    break