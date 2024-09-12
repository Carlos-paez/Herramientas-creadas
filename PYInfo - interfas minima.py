import platform
import psutil
import tkinter as tk

def mostrar_informacion_sistema(ventana):
    """Muestra la información del sistema en la ventana."""
    label_sistema = tk.Label(ventana, text=f"Sistema Operativo: {platform.system()}")
    label_sistema.pack()
    label_nodo = tk.Label(ventana, text=f"Nombre del Nodo: {platform.node()}")
    label_nodo.pack()
    # ... (agrega más etiquetas para otros datos del sistema)

def mostrar_informacion_hardware(ventana):
    """Muestra la información del hardware en la ventana."""
    label_cpu = tk.Label(ventana, text=f"Núcleos Lógicos: {psutil.cpu_count(logical=True)}")
    label_cpu.pack()
    label_ram = tk.Label(ventana, text=f"RAM Total: {psutil.virtual_memory().total / (1024 ** 3):.2f} GB")
    label_ram.pack()
    # ... (agrega más etiquetas para otros datos del hardware)

def main():
    """Crea la ventana principal y los botones."""
    ventana = tk.Tk()
    ventana.title("Información del Sistema")

    boton_sistema = tk.Button(ventana, text="Información del Sistema", command=lambda: mostrar_informacion_sistema(ventana))
    boton_sistema.pack()

    boton_hardware = tk.Button(ventana, text="Información de Hardware", command=lambda: mostrar_informacion_hardware(ventana))
    boton_hardware.pack()

    ventana.mainloop()

if __name__ == "__main__":
    main()