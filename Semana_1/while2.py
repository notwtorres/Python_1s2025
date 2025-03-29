cont = 1
number = int(input("Ingresa a un numero: "))
print(f"Tabla de multiplicar del {number}")
print("="*13)
while cont <= 12:
    print(f"{number} x {cont} = {number * cont}")
    cont += 1
print("=" * 13)