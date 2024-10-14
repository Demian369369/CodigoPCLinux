# #exec(open('main.py').read())
# import sh1106
# import network
# from machine import Pin, I2C
# import time
# wifi = network.WLAN(network.STA_IF)
# i2c = I2C(scl=Pin(4), sda=Pin(5), freq=400000)
# display = sh1106.SH1106_I2C(128, 64, i2c, None, 0x3c)
# display.sleep(False)
# display.rotate(True, update=True)
# rTiempo = True
# Mostrar = True
# Bandera = False
# suma = True
# suma2 = "+"
# DN = "AM"
# WHEEL_UP = Pin(13, Pin.IN, Pin.PULL_UP)
# WHEEL_CENTER = Pin(14, Pin.IN, Pin.PULL_UP)
# WHEEL_DOWN = Pin(12, Pin.IN, Pin.PULL_UP)
# SIDE_A = Pin(2, Pin.IN, Pin.PULL_UP)
# SIDE_B = Pin(0, Pin.IN, Pin.PULL_UP)    
# class tiempo:
#     def __init__(self):
#         self.año = tiempoInicial[0]
#         self.mes = tiempoInicial[1]
#         self.dia = tiempoInicial[2]
#         self.hora = tiempoInicial[3]
#         self.minuto = tiempoInicial[4]
#         self.segundo = tiempoInicial[5]
#     def imprimeHora(self):
#         tiempo_actual = str(self.hora) + ":" + str(self.minuto) + ":" + str(self.segundo)
#         return tiempo_actual
#     def imprimeFecha(self):
#         fecha = str(self.dia) + " | " + str(self.mes) + " | " + str(self.año)
#         return fecha
#     def decoracion(self):
#         if wifi.isconnected():  
#          decoracion = "([])"
#         else: 
#          decoracion = "(X)"
#         return decoracion
#     def elHorario(self):
#         if self.hora >= 12:
#             DN = "PM"
#         else:
#             DN = "AM"
#         return DN
#     def SoR(self):
#         if suma == True:
#          suma2 = "+"
#         else:
#          suma2 = "-"
#         return suma2
#     def elTiempo(self):
#         if self.segundo <= 59:
#             self.segundo += 1
#         elif self.minuto <= 59 and self.segundo == 60:
#             self.minuto += 1
#             self.segundo = 0
#         elif self.hora <= 23 and self.minuto == 60:
#             self.hora += 1
#             self.minuto = 0
#             self.segundo = 0
#         elif self.dia <= 30 and self.hora == 24:
#             self.dia += 1
#             self.hora = 0
#             self.minuto = 0
#             self.segundo = 0
#         elif self.mes <= 11 and self.dia == 30:
#             self.mes += 1
#             self.dia = 0
#             self.hora = 0
#             self.minuto = 0
#             self.segundo = 0
#         elif self.año <= 99 and self.mes == 12:
#             self.año += 1
#             self.mes = 0
#             self.dia = 0
#             self.hora = 0
#             self.minuto = 0
#             self.segundo = 0
# ajusteDeHora = time.time() + -6 * 3600
# tiempoInicial = time.localtime(ajusteDeHora)
# print(tiempoInicial)
# contador = tiempo()
# while True:
#          Bandera = not Bandera
#          print(f"SIDE_A: {SIDE_A.value()}, WHEEL_UP: {WHEEL_UP.value()}, WHEEL_CENTER: {WHEEL_CENTER.value()}, WHEEL_DOWN: {WHEEL_DOWN.value()}, SIDE_B: {SIDE_B.value()}")
#          if SIDE_A.value() == 0 and not WHEEL_UP == 0 and not WHEEL_CENTER == 0 and not WHEEL_DOWN == 0 and not SIDE_B == 0:
#             if Bandera == True:
#              Mostrar = False
#              display.fill(0)
#              display.show()
#             else :
#              Mostrar = True
#          if SIDE_B.value() == 0 and not WHEEL_UP == 0 and not WHEEL_CENTER == 0 and not WHEEL_DOWN == 0 and not SIDE_A == 0:
#             suma = not suma
#          if rTiempo == True:
#             contador.elTiempo()
#             tiempo_actual = contador.imprimeHora()
#             fecha = contador.imprimeFecha()
#             time.sleep(1)
#          if Mostrar == True:
#             display.fill(0)
#             display.text("(" + 'Tiempo:' + ")", 1, 1, 1)
#             display.text(tiempo_actual, 1, 15, 1)
#             display.text(contador.elHorario(), 70, 15, 1)
#             display.text("(" + 'Fecha:' + ")", 1, 30, 1)
#             display.text(fecha, 1, 45, 1)
#             display.text(contador.decoracion(), 95, 1, 1)
#             display.text(contador.SoR(), 115, 15, 1)
#             display.show()
#          if SIDE_A.value() == 0 and WHEEL_UP.value() == 0:
#             if suma == True:
#              contador.hora += 1
#             else:
#              contador.hora -= 1
#          elif SIDE_A.value() == 0 and WHEEL_CENTER.value() == 0:
#           if suma == True:
#             contador.minuto += 1
#           else:
#             contador.minuto -= 1
#          elif SIDE_A.value() == 0 and WHEEL_DOWN.value() == 0:
#             if suma == True:
#              contador.segundo += 1
#             else:
#              contador.segundo -= 1
#          elif SIDE_B.value() == 0 and WHEEL_UP.value() == 0:
#             if suma == True:
#              contador.dia += 1
#             else:
#              contador.dia -= 1
#          elif SIDE_B.value() == 0 and WHEEL_CENTER.value() == 0:
#             if suma == True:
#              contador.mes += 1
#             else:
#              contador.mes -= 1
#          elif SIDE_B.value() == 0 and WHEEL_DOWN.value() == 0:
#             if suma == True:
#              contador.año += 1
#             else:
#              contador.año -= 1
import sh1106
import network
from machine import Pin, I2C
import time

# Configuración de red y display
wifi = network.WLAN(network.STA_IF)
i2c = I2C(scl=Pin(4), sda=Pin(5), freq=400000)
display = sh1106.SH1106_I2C(128, 64, i2c, None, 0x3c)
display.sleep(False)
display.rotate(True, update=True)

# Inicialización de variables
rTiempo = True
Mostrar = True
Bandera = False
suma = True
suma2 = "+"
DN = "AM"
WHEEL_UP = Pin(13, Pin.IN, Pin.PULL_UP)
WHEEL_CENTER = Pin(14, Pin.IN, Pin.PULL_UP)
WHEEL_DOWN = Pin(12, Pin.IN, Pin.PULL_UP)
SIDE_A = Pin(2, Pin.IN, Pin.PULL_UP)
SIDE_B = Pin(0, Pin.IN, Pin.PULL_UP)

# Ajuste de tiempo inicial con manejo de zona horaria
ajusteDeHora = time.time() - (6 * 3600)  # Ajuste de -6 horas para la zona horaria
tiempoInicial = time.localtime(ajusteDeHora)
print(tiempoInicial)

# Clase para manejar el tiempo
class Tiempo:
    def __init__(self):
        self.año = tiempoInicial[0]
        self.mes = tiempoInicial[1]
        self.dia = tiempoInicial[2]
        self.hora = tiempoInicial[3]
        self.minuto = tiempoInicial[4]
        self.segundo = tiempoInicial[5]
    
    def imprimeHora(self):
        tiempo_actual = f"{self.hora:02}:{self.minuto:02}:{self.segundo:02}"
        return tiempo_actual
    
    def imprimeFecha(self):
        fecha = f"{self.dia:02} | {self.mes:02} | {self.año}"
        return fecha
    
    def decoracion(self):
        if wifi.isconnected():  
            decoracion = "([])"
        else: 
            decoracion = "(X)"
        return decoracion
    
    def elHorario(self):
        if self.hora >= 12:
            return "PM"
        else:
            return "AM"
    
    def SoR(self):
        if suma:
            return "+"
        else:
            return "-"
    
    def elTiempo(self, current_time):
        self.año = current_time[0]
        self.mes = current_time[1]
        self.dia = current_time[2]
        self.hora = current_time[3]
        self.minuto = current_time[4]
        self.segundo = current_time[5]

contador = Tiempo()

while True:
    Bandera = not Bandera
    print(f"SIDE_A: {SIDE_A.value()}, WHEEL_UP: {WHEEL_UP.value()}, WHEEL_CENTER: {WHEEL_CENTER.value()}, WHEEL_DOWN: {WHEEL_DOWN.value()}, SIDE_B: {SIDE_B.value()}")

    if SIDE_A.value() == 0 and not WHEEL_UP.value() == 0 and not WHEEL_CENTER.value() == 0 and not WHEEL_DOWN.value() == 0 and not SIDE_B.value() == 0:
        if Bandera:
            Mostrar = False
            display.fill(0)
            display.show()
        else:
            Mostrar = True

    if SIDE_B.value() == 0 and not WHEEL_UP.value() == 0 and not WHEEL_CENTER.value() == 0 and not WHEEL_DOWN.value() == 0 and not SIDE_A.value() == 0:
        suma = not suma

    if rTiempo:
        current_time = time.localtime(time.time() - (6 * 3600))  # Ajuste de -6 horas para la zona horaria
        contador.elTiempo(current_time)
        tiempo_actual = contador.imprimeHora()
        fecha = contador.imprimeFecha()
        time.sleep(1)  # Espera de 1 segundo para la siguiente iteración

    if Mostrar:
        display.fill(0)
        display.text("(" + 'Tiempo:' + ")", 1, 1, 1)
        display.text(tiempo_actual, 1, 15, 1)
        display.text(contador.elHorario(), 70, 15, 1)
        display.text("(" + 'Fecha:' + ")", 1, 30, 1)
        display.text(fecha, 1, 45, 1)
        display.text(contador.decoracion(), 95, 1, 1)
        display.text(contador.SoR(), 115, 15, 1)
        display.show()

    if SIDE_A.value() == 0 and WHEEL_UP.value() == 0:
        if suma:
            contador.hora += 1
        else:
            contador.hora -= 1
    elif SIDE_A.value() == 0 and WHEEL_CENTER.value() == 0:
        if suma:
            contador.minuto += 1
        else:
            contador.minuto -= 1
    elif SIDE_A.value() == 0 and WHEEL_DOWN.value() == 0:
        if suma:
            contador.segundo += 1
        else:
            contador.segundo -= 1
    elif SIDE_B.value() == 0 and WHEEL_UP.value() == 0:
        if suma:
            contador.dia += 1
        else:
            contador.dia -= 1
    elif SIDE_B.value() == 0 and WHEEL_CENTER.value() == 0:
        if suma:
            contador.mes += 1
        else:
            contador.mes -= 1
    elif SIDE_B.value() == 0 and WHEEL_DOWN.value() == 0:
        if suma:
            contador.año += 1
        else:
            contador.año -= 1
