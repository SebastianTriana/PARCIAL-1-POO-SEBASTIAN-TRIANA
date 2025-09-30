#Autor: Sebastian Triana

#Registro de nuevos libros X
#Registro de nuevos usuarios X
#Mínimo 3 categorías de libros X
#Menu de opciones X

#caso de uso: Biblioteca Universitaria(PARCIAL1 POO)


class Biblioteca:
    #definimos el constructor de la biblioteca con un inventario y usuarios
    def __init__(self):
        self.inventario=[]

    def actualizar_inventario(self, value):
        self.inventario.append(value)

    def mostrar_inventario(self):
        print(self.inventario)

class Libro:
    #definimos el constructor de los libros con su categoria
    def __init__(self, nombre, categoria):
        self.nombre = nombre
        self.categoria = categoria

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre


def registro_libro():
    b = Biblioteca()
    categorias = ["suspenso", "aventura", "ficcion", "N/A"]
    nombre_libro = input("\nIngrese el nombre del libro: ")
    opcion_categoria = input("\nIngrese el genero del libro de entre las opciones: \n 1 para suspenso \n 2 para aventura \n 3 para ficcion \nDigite su opcion: ")
    if opcion_categoria == "1":
            categoria = categorias[0]
            print(f"\nSe le ha asignado el genero {categorias[0]} a su libro")
    elif opcion_categoria == "2":
            categoria = categorias[1]
            print(f"\nSe le ha asignado el genero {categorias[1]} a su libro")
    elif opcion_categoria == "3":
            categoria = categorias[2]
            print(f"\nSe le ha asignado el genero {categorias[2]} a su libro")
    else:
            print(f"\nOpcion invalida, no se le asignara ningun genero al libro ({categorias[3]})")
            categoria = categorias[3]

    libro = Libro(nombre_libro, categoria)
    b.actualizar_inventario(libro)
    b.mostrar_inventario()

def main():
    print("\n ***Sistema de biblioteca***")
    opcion = input("\n --- Menu ---  \n-para registro de nuevos LIBROS ingrese 1- \n-para registro de nuevos USUARIOS ingrese 2- \n Digite su opcion: ")
    if opcion == "1":
         registro_libro()
    elif opcion == "2":
        pass

main()