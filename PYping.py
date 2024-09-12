import subprocess
import time
import winsound  # Módulo para reproducir sonidos en Windows
import datetime

def ping_ip(ip):
    """Realiza un ping a la IP especificada y devuelve True si hay respuesta, False si no."""
    ping_command = ["ping", "-n", "1", ip]  # -n 1 para enviar solo un paquete
    response = subprocess.call(ping_command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return response == 0

def registrar_en_archivo(mensaje):
    """Registra el mensaje en un archivo de texto."""
    with open("registro_ping.txt", "a") as archivo:
        fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        archivo.write(f"{fecha_hora}: {mensaje}\n")

def main():
    ip = input("Ingrese la dirección IP: ")
    while True:
        if ping_ip(ip):
            print(f"¡La IP {ip} está activa!")
            winsound.Beep(2000, 500)  # Reproduce un sonido de 2000 Hz durante 1 segundo
            registrar_en_archivo(f"La IP {ip} respondió")
        else:
            print(f"La IP {ip} no está activa.")
        time.sleep(0.3)  # Espera 0.3 segundos antes de realizar el siguiente ping

if __name__ == "__main__":
    main()