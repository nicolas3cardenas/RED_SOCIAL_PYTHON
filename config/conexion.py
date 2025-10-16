import mysql.connector
from mysql.connector import Error

class Conexion:
    def __init__(self):
        self.conn = None

    def conectar(self):
        try:
            self.conn = mysql.connector.connect(
                host="127.0.0.1",
                user="root",           # usuario por defecto de Wamp
                password="",           # deja vacío si tu root no tiene clave
                database="red_social"  # nombre de la base en phpMyAdmin
            )
            return self.conn
        except Error as err:
            print(f"❌ Error de conexión: {err}")
            return None

    def cerrar(self):
        if self.conn and self.conn.is_connected():
            self.conn.close()
