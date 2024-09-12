import pandas as pd
import os

# Nombre del archivo de Excel
archivo_excel = 'tareas.xlsx'

# Inicializa la lista de tareas
todo_list = []

# Cargar tareas desde el archivo Excel si existe
if os.path.exists(archivo_excel):
    df = pd.read_excel(archivo_excel)
    todo_list = df['Tareas'].tolist()

def guardar_tareas():
    df = pd.DataFrame(todo_list, columns=['Tareas'])
    df.to_excel(archivo_excel, index=False)

def agregar_tarea(tarea):
    todo_list.append(tarea)
    print(f"Tarea '{tarea}' agregada.")
    guardar_tareas()

def mostrar_tareas():
    print("Lista de Tareas:")
    if not todo_list:
        print("No hay tareas en la lista.")
    else:
        for index, tarea in enumerate(todo_list, start=1):
            print(f"{index}. {tarea}")

def eliminar_tarea(indice):
    if 0 <= indice < len(todo_list):
        tarea_eliminada = todo_list.pop(indice)
        print(f"Tarea '{tarea_eliminada}' eliminada.")
        guardar_tareas()
    else:
        print("Índice no válido.")

# Bucle principal para interactuar con el usuario
while True:
    print("\nOpciones:")
    print("1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Eliminar tarea")
    print("4. Salir")

    opcion = input("Selecciona una opción (1-4): ")

    if opcion == '1':
        tarea = input("Ingresa la tarea que deseas agregar: ")
        agregar_tarea(tarea)
    elif opcion == '2':
        mostrar_tareas()
    elif opcion == '3':
        mostrar_tareas()
        indice = int(input("Ingresa el número de la tarea que deseas eliminar: ")) - 1
        eliminar_tarea(indice)
    elif opcion == '4':
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción entre 1 y 4.")