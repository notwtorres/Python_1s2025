#Escribe un programa que recorra una lista de cadenas y 
# elimine aquellas que estén vacías. Imprime la lista resultante.


list1 = list()

def add_string_text():
    list1.append(input("Inserte la cadena de texto => "))

def delete_empty_strings(list_of_strings):
    for i in range(len(list_of_strings)):
        if list_of_strings[i].strip() == "":
            list_of_strings.pop(i) 

while True:
    add_string_text()
    delete_empty_strings(list1)
    print(list1)
    if input(str("Desea agregar otra cadena de texto ('n' para salir / cualquier tecla para continuar) => ")).lower() != "n":
        continue
    print("Gracias por usar")
    break