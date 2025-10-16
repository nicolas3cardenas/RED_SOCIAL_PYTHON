from config.conexion import Conexion

class Like:
    def __init__(self, usuario_id, publicacion_id):
        self.usuario_id = usuario_id
        self.publicacion_id = publicacion_id

    def guardar(self):
        """Agrega un 'me gusta' si no existe ya."""
        conn = Conexion().conectar()
        cursor = conn.cursor()
        try:
            sql = "INSERT INTO likes (usuario_id, publicacion_id) VALUES (%s, %s)"
            cursor.execute(sql, (self.usuario_id, self.publicacion_id))
            conn.commit()
            print(f"Like agregado: usuario {self.usuario_id} -> publicación {self.publicacion_id}")
            return True
        except Exception as e:
            print("Error al registrar el like:", e)
            return False
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def contar_por_publicacion(publicacion_id):
        """Cuenta cuántos 'me gusta' tiene una publicación."""
        conn = Conexion().conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM likes WHERE publicacion_id = %s", (publicacion_id,))
        cantidad = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        return cantidad

    @staticmethod
    def listar_por_publicacion(publicacion_id):
        """Devuelve la lista de usuarios que dieron like."""
        conn = Conexion().conectar()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            "SELECT u.id, u.nombre, u.correo "
            "FROM likes l JOIN usuario u ON l.usuario_id = u.id "
            "WHERE l.publicacion_id = %s",
            (publicacion_id,)
        )
        resultados = cursor.fetchall()
        cursor.close()
        conn.close()
        return resultados
