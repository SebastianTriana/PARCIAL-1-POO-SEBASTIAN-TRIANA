#Autor: Sebastian Triana

#Registro de nuevos libros SI
#Registro de nuevos usuarios AHORA SI :D
#Mínimo 3 categorías de libros SI
#Menu de opciones SI

#caso de uso: Biblioteca Universitaria(CORRECCION PARCIAL1 POO)

#BASE DE DATOS: FIREBASE
import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("C:\\Users\\Sebastian\\Downloads\\nube_firebase.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://proyecto-firebase-48337-default-rtdb.firebaseio.com/" 
})

class Biblioteca:
    def __init__(self):
        self.inventario = []
        self.usuarios = []

    def actualizar_inventario(self, libro):
        self.inventario.append(libro)

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def mostrar_inventario(self):  #agregue las funciones huerfanas a biblioteca
        print("\n--- Inventario de libros ---")  
        if not self.inventario:
            print("No hay libros registrados.")
        for libro in self.inventario:
            print(libro)

    def mostrar_usuarios(self):  #agregue tambien este metodo nuevo para hacer lo mismo pero con usuarios
        print("\n--- Lista de usuarios registrados ---")
        if not self.usuarios:
            print("No hay usuarios registrados.")
        for usuario in self.usuarios:
            print(usuario)


class Libro:
    def __init__(self, nombre, categoria):
        self.nombre = nombre
        self.categoria = categoria

    def __str__(self):
        return f"Libro: {self.nombre}, Categoría: {self.categoria}"

    def to_dict(self): #parece igual al de arriba pero este es para la firebase
        return {"nombre": self.nombre, "categoria": self.categoria}

class Usuario:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

    def __str__(self):
        return f"Usuario: {self.nombre}, Código: {self.codigo}"

    def to_dict(self): #metodo para diccionario python
        return {"nombre": self.nombre, "codigo": self.codigo}

#MVVM

class BibliotecaViewModel:
    def __init__(self):
        self.biblioteca = Biblioteca()
        self.ref_libros = None
        self.ref_usuarios = None

        try:
            self.ref_libros = db.reference("biblioteca/libros")
            self.ref_usuarios = db.reference("biblioteca/usuarios")
        except:
            pass  # Modo local sin Firebase

    def registrar_libro(self, nombre_libro, categoria): #en estos metodos del VM es que guardamos la data
        libro = Libro(nombre_libro, categoria)
        self.biblioteca.actualizar_inventario(libro) 

        if self.ref_libros:
            self.ref_libros.push(libro.to_dict())

        print("\n Libro registrado con éxito.")
        self.biblioteca.mostrar_inventario()

    def registrar_usuario(self, nombre_usuario, codigo_usuario): #guardar data
        usuario = Usuario(nombre_usuario, codigo_usuario)
        self.biblioteca.agregar_usuario(usuario)

        if self.ref_usuarios:
            self.ref_usuarios.push(usuario.to_dict())

        print("\n Usuario registrado con éxito.")
        self.biblioteca.mostrar_usuarios()

class BibliotecaView:
    def __init__(self, viewmodel):
        self.viewmodel = viewmodel

    def mostrar_menu(self):
        print("\n *** Sistema de biblioteca ***") #Adicion de codigo huerfano a metodo de BibliotecaView
        while True:
            opcion = input(
                "\n--- Menú ---\n"
                "1. Registrar nuevo libro\n"
                "2. Registrar nuevo usuario\n"
                "3. Mostrar inventario de libros\n"
                "4. Mostrar lista de usuarios\n"
                "0. Salir\n"
                "Digite su opción: "
            )

            if opcion == "1":
                self.registro_libro()
            elif opcion == "2":
                self.registro_usuario()
            elif opcion == "3":
                self.viewmodel.biblioteca.mostrar_inventario()
            elif opcion == "4":
                self.viewmodel.biblioteca.mostrar_usuarios()
            elif opcion == "0":
                print(" Saliendo del sistema...")
                break
            else:
                print(" Opción inválida, intente de nuevo.")

    def registro_libro(self): #Este metodo UNICAMENTE se encarga de la interfaz de usuario
        categorias = ["suspenso", "aventura", "ficcion"]
        nombre_libro = input("\nIngrese el nombre del libro: ")
        opcion_categoria = input(
            "\nIngrese el género del libro:\n"
            "1. Suspenso\n"
            "2. Aventura\n"
            "3. Ficción\n"
            "Seleccione: "
        )

        if opcion_categoria in ["1", "2", "3"]:
            categoria = categorias[int(opcion_categoria) - 1]
        else:
            categoria = "N/A"
            print(f"\n Opción inválida, se asignará categoría ({categoria})")

        self.viewmodel.registrar_libro(nombre_libro, categoria) #el metodo invocado guarda la data

    def registro_usuario(self): #Este metodo UNICAMENTE se encarga de la interfaz de usuario
        print("\n--- Registro de nuevo usuario ---")
        nombre = input("Ingrese el nombre del usuario: ")
        codigo = input("Ingrese el código del estudiante: ")
        self.viewmodel.registrar_usuario(nombre, codigo) #el metodo invocado guarda la data

def main():
    viewmodel = BibliotecaViewModel() #mirame ese main con 3 lineas de codigo
    vista = BibliotecaView(viewmodel) #limpiesito como debe ser ajajajaja
    vista.mostrar_menu()

if __name__ == "__main__":
    main()
