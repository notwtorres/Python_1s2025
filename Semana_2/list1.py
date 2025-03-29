#Almacenar 10 números enteros
#Agregar solo impares mayores de 18
list_int = list()

def add_number():
    for i in range (10):
        number = (int(input(f"{i} of 10 - Put the number here => ")))
        
        if(number < 18 or number % 2 != 1):
            print("el número tiene que ser impar y mayor que 18")
            add_number()
        list_int.append(number)

    
add_number()
print(list_int)