import tkinter as tk
from tkinter import ttk
import subprocess
import time
import winsound
import datetime

def ping_ip(ip):
    """Realiza un ping a la IP especificada y devuelve True si hay respuesta, False si no."""
    ping_command = ["ping", "-n", "1", ip]
    response = subprocess.call(ping_command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return response == 0

def registrar_en_archivo(mensaje):
    """Registra el mensaje en un archivo de texto."""
    with open("registro_ping.txt", "a") as archivo:
        fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        archivo.write(f"{fecha_hora}: {mensaje}\n")

def iniciar_ping():
    global ip_entrada, estado_label, resultado_text, detener_ping_flag
    detener_ping_flag = False  # Reiniciar la bandera antes de iniciar un nuevo ping
    ip = ip_entrada.get()
    if ip:
        estado_label.config(text="Ping en curso...")
        while not detener_ping_flag:
            if ping_ip(ip):
                estado_label.config(text=f"La IP {ip} está activa!")
                winsound.Beep(2000, 500)
                registrar_en_archivo(f"La IP {ip} respondió")
                resultado_text.insert(tk.END, f"{datetime.datetime.now()}: La IP {ip} está activa!\n")
            else:
                estado_label.config(text=f"La IP {ip} no está activa.")
                registrar_en_archivo(f"La IP {ip} no respondió")
                resultado_text.insert(tk.END, f"{datetime.datetime.now()}: La IP {ip} no está activa!\n")
            #resultado_text.see(tk.END)  # Desplazar la vista al final
            time.sleep(0.3)

def detener_ping():
    global detener_ping_flag
    detener_ping_flag = True
    estado_label.config(text="Ping detenido.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Monitor de Ping")

# Crear los elementos de la interfaz
ip_label = ttk.Label(ventana, text="Dirección IP:")
ip_entrada = ttk.Entry(ventana)
iniciar_boton = ttk.Button(ventana, text="Iniciar Ping", command=iniciar_ping)
detener_boton = ttk.Button(ventana, text="Detener Ping", command=detener_ping, state=tk.DISABLED)
estado_label = ttk.Label(ventana, text="")
resultado_label = ttk.Label(ventana, text="Resultados:")
resultado_text = tk.Text(ventana, height=10)

# Empaquetar los elementos
ip_label.pack()
ip_entrada.pack()
iniciar_boton.pack()
detener_boton.pack()
estado_label.pack()
resultado_label.pack()
resultado_text.pack()

ventana.mainloop()
