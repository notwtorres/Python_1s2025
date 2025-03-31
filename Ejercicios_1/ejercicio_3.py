#Escribe un programa que recorra una lista de cadenas y 
# convierta cada cadena a mayúsculas o minúsculas dependiendo
# de un criterio. Si la longitud de la cadena es par, se 
# convertirá a mayúsculas; si es impar, a minúsculas.

list1 = list()

def add_string_text():
    list1.append(input("Inserte la cadena de texto => "))

def word_modifier(list_of_strings):
    for string in list_of_strings:
        if len(string) % 2 == 0:
            print(f"{string.upper()} / longitud => {len(string)}")
        else:
            print(f"{string.lower()} / longitud => {len(string)}")
            
while True:
    add_string_text()
    word_modifier(list1)
    if input(str("Desea agregar otra cadena de texto ('n' para salir / cualquier tecla para continuar) => ")).lower() != "n":
        continue
    print("Gracias por usar")
    break