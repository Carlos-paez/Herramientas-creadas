import sqlite3

# Conectar a la base de datos (se creará si no existe)
conn = sqlite3.connect('historial_cuenta.db')
cursor = conn.cursor()

# Crear la tabla si no existe
cursor.execute('''
CREATE TABLE IF NOT EXISTS movimientos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo_movimiento TEXT,
    monto REAL,
    nuevo_saldo REAL
)
''')

# Verificar si ya existe un Monto_Base en la base de datos
cursor.execute("SELECT nuevo_saldo FROM movimientos ORDER BY id DESC LIMIT 1")
resultado = cursor.fetchone()

if resultado:
    monto_base = resultado[0]
    print(f"El Monto Base actual en la cuenta es: {monto_base} Bolivares")
else:
    monto_base = float(input("Ingrese el monto base de la cuenta en Bolivares:\n"))
    cursor.execute("INSERT INTO movimientos (tipo_movimiento, monto, nuevo_saldo) VALUES (?, ?, ?)",
                   ("Inicial", monto_base, monto_base))  # Registrar el monto inicial

def vaciar_base_datos():
    cursor.execute("DELETE FROM movimientos")  # Vaciar la tabla
    conn.commit()
    print("La base de datos ha sido vaciada. Puedes empezar desde cero.")

    def resetear_base_datos():
    cursor.execute("df.reset_index(drop=False, inplace=False) FROM movimientos")  # Vaciar la tabla
    conn.commit()
    print("La base de datos ha sido vaciada. Puedes empezar desde cero.")

while True:
    opcion = str(input(
        "Ingrese qué acción desea realizar:\n"
        "1. Dividir el Monto Base de la cuenta\n"
        "2. Calcular un egreso de la cuenta\n"
        "3. Adicionar un ingreso al total de la cuenta\n"
        "4. Vaciar la base de datos\n"
        "5. Salir\n"
    ))

    if opcion.title() == "Dividir":
        Ahorro = monto_base * 0.40
        Necesidades = monto_base * 0.40
        gastos = monto_base * 0.20
        print(f"El resultado sería el siguiente:\n"
              f"Ahorrar: {Ahorro}\n"
              f"Primera Necesidad: {Necesidades}\n"
              f"Gastos personales: {gastos}\n\n\n")

    elif opcion.title() == "Egresar":
        Descontar = float(input("Ingrese el monto a descontar de la cuenta: \n"))
        monto_base -= Descontar
        print(f"El monto total actual en la cuenta es: {monto_base}\n\n\n")
        cursor.execute("INSERT INTO movimientos (tipo_movimiento, monto, nuevo_saldo) VALUES (?, ?, ?)",
                       ("Egreso", Descontar, monto_base))  # Registrar en SQLite

    elif opcion.title() == "Ingresar":
        Ingreso = float(input("Ingrese el monto que va a ingresar: \n"))
        monto_base += Ingreso
        print(f"El monto total actual en la cuenta es: {monto_base}\n\n\n")
        cursor.execute("INSERT INTO movimientos (tipo_movimiento, monto, nuevo_saldo) VALUES (?, ?, ?)",
                       ("Ingreso", Ingreso, monto_base))  # Registrar en SQLite

    elif opcion.title() == "Vaciar":
        vaciar_base_datos()
        # Reiniciar el monto_base a 0 después de vaciar la base de datos
        monto_base = 0

    elif opcion.title() == "Salir":
        break

    else:
        print("Esa no es una acción válida en este sistema")

    # Guardar los cambios en la base de datos
    conn.commit()

# Cerrar la conexión al final del programa
conn.close()

