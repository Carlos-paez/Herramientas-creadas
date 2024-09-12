import platform
import psutil
import tkinter as tk

def mostrar_informacion_completa(ventana):
    """Muestra toda la información disponible del sistema en la ventana."""

    # Información del sistema operativo
    sistema_operativo = tk.Label(ventana, text=f"Sistema Operativo: {platform.system()}")
    sistema_operativo.pack()
    version_so = tk.Label(ventana, text=f"Versión: {platform.version()}")
    version_so.pack()
    nodo = tk.Label(ventana, text=f"Nombre del Nodo: {platform.node()}")
    nodo.pack()
    procesador = tk.Label(ventana, text=f"Procesador: {platform.processor()}")
    procesador.pack()
    arquitectura = tk.Label(ventana, text=f"Arquitectura: {platform.architecture()}")
    arquitectura.pack()
    distribucion = tk.Label(ventana, text=f"Distribución: {platform.platform()}")
    distribucion.pack()

    # Información de hardware
    hardware = tk.Label(ventana, text="Información de Hardware:")
    hardware.pack()
    cpu = tk.Label(ventana, text=f"CPU: {psutil.cpu_count(logical=True)} núcleos lógicos")
    cpu.pack()
    ram_total = tk.Label(ventana, text=f"RAM Total: {psutil.virtual_memory().total / (1024 ** 3):.2f} GB")
    ram_total.pack()
    ram_usada = tk.Label(ventana, text=f"RAM Usada: {psutil.virtual_memory().used / (1024 ** 3):.2f} GB")
    ram_usada.pack()
    discos = tk.Label(ventana, text="Discos:")
    discos.pack()
    for disco in psutil.disk_partitions():
        disco_info = tk.Label(ventana, text=f"  - {disco.device}: {disco.mountpoint}")
        disco_info.pack()
    # Agrega más información de hardware según tus necesidades (por ejemplo, uso de disco, temperatura, etc.)

def main():
    ventana = tk.Tk()
    ventana.title("Información Completa del Sistema")

    boton_info = tk.Button(ventana, text="Mostrar Información", command=lambda: mostrar_informacion_completa(ventana))
    boton_info.pack()

    ventana.mainloop()

if __name__ == "__main__":
    main()