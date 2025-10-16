from modelos.usuario import Usuario
from modelos.publicacion import Publicacion

def main():
    # Obtener usuarios existentes; si no hay ninguno, crear uno
    usuarios = Usuario.listar_todos()
    if not usuarios:
        print("No hay usuarios. Creando un usuario de prueba...")
        u = Usuario("Usuario Prueba", f"prueba_{__import__('time').time()}@example.com")
        u.guardar()
        usuarios = Usuario.listar_todos()

    usuario = usuarios[0]  # tomamos el primer usuario
    usuario_id = usuario['id']
    print(f"Usando usuario id={usuario_id}, nombre={usuario['nombre']}")

    # Crear una publicación
    contenido = "Esta es una publicación de prueba desde Python."
    pub = Publicacion(usuario_id, contenido)
    ok = pub.guardar()
    if ok:
        print(f"Publicación guardada correctamente. id={pub.id}")
    else:
        print("Fallo al guardar la publicación.")

    # Listar publicaciones del usuario
    publicaciones = Publicacion.listar_por_usuario(usuario_id)
    print("\nPublicaciones del usuario:")
    for p in publicaciones:
        print(p)

    # Listar todas las publicaciones
    todas = Publicacion.listar_todas()
    print("\nTodas las publicaciones (últimas primero):")
    for p in todas:
        print(p)

if __name__ == "__main__":
    main()
