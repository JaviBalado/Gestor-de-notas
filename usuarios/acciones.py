import usuarios.usuario as modelo
import notas.acciones


class Acciones:

    def registro(self):
        print("\nVamos a registrarte en el sistema.")
        nombre = input("¿Cuál es tu nombre?: ")
        apellidos = input("¿Cuáles son tus apellidos?: ")
        email = input("¿Cuál es tu email?: ")
        password = input("¿Cuál es tu contraseña?: ")

        usuario = modelo.Usuario(nombre,apellidos, email,password)
        registro= usuario.registrar()

        if registro[0] >= 1:
            print(f"Enhorabuena, {registro[1].nombre} te has registrado correctamente")
        else:
            print("Disculpa, ha habido un error")

    def login (self):
        print("\nVamos a iniciar sesión.")
        try: 
            email = input("¿Cuál es tu email?: ")
            password = input("¿Cuál es tu contraseña?: ")

            usuario = modelo.Usuario('', '', email, password)
            login = usuario.identificar()

            if email == login[3]:
                print(f"\nBienvenido {login[1]} ")
                self.proximasAcciones(login)
 
        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print("Login incorrecto")

    def proximasAcciones(self,usuario):
        print(f"""
            Acciones disponibles:
            - Crear nota (crear)
            - Mostrar tus notas (mostrar)
            - Eliminar nota (eliminar)
            - Salir (salir)
        """)

        accion = input("¿Qué quieres hacer? ")
        accion = accion.lower()
        hazEl = notas.acciones.Acciones()

        if accion == "crear":
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)

        elif accion == "mostrar":
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "eliminar":
            hazEl.eliminar(usuario)
            self.proximasAcciones(usuario)
            
        if accion == "salir":
            print(f"¡Hasta la próxima {usuario[1]}!")
            exit()
