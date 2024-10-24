import sqlite3
from tkinter import *
from datetime import datetime

# Conectar a la base de datos (o crearla si no existe)
conexion = sqlite3.connect('inspecciones.db')
cursor = conexion.cursor()

# Crear la tabla si no existe
cursor.execute('''
CREATE TABLE IF NOT EXISTS inspecciones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha_hora TEXT,
    temperatura REAL,
    humedad REAL,
    nivel_agua TEXT,
    cantidad_lamparas INTEGER,
    cantidad_extintores INTEGER,
    responsable TEXT
)
''')
conexion.commit()

# Crear la ventana principal
ventana = Tk()
ventana.title("Registro de Inspecciones")

# Crear los elementos de la interfaz
label_temperatura = Label(ventana, text="Temperatura (°C):")
label_temperatura.pack()
entry_temperatura = Entry(ventana)
entry_temperatura.pack()

label_humedad = Label(ventana, text="Humedad (%):")
label_humedad.pack()
entry_humedad = Entry(ventana)
entry_humedad.pack()

label_nivel_agua = Label(ventana, text="Nivel de Agua (m):")
label_nivel_agua.pack()
entry_nivel_agua = Entry(ventana)
entry_nivel_agua.pack()

label_cantidad_lamparas = Label(ventana, text="Cantidad de Lámparas:")
label_cantidad_lamparas.pack()
entry_cantidad_lamparas = Entry(ventana)
entry_cantidad_lamparas.pack()

label_cantidad_extintores = Label(ventana, text="Cantidad de Extintores:")
label_cantidad_extintores.pack()
entry_cantidad_extintores = Entry(ventana)
entry_cantidad_extintores.pack()

label_responsable = Label(ventana, text="Responsable de la Revisión:")
label_responsable.pack()
entry_responsable = Entry(ventana)
entry_responsable.pack()

# Label para mostrar mensajes de error
label_error = Label(ventana, text="", fg="red")
label_error.pack()

# Función para validar el tipo de dato
def validar_dato(entry, tipo):
    try:
        if tipo == 'float':
            return float(entry)
        elif tipo == 'int':
            return int(entry)
        elif tipo == 'str':
            return str(entry)
        else:
            return str(entry)
    except ValueError:
        return None

# Función para registrar nuevos datos
def registrar_datos():
    global label_error
    label_error.config(text="")  # Limpiar mensajes de error

    temperatura = validar_dato(entry_temperatura.get(), 'float')
    humedad = validar_dato(entry_humedad.get(), 'str')
    nivel_agua = validar_dato(entry_nivel_agua.get(), 'str')
    cantidad_lamparas = validar_dato(entry_cantidad_lamparas.get(), 'int')
    cantidad_extintores = validar_dato(entry_cantidad_extintores.get(), 'int')
    responsable = entry_responsable.get()

    # Validar si hay errores en los datos
    if temperatura is None:
        label_error.config(text="Error: Temperatura debe ser un número.")
        return
    if humedad is None:
        label_error.config(text="Error: Humedad debe ser un número.")
        return
    if nivel_agua is None:
        label_error.config(text="Error: Nivel de Agua debe ser un texto válido.")
        return
    if cantidad_lamparas is None:
        label_error.config(text="Error: Cantidad de Lámparas debe ser un número entero.")
        return
    if cantidad_extintores is None:
        label_error.config(text="Error: Cantidad de Extintores debe ser un número entero.")
        return

    # Obtener la fecha y hora actual
    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Insertar los datos en la base de datos
    cursor.execute('''
    INSERT INTO inspecciones (fecha_hora, temperatura, humedad, nivel_agua, cantidad_lamparas, cantidad_extintores, responsable) 
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (fecha_hora, temperatura, humedad, nivel_agua, cantidad_lamparas, cantidad_extintores, responsable))
    conexion.commit()

    # Limpiar los campos de entrada
    entry_temperatura.delete(0, END)
    entry_humedad.delete(0, END)
    entry_nivel_agua.delete(0, END)
    entry_cantidad_lamparas.delete(0, END)
    entry_cantidad_extintores.delete(0, END)
    entry_responsable.delete(0, END)

# Función para mostrar todos los registros
def mostrar_registros():
    # Consultar la base de datos
    cursor.execute('SELECT * FROM inspecciones')
    registros = cursor.fetchall()

    # Crear una nueva ventana para mostrar los resultados
    ventana_registros = Toplevel(ventana)
    ventana_registros.title("Registros de Inspecciones")

    # Mostrar los resultados en un widget de texto
    texto = Text(ventana_registros)
    for registro in registros:
        texto.insert(END, f"ID: {registro[0]}, Fecha y Hora: {registro[1]}, Temperatura: {registro[2]}, Humedad: {registro[3]}, Nivel de Agua: {registro[4]}, Lámparas: {registro[5]}, Extintores: {registro[6]}, Responsable: {registro[7]}\n")
    texto.pack()

# Función para limpiar la base de datos
def limpiar_base_datos():
    def verificar_credenciales():
        usuario = entry_usuario.get()
        contrasena = entry_contrasena.get()
        
        if usuario == "admin" and contrasena == "conver":
            cursor.execute('DELETE FROM inspecciones')  # Limpiar la tabla
            conexion.commit()
            label_error.config(text="Base de datos limpiada exitosamente.")
            ventana_credenciales.destroy()  # Cerrar ventana de credenciales
        else:
            label_error.config(text="Credenciales incorrectas. Intente de nuevo.")

    # Crear ventana para ingresar credenciales
    ventana_credenciales = Toplevel(ventana)
    ventana_credenciales.title("Credenciales de Administrador")

    label_usuario = Label(ventana_credenciales, text="Usuario:")
    label_usuario.pack()
    entry_usuario = Entry(ventana_credenciales)
    entry_usuario.pack()

    label_contrasena = Label(ventana_credenciales, text="Contraseña:")
    label_contrasena.pack()
    entry_contrasena = Entry(ventana_credenciales, show="*")
    entry_contrasena.pack()

    boton_verificar = Button(ventana_credenciales, text="Verificar", command=verificar_credenciales)
    boton_verificar.pack()

# Crear los botones y asociarlos a las funciones
boton_registrar = Button(ventana, text="Registrar", command=registrar_datos)
boton_registrar.pack()

boton_mostrar = Button(ventana, text="Mostrar Registros", command=mostrar_registros)
boton_mostrar.pack()

boton_limpiar = Button(ventana, text="Limpiar Base de Datos", command=limpiar_base_datos)
boton_limpiar.pack()

# Empaquetar los elementos en la ventana
ventana.mainloop()

# Cerrar la conexión a la base de datos al finalizar
conexion.close()
