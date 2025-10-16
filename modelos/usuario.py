from config.conexion import Conexion

class Usuario:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo

    def guardar(self):
        """Guarda un nuevo usuario en la base de datos"""
        conn = Conexion().conectar()
        if not conn:
            print("❌ No hay conexión a la BD.")
            return False
        cursor = conn.cursor()
        try:
            sql = "INSERT INTO usuario (nombre, correo) VALUES (%s, %s)"
            cursor.execute(sql, (self.nombre, self.correo))
            conn.commit()
            print(f"✅ Usuario '{self.nombre}' registrado correctamente.")
            return True
        except Exception as e:
            print("❌ Error al guardar usuario:", e)
            return False
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def listar_todos():
        """Devuelve todos los usuarios registrados"""
        conn = Conexion().conectar()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuario ORDER BY id ASC")
        resultados = cursor.fetchall()
        cursor.close()
        conn.close()
        return resultados
