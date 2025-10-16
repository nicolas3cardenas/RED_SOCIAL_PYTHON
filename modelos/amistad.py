from config.conexion import Conexion

class Amistad:
    def __init__(self, usuario_id_1, usuario_id_2):
        self.usuario_id_1 = usuario_id_1
        self.usuario_id_2 = usuario_id_2

    def guardar(self):
        """Crea una relación de amistad entre dos usuarios."""
        if self.usuario_id_1 == self.usuario_id_2:
            print("No puedes ser amigo de ti mismo.")
            return False

        # Ordenar IDs para evitar duplicados invertidos
        uid1, uid2 = sorted([self.usuario_id_1, self.usuario_id_2])

        conn = Conexion().conectar()
        cursor = conn.cursor()
        try:
            sql = "INSERT INTO amistad (usuario_id_1, usuario_id_2) VALUES (%s, %s)"
            cursor.execute(sql, (uid1, uid2))
            conn.commit()
            print(f"Amistad creada entre usuarios {uid1} y {uid2}.")
            return True
        except Exception as e:
            if "Duplicate entry" in str(e):
                print("Estos usuarios ya son amigos.")
            else:
                print("Error al crear la amistad:", e)
            return False
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def listar_amigos(usuario_id):
        """Devuelve la lista de amigos de un usuario."""
        conn = Conexion().conectar()
        cursor = conn.cursor(dictionary=True)
        sql = """
            SELECT u.id, u.nombre, u.correo
            FROM usuario u
            JOIN amistad a 
                ON (u.id = a.usuario_id_1 OR u.id = a.usuario_id_2)
            WHERE (%s IN (a.usuario_id_1, a.usuario_id_2)) 
              AND u.id != %s
        """
        cursor.execute(sql, (usuario_id, usuario_id))
        amigos = cursor.fetchall()
        cursor.close()
        conn.close()
        return amigos
