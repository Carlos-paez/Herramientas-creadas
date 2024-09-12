import platform
import psutil

def mostrar_informacion_sistema():
    print("Información del sistema:")
    print(f"Nombre del sistema: {platform.system()}")
    print(f"Nombre del nodo: {platform.node()}")
    print(f"Versión del sistema operativo: {platform.version()}")
    print(f"Versión de Python: {platform.python_version()}")
    print(f"Arquitectura: {platform.architecture()}")
    print(f"Procesador: {platform.processor()}")
    print(f"Máquina: {platform.machine()}")
    print(f"Distribución: {platform.platform()}")

def mostrar_informacion_hardware():
    print("\nInformación de hardware:")
    print(f"CPU: {psutil.cpu_count(logical=True)} núcleos lógicos")
    print(f"RAM total: {psutil.virtual_memory().total / (1024 ** 3):.2f} GB")
    print(f"Uso de RAM: {psutil.virtual_memory().percent}%")
    print(f"Discos: {[disk.device for disk in psutil.disk_partitions()]}")

def main():
    mostrar_informacion_sistema()
    mostrar_informacion_hardware()

if __name__ == "__main__":
    main()



pausa=str(input("."))