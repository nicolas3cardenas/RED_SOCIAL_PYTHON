#  Red Social - Proyecto de Programación Orientada a Objetos (Python + MySQL)

##  Descripción General
Este proyecto implementa una **red social básica** desarrollada en **Python**, aplicando los principios de **Programación Orientada a Objetos (POO)**.  
El sistema se conecta a una base de datos **MySQL** y permite realizar operaciones típicas de una red social, como:

- Registrar usuarios con nombre y correo electrónico.  
- Crear publicaciones con fecha y contenido.  
- Dar “me gusta” (likes) a publicaciones.  
- Registrar relaciones de amistad entre usuarios.  

El proyecto fue desarrollado y probado en **Visual Studio Code**, utilizando **WampServer** como entorno local de base de datos.

---

##  Tecnologías Utilizadas
- **Lenguaje:** Python 3.14  
- **Base de datos:** MySQL (administrada con phpMyAdmin)  
- **Servidor local:** WampServer  
- **Paradigma:** Programación Orientada a Objetos (POO)  
- **Librerías externas:**
  - `mysql-connector-python` → para conectar Python con MySQL  
  - `prettytable` → para mostrar tablas con formato en consola

---

##  Estructura del Proyecto

```bash
red_social_python/
├── config/
│   └── conexion.py              # Clase para manejar la conexión con MySQL
├── modelos/
│   ├── usuario.py               # Clase Usuario
│   ├── publicacion.py           # Clase Publicacion
│   ├── like.py                  # Clase Like (gestiona los "me gusta")
│   └── amistad.py               # Clase Amistad (gestiona relaciones)
├── tests/
│   ├── test_conexion.py         # Prueba de conexión con la base de datos
│   ├── test_usuario.py          # Pruebas CRUD de usuarios
│   ├── test_publicacion.py      # Pruebas de publicaciones
│   ├── test_like.py             # Pruebas de likes
│   └── test_amistad.py          # Pruebas de amistad
├── sql/
│   ├── ddl_red_social.sql       # Definición de tablas (estructura de BD)
│   └── dml_red_social.sql       # Datos iniciales para pruebas
├── main.py                      # Menú principal de la aplicación
└── README.md                    # Documentación del proyecto
