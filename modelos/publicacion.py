from config.conexion import Conexion

class Publicacion:
    def __init__(self, usuario_id, contenido):
        self.usuario_id = usuario_id
        self.contenido = contenido
        self.id = None
        self.fecha = None

    def guardar(self):
        conn = Conexion().conectar()
        if not conn:
            print("Error: no hay conexión a la BD.")
            return False
        cursor = conn.cursor()
        try:
            sql = "INSERT INTO publicacion (usuario_id, contenido) VALUES (%s, %s)"
            cursor.execute(sql, (self.usuario_id, self.contenido))
            conn.commit()
            self.id = cursor.lastrowid
            # obtener fecha desde la BD si se necesita
            cursor.execute("SELECT fecha FROM publicacion WHERE id = %s", (self.id,))
            row = cursor.fetchone()
            if row:
                # mysql-connector devuelve tupla; la fecha suele estar en row[0]
                self.fecha = row[0]
            return True
        except Exception as e:
            print("Error al guardar publicación:", e)
            return False
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def listar_por_usuario(usuario_id):
        conn = Conexion().conectar()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute("SELECT p.id, p.usuario_id, p.contenido, p.fecha, u.nombre "
                           "FROM publicacion p JOIN usuario u ON p.usuario_id = u.id "
                           "WHERE p.usuario_id = %s ORDER BY p.fecha DESC", (usuario_id,))
            filas = cursor.fetchall()
            return filas
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def listar_todas():
        conn = Conexion().conectar()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute("SELECT p.id, p.usuario_id, p.contenido, p.fecha, u.nombre "
                           "FROM publicacion p JOIN usuario u ON p.usuario_id = u.id "
                           "ORDER BY p.fecha DESC")
            filas = cursor.fetchall()
            return filas
        finally:
            cursor.close()
            conn.close()
