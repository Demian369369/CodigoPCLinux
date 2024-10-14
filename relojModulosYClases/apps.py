from machine import Pin, SoftI2C, RTC
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
import time
import reloj
import cronometro
import calculadora
def App():
    vistas = 0
    Bandera = True
    Mostrar = True
    row_list = [13, 12, 14, 27]
    col_list = [26, 25, 33, 32]
    for x in range(4):
        row_list[x] = Pin(row_list[x], Pin.OUT)
        row_list[x].value(1)
    for x in range(4):
        col_list[x] = Pin(col_list[x], Pin.IN, Pin.PULL_UP)
    key_map = [["D", "#", "0", "*"],
            ["C", "9", "8", "7"],
            ["B", "6", "5", "4"],
            ["A", "3", "2", "1"]]


    def Keypad4x4Read(cols, rows):
        key = None
        for r in rows:
            r.value(0)
            result = [cols[0].value(), cols[1].value(),
                    cols[2].value(), cols[3].value()]
            if 0 in result:
                key = key_map[rows.index(r)][result.index(0)]
            r.value(1)
        return key


    I2C_ADDR = 0x3f
    totalRows = 2
    totalColumns = 16
    i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)
    lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)
    t = time.ticks_ms()
    rel = reloj.tiempo()
    # cron = cronometro.cronometro()
    # Mueve la inicialización de t al principio del programa
    t = time.ticks_ms()
    while True:
        tiempo_actual = rel.imprimeHora()
        fecha = rel.imprimeFecha()
        if Bandera == True:
            if Mostrar == True:
                lcd.clear()
                lcd.move_to(0, 0)
                lcd.putstr("Estas en Apps ")
                lcd.move_to(0, 1)
                lcd.putstr("   Menu    ")
            Bandera = False
        if Mostrar == False:
            lcd.clear()
        if time.ticks_diff(time.ticks_ms(), t) > 1000:
            t = time.ticks_ms()
            key = Keypad4x4Read(col_list, row_list)
            if key == "#":
                lcd.clear()
                break
            if key == "0":
                lcd.clear()
                vistas = 0
            if key == "*":
                if Mostrar == True:
                    Mostrar = False
                else:
                    Mostrar = True
            if key is not None:
                if vistas == 0:
                    if key == "1":
                        lcd.clear()
                        vistas = 1
                    if key == "2":
                        lcd.clear()
                        vistas = 2
                    if key == "3":
                        lcd.clear()
                        vistas = 3
            else:
                pass
            if vistas == 0:
                if Mostrar == True:
                    lcd.move_to(0, 0)
                    lcd.putstr("1Reloj 2Crono(m)")
                    lcd.move_to(0, 1)
                    lcd.putstr("3Calculadora")
            elif vistas == 1:
                lcd.move_to(0, 0)
                lcd.putstr(tiempo_actual)
                lcd.move_to(0, 1)
                lcd.putstr(fecha)
            elif vistas == 2:
                cronometro.cronometros()
            elif vistas == 3:
                calculadora.cal()
        key = None
    # exec(open("main.py").read())
