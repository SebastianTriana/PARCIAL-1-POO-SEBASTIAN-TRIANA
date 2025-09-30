#Autor: Sebastian Triana

#Registro de nuevos libros SI
#Registro de nuevos usuarios SI
#Mínimo 3 categorías de libros SI
#Menu de opciones SI

#caso de uso: Biblioteca Universitaria(PARCIAL1 POO)

class Biblioteca:
    def __init__(self):
        self.inventario=[]

    def actualizar_inventario(self, value):
        self.inventario.append(value)

    def mostrar_inventario(self):
        print("\n--- Inventario de libros ---")
        for libro in self.inventario:
            print(libro)

class Libro:
    def __init__(self, nombre, categoria):
        self.nombre = nombre
        self.categoria = categoria

    def __str__(self):
        return f"Libro: {self.nombre}, Categoría: {self.categoria}"

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre


def registro_libro(biblioteca):
    categorias = ["suspenso", "aventura", "ficcion", "N/A"]
    nombre_libro = input("\nIngrese el nombre del libro: ")
    opcion_categoria = input("\nIngrese el genero del libro de entre las opciones: \n 1 para suspenso \n 2 para aventura \n 3 para ficcion \nDigite su opcion: ")
    if opcion_categoria == "1":
        categoria = categorias[0]
    elif opcion_categoria == "2":
        categoria = categorias[1]
    elif opcion_categoria == "3":
        categoria = categorias[2]
    else:
        categoria = categorias[3]
        print(f"\nOpcion invalida, no se le asignara ningun genero al libro ({categoria})")

    libro = Libro(nombre_libro, categoria)
    biblioteca.actualizar_inventario(libro)
    biblioteca.mostrar_inventario()


def main():
    b = Biblioteca()
    print("\n ***Sistema de biblioteca***")

    while True:
        opcion = input("\n --- Menu ---  \n-para registro de nuevos LIBROS ingrese 1- \n-para registro de nuevos USUARIOS ingrese 2- \n-para salir ingrese 0-\n Digite su opcion: ")
        if opcion == "1":
            registro_libro(b)
        elif opcion == "2":
            print("Función de registro de usuarios pendiente...")
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida, intente de nuevo.")

main()
