from modelos.usuario import Usuario
from modelos.publicacion import Publicacion
from modelos.like import Like

def main():
    usuarios = Usuario.listar_todos()
    if len(usuarios) < 2:
        print("No hay suficientes usuarios, creando segundo usuario de prueba...")
        u2 = Usuario("Juan Gómez", "juan@example.com")
        u2.guardar()
        usuarios = Usuario.listar_todos()

    usuario1 = usuarios[0]  # autor
    usuario2 = usuarios[1]  # quien da like

    print(f"Usuario autor: {usuario1['nombre']} (id={usuario1['id']})")
    print(f"Usuario que da like: {usuario2['nombre']} (id={usuario2['id']})")

    publicaciones = Publicacion.listar_por_usuario(usuario1['id'])
    if not publicaciones:
        print("El autor no tiene publicaciones, creando una...")
        nueva_pub = Publicacion(usuario1['id'], "Publicación de prueba para like.")
        nueva_pub.guardar()
        publicaciones = Publicacion.listar_por_usuario(usuario1['id'])

    publicacion = publicaciones[0]
    print(f"Publicación seleccionada: id={publicacion['id']} -> {publicacion['contenido']}")

    like = Like(usuario2['id'], publicacion['id'])
    like.guardar()

    cantidad = Like.contar_por_publicacion(publicacion['id'])
    print(f"Número de likes en la publicación: {cantidad}")

    print("\nUsuarios que dieron like:")
    for u in Like.listar_por_publicacion(publicacion['id']):
        print(u)

if __name__ == "__main__":
    main()
