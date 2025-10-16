from modelos.usuario import Usuario
from modelos.amistad import Amistad

def main():
    usuarios = Usuario.listar_todos()
    if len(usuarios) < 2:
        print("Se necesitan al menos dos usuarios para crear amistad.")
        return

    u1 = usuarios[0]
    u2 = usuarios[1]

    print(f"Intentando crear amistad entre {u1['nombre']} (id={u1['id']}) y {u2['nombre']} (id={u2['id']})")

    amistad = Amistad(u1['id'], u2['id'])
    amistad.guardar()

    print(f"\nAmigos de {u1['nombre']}:")
    amigos1 = Amistad.listar_amigos(u1['id'])
    for a in amigos1:
        print(a)

    print(f"\nAmigos de {u2['nombre']}:")
    amigos2 = Amistad.listar_amigos(u2['id'])
    for a in amigos2:
        print(a)

if __name__ == "__main__":
    main()
