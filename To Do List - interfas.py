import tkinter as tk
from tkinter import messagebox
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

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Tareas")

# Crear los elementos de la interfaz
etiqueta_tarea = tk.Label(ventana, text="Nueva tarea:")
entrada_tarea = tk.Entry(ventana)
boton_agregar = tk.Button(ventana, text="Agregar", command=lambda: agregar_tarea(entrada_tarea.get()))
lista_tareas = tk.Listbox(ventana)
boton_eliminar = tk.Button(ventana, text="Eliminar", command=lambda: eliminar_tarea(lista_tareas.curselection()))
boton_marcar = tk.Button(ventana, text="Marcar como completada", command=lambda: marcar_como_completada())

# Función para actualizar la lista de tareas en la interfaz
def actualizar_lista():
    lista_tareas.delete(0, tk.END)
    for tarea in todo_list:
        lista_tareas.insert(tk.END, tarea)

# Función para agregar una tarea
def agregar_tarea(tarea):
    if tarea:
        todo_list.append(tarea)
        actualizar_lista()
        messagebox.showinfo("Tarea agregada", "La tarea se ha agregado correctamente.")
        guardar_tareas()
    else:
        messagebox.showwarning("Error", "Debes ingresar una tarea.")

# Función para eliminar una tarea
def eliminar_tarea(indice):
    if indice:
        indice = indice[0]  # Obtener el índice seleccionado
        tarea_eliminada = todo_list.pop(indice)
        actualizar_lista()
        messagebox.showinfo("Tarea eliminada", f"La tarea '{tarea_eliminada}' se ha eliminado.")
        guardar_tareas()
    else:
        messagebox.showwarning("Error", "Debes seleccionar una tarea para eliminar.")

# Función para marcar una tarea como completada
def marcar_como_completada():
    indice = lista_tareas.curselection()
    if indice:
        indice = indice[0]
        tarea_completada = todo_list.pop(indice)
        todo_list.append(f"✅ {tarea_completada}")
        actualizar_lista()
        guardar_tareas()

# ... (tus funciones guardar_tareas y mostrar_tareas)

# Empaquetar los elementos en la ventana
etiqueta_tarea.pack()
entrada_tarea.pack()
boton_agregar.pack()
lista_tareas.pack()
boton_eliminar.pack()
boton_marcar.pack()

# Actualizar la lista al iniciar la aplicación
actualizar_lista()

# Iniciar el bucle principal de Tkinter
ventana.mainloop()