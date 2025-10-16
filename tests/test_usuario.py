from modelos.usuario import Usuario

def main():
    # Crear un nuevo usuario
    u = Usuario("Ana Pérez", "ana@example.com")
    u.guardar()

    # Listar todos los usuarios registrados
    usuarios = Usuario.listar_todos()
    print("\n👥 Usuarios registrados:")
    for usr in usuarios:
        print(usr)

if __name__ == "__main__":
    main()
