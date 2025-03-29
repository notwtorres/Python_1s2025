nombre = "Fernando"
apellido = "Jimenez"

nombre_completo = nombre + " " + apellido
print(nombre_completo) 

nombre_completo2 = f"{nombre} {apellido}"
print(nombre_completo2)

nombre_completo3 = " ".join(nombre, apellido)

list = [nombre, apellido]
nombre_completo4 = " ".join(list)
print(nombre_completo4)