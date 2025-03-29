#Agregar los nombres de x cantidad de estudiantes

list_students = list()

def add_student():
    student = input("Write de name of the student here => ")
    list_students.append(student)
def show_student():
    print("Lista de estudiantes")
    for student in list_students:
        print(student)
while True:
    add_student()
    show_student()
    if((input("Desea agregar otro estudiante s/n => ").lower() != "s")):
        break
print("hola negros")