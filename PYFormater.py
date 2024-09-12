import os
import subprocess

def listar_unidades():
    # Listar unidades en el sistema
    unidades = []
    for letra in range(65, 91):  # de A a Z
        unidad = f"{chr(letra)}:\\"
        if os.path.exists(unidad) and unidad != "C:\\":
            unidades.append(unidad)
    return unidades

def formatear_disco(disco):
    # Formatear el disco seleccionado
    confirmacion = input(f"¿Estás seguro de que quieres formatear {disco}? (s/n): ")
    if confirmacion.lower() == 's':
        try:
            # Ejecutar el comando de formateo
            subprocess.run(['format', disco, '/fs:NTFS', '/q', '/y'], check=True)
            print(f"{disco} formateado exitosamente.")
        except subprocess.CalledProcessError:
            print("Error al formatear el disco.")
    else:
        print("Formateo cancelado.")

def main():
    print("Unidades de almacenamiento conectadas (ignorando el disco C):")
    unidades = listar_unidades()
    
    if not unidades:
        print("No se encontraron unidades disponibles.")
        return

    for i, unidad in enumerate(unidades):
        print(f"{i + 1}: {unidad}")

    seleccion = int(input("Selecciona el número del disco que deseas formatear: ")) - 1

    if 0 <= seleccion < len(unidades):
        formatear_disco(unidades[seleccion])
    else:
        print("Selección no válida.")

if __name__ == "__main__":
    main()
