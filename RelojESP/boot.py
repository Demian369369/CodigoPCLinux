import network
import ntptime
import time
import sh1106
from machine import Pin, I2C

i2c = I2C(scl=Pin(4), sda=Pin(5), freq=400000)
display = sh1106.SH1106_I2C(128, 64, i2c, None, 0x3c)
display.sleep(False)
display.rotate(True, update=True)
wifi = network.WLAN(network.STA_IF)
wifi.disconnect()

def do_connect(nombre, password):
    timeout = 8000

    if not wifi.isconnected():
        print('Conectándose a la red WiFi...')
        wifi.active(True)
        if password:
            wifi.connect(nombre, password)
        else:
            wifi.connect(nombre)

        t = time.ticks_ms()
        while not wifi.isconnected():
            if time.ticks_diff(time.ticks_ms(), t) > timeout:
                wifi.disconnect()
                print("Error: No se pudo conectar a", nombre)
                display.fill(0)
                display.text("Error:", 1, 1, 1)
                display.text("No se pudo conectar", 1, 20, 1)
                display.text("a la red:", 1, 30, 1)
                display.text(nombre, 1, 40, 1)
                display.show()
                time.sleep(2)  # Pausa para que el mensaje sea visible
                return False
        while not wifi.isconnected():
            pass

    print('Datos de red: ', wifi.ifconfig())
    if wifi.isconnected():
        ntptime.settime()
        return True
    return False

redes = [
    {"nombre": "algocool", "password": "after9948"},
    {"nombre": "MOVE WELLNESS", "password": "sociosMOVE"},
    {"nombre": "INFINITUMA6A1_2.4", "password": "TvF3x8aFqF"},
    {"nombre": "iCUCEI", "password": None}  
]

conectado = False
for red in redes:
    print("Conectando a la red:", red["nombre"], red["password"] or "Sin contraseña")
    display.fill(0)
    display.text("Buscando Red ", 1, 1, 1)
    display.text("Conectando a:", 1, 20, 1)
    display.text(red["nombre"], 1, 30, 1)
    display.text("Clave:", 1, 40, 1)
    display.text(red["password"] or "Sin contraseña", 1, 50, 1)
    display.show()

    if do_connect(red["nombre"], red["password"]):
        conectado = True
        break

if conectado:
    print('Conectado a la red WiFi:', red["nombre"])
    display.fill(0)
    display.text("Conectado a:", 1, 1, 1)
    display.text(red["nombre"], 1, 20, 1)
    display.text("IP:", 1, 30, 1)
    display.text(wifi.ifconfig()[0], 1, 40, 1)
    display.show()
else:
    print('No se pudo conectar a ninguna red.')
    display.fill(0)
    display.text("Error:", 1, 1, 1)
    display.text("No se pudo conectar", 1, 20, 1)
    display.text("a ninguna red", 1, 30, 1)
    display.show()
