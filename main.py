"""
Proyecto Python Mysql: 
- Abrir asistente
- login o registro
- si elegimos registro creará un usuarip en la bbdd
- si elegimos login, identificará al usuario y nos preguntará
- Opciones de usuario: Crear notas, mostrar notas y borrar notas
"""
from usuarios import acciones

print("""
    Acciones disponibles:
         - Registro
         - Login
""")

hazEl = acciones.Acciones()
accion = input("¿Qué quieres hacer?: ")

accion = accion.lower()

if accion == "registro":
    hazEl.registro()

elif accion == "login":
    hazEl.login()
     