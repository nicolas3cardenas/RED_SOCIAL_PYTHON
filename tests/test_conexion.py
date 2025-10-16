from config.conexion import Conexion

def main():
    db = Conexion()
    conn = db.conectar()
    if conn:
        print("✅ Conexión exitosa con la base de datos 'red_social'.")
        db.cerrar()
    else:
        print("❌ Error al conectar con la base de datos.")

if __name__ == "__main__":
    main()
