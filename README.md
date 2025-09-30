# 📚 Parcial 1 - Programación Orientada a Objetos
**Autor:** Sebastian Triana  
**Curso:** POO  
**Caso de uso:** Biblioteca Universitaria  

---

## 📌 Descripción
Este proyecto implementa un **sistema básico de biblioteca** en Python, con las siguientes funcionalidades principales:
- Registro de nuevos **libros** con categorías.
- Registro de nuevos **usuarios** (pendiente de implementación).
- Inventario de libros que se muestra en consola.
- Menú interactivo para navegar entre opciones.

El programa fue desarrollado para el Parcial 1 de la materia de Programación Orientada a Objetos.

---

## ⚙️ Funcionalidades
- **Registro de libros**:  
  Permite ingresar el nombre y la categoría de un libro.  
  Categorías disponibles:  
  - Suspenso  
  - Aventura  
  - Ficción  
  - N/A (cuando la opción es inválida)  

- **Inventario**:  
  Los libros registrados se almacenan en el inventario y se muestran en pantalla con su nombre y categoría.  

- **Menú interactivo**:  
  - `1` → Registrar un nuevo libro  
  - `2` → Registrar un nuevo usuario (pendiente)  
  - `0` → Salir del sistema  

---

## 🖥️ Ejemplo de ejecución
```bash
 ***Sistema de biblioteca***

 --- Menu ---  
-para registro de nuevos LIBROS ingrese 1-  
-para registro de nuevos USUARIOS ingrese 2-  
-para salir ingrese 0-  
 Digite su opcion: 1

Ingrese el nombre del libro: El Hobbit

Ingrese el genero del libro de entre las opciones:  
 1 para suspenso  
 2 para aventura  
 3 para ficcion  
Digite su opcion: 2

Se le ha asignado el genero aventura a su libro

--- Inventario de libros ---
Libro: El Hobbit, Categoría: aventura
