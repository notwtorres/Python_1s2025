#Escribe un programa que busque si una subcadena está 
#presente en cada una de las cadenas de una lista. El 
#programa debe devolver una lista con valores booleanos 
#que indiquen si la subcadena fue encontrada en cada cadena.

list1 = list()
boolean_list = list()
def add_string_text():
    list1.append(input("Inserte la cadena de texto => "))

def search_sub_string(list_of_strings, sub_string):
    return [sub_string in string for string in list_of_strings]

def add_boolean_data():
    global boolean_list
    boolean_list = search_sub_string(list1, input("Ingrese la subcadena => "))
    
while True:
    user_input = input(str("Desea agregar una cadena de texto ('n' para salir / 'b' para buscar una subcadena / cualquier tecla para continuar) => "))
    
    if user_input.lower() == "b":
        if len(list1) == 0:
            print("No hay cadenas de texto para buscar")
            continue
        add_boolean_data()
        print(f"lista booleana => {boolean_list}")
        continue
    if user_input.lower() == "n":
        print("Gracias por usar")
        break
    add_string_text()
