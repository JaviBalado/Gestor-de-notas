import notas.nota as modelo
import usuarios.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Acciones:

    def crear(self, usuario):
        print(f"De acuerdo {usuario[1]}, vamos a crear una nota")
        titulo = input("Introduce el título: ")
        descripcion = input("Introduce el contenido: ")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"\nLa nota '{nota.titulo}' se ha guardado con éxito")

        else:
            print(f"\nNo se ha podido guardar la nota. Prueba en otro momento")

    def mostrar(self, usuario):
        print("\n Estas son tus notas: ")

        nota = modelo.Nota(usuario[0])
        notas = nota.listar()

        for nota in notas:
            print("\n###############")
            print(f"Título: {nota[2]}")
            print(nota[3])
            print("###############")

    def eliminar(self, usuario):
        print(f"\n Vamos a borrar notas")
        titulo = input("¿Cuál es el título de la nota que quieres borrar? ")

        nota = modelo.Nota(usuario[0], titulo)
        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print("Se ha borrado la nota")

        else:
            print("No se ha podido borrar. Prueba en otro momento")