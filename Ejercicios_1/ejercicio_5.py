#Escribe un programa que recorra una lista de cadenas 
# y reemplace todas las apariciones de un carácter específico
# con otro carácter, luego imprime la lista modificada.

list1 = list()

def add_string_text():
    list1.append(input("Inserte la cadena de texto => "))
    
def switch_character(list_of_strings):
    character1 = input("Ingrese el carácter a cambiar => ")
    character2 = input("Ingrese el nuevo carácter => ")
    for i in range(len(list_of_strings)):
        list_of_strings[i] = list_of_strings[i].replace(character1, character2)

while True:
    user_input = input(str("Desea agregar una cadena de texto ('n' para salir / 's' cambiar carácter / cualquier tecla para continuar) => "))
    
    if user_input.lower() == "s":
        if len(list1) == 0:
            print("No hay cadenas de texto para buscar")
            continue
        switch_character(list1)
        print(f"lista modificada => {list1}")
        continue
    if user_input.lower() == "n":
        print("Gracias por usar")
        break
    add_string_text()
    
