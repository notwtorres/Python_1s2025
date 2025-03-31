#Escribe un programa que recorra una lista de cadenas 
# y las ordene alfabéticamente en orden ascendente.

list1 = list()

def add_string_text():
    list1.append(input("Inserte la cadena de texto => "))
         
while True:
    if input(("Desea agregar una cadena de texto ('n' para salir / cualquier tecla para continuar) => ")).lower() != "n":
        add_string_text()
        list1.sort()
        print(list1)
        continue
    print("Gracias por usar")
    break