parrafo_input = input("Escribe un párrafo: ")

if parrafo_input[-1] == ".":
    parrafo = parrafo_input[0:len(parrafo_input)-1].strip()
else: 
    parrafo = parrafo_input
    
print(parrafo)

parrafo = parrafo.strip()
oraciones = parrafo.split(".")

print(f"El párrafo tiene {len(oraciones)} oraciones")
print(oraciones)