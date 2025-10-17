#  Parcial 1 - Programación Orientada a Objetos  
**Autor:** Sebastian Triana  
**Curso:** POO  
**Caso de uso:** Biblioteca Universitaria  
**Base de datos:** Firebase Realtime Database  

---

##  Descripción  
Este proyecto corrige la version 1 de un **sistema de gestión de biblioteca universitaria** en Python, corregido bajo el **patrón de arquitectura MVVM (Model–View–ViewModel)**.  
El sistema permite registrar libros y ahora tambien usuarios usuarios, almacenando la información tanto localmente como en una base de datos **Firebase Realtime Database**.  

Este repositorio fue desarrollado como **Parcial 1** para la asignatura **Programación Orientada a Objetos (POO)**.  

---

##  Funcionalidades  

###  Registro de Libros  
- Permite registrar nuevos libros con nombre y categoría.  
- Las categorías disponibles son:  
  - Suspenso  
  - Aventura  
  - Ficción  
  - N/A (asignada cuando la opción es inválida)  
- Cada libro se guarda tanto localmente en el inventario como en Firebase.  

###  Registro de Usuarios (Esta funcion se agrego por la actividad opcional)
- Permite registrar usuarios ingresando su nombre y código de estudiante.  
- Los datos se almacenan localmente y en Firebase.  

###  Visualización  
- Mostrar todos los libros registrados.  
- Mostrar la lista completa de usuarios registrados.  

###  Menú interactivo  
El sistema ofrece un menú en consola para facilitar la navegación:  
<img width="276" height="145" alt="image" src="https://github.com/user-attachments/assets/08d9db4c-05a8-4e53-b55c-fa9da149d826" />

---

##  Arquitectura MVVM  

El proyecto está estructurado según el patrón **MVVM**, separando responsabilidades de forma clara:  

| Capa | Clase | Responsabilidad |
|------|--------|-----------------|
| **Model** | `Libro`, `Usuario`, `Biblioteca` | Representan los datos y su estructura interna. |
| **ViewModel** | `BibliotecaViewModel` | Contiene la lógica de negocio y conexión con Firebase. |
| **View** | `BibliotecaView` | Interactúa con el usuario, muestra menús y recopila datos. |

Esta arquitectura vista en clase mejora la organización, escalabilidad y mantenibilidad del código.  

---

##  Integración con Firebase  

El sistema utiliza **Firebase Realtime Database** para el almacenamiento remoto.  
La conexión se realiza con las siguientes líneas de código:  

```python
cred = credentials.Certificate("ruta/al/archivo/nube_firebase.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://proyecto-firebase-48337-default-rtdb.firebaseio.com/"
})
```

Las referencias a la base de datos son gestionadas desde el **ViewModel**:  
```python
self.ref_libros = db.reference("biblioteca/libros")
self.ref_usuarios = db.reference("biblioteca/usuarios")
```

Cada registro se sube automáticamente mediante:
```python
self.ref_libros.push(libro.to_dict())
self.ref_usuarios.push(usuario.to_dict())
```

La informacion finalmente llega a la realtime database donde se puede observar:
<img width="472" height="457" alt="image" src="https://github.com/user-attachments/assets/db678df5-c819-46ef-a6a9-28be68e62567" />


---

##  Conceptos aplicados
- Programación Orientada a Objetos (POO)  
- Encapsulamiento y reutilización de clases  
- Patrón de diseño **MVVM**  
- Conexión con **Firebase Realtime Database**  
- Separación entre lógica, modelo y vista  
- Control de flujo mediante menú interactivo  

---

##  Autor  
**Sebastian Triana**  
Estudiante de Ingeniería de Sistemas y Computación  
Universidad Nacional de Colombia  

---

##  Ejemplos de ejecución  
- <img width="384" height="356" alt="image" src="https://github.com/user-attachments/assets/06849c98-a9e0-432a-a193-9dfa8e87ada2" /> 

- <img width="372" height="286" alt="image" src="https://github.com/user-attachments/assets/92bdf6e6-3931-4fc8-9974-8c87e92d28e7" />

- <img width="356" height="191" alt="image" src="https://github.com/user-attachments/assets/441fdd75-22d1-4cf1-8cdc-d98cc68695b7" />

- <img width="349" height="180" alt="image" src="https://github.com/user-attachments/assets/dec6df7f-00da-44d0-84cf-77e67735437a" />

- <img width="472" height="457" alt="image" src="https://github.com/user-attachments/assets/788a7a52-facb-4609-9915-2ffb20773daf" />
