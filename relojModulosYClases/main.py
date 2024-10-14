from machine import Pin, SoftI2C, RTC
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
from wifi import do_connect
import time
import Juegos
import apps
import Funciones
Mostrar = True
Bandera = True
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
        result = [cols[0].value(), cols[1].value(), cols[2].value(), cols[3].value()]
        if 0 in result:
            key = key_map[rows.index(r)][result.index(0)]
        r.value(1) 
    return key
I2C_ADDR = 0x3f
totalRows = 2
totalColumns = 16
i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)
lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)
redes = [
    {"nombre": "algocool", "password": "after9948"},
    {"nombre": "UNE Alumnos", "password": "0123456789"},
    {"nombre": "INFINITUMA6A1_2.4", "password": "TvF3x8aFqF"}
]
for red in redes:
    do_connect(red["nombre"], red["password"])
    print("conectando a la red: " + red["nombre"], red["password"])
    lcd.clear()
    lcd.move_to(0, 0)
    lcd.putstr("wifi: " + red["nombre"])
    lcd.move_to(0, 1)
    lcd.putstr(red["password"])
t = time.ticks_ms()
vista = 0
while True:
    if Bandera == True:
     if Mostrar == True:
      lcd.clear()
      lcd.move_to(0, 0)
      lcd.putstr("Estas en: ")
      lcd.move_to(0, 1)
      lcd.putstr(" Menu Principal")
      vista = 0
     Bandera = False
    if Mostrar == False:
       lcd.clear()
    if time.ticks_diff(time.ticks_ms(), t) > 1000:
      key = Keypad4x4Read(col_list, row_list)
      if key == "#":
          lcd.clear()
          vista = 0 
      if key == "*":
        if Mostrar == True:
          Mostrar  = False
        else: 
          Mostrar = True
      if key is not None:
       if vista == 0:
        if key == "1":
          lcd.clear()
          vista = 1
        if key == "2":
          lcd.clear()
          vista = 2
        if key == "3":
          lcd.clear()
          vista = 3
        else:
          pass
        if vista == 0:
          lcd.clear()
          lcd.move_to(0, 0)
          lcd.putstr("1Juegos 2Apps")
          lcd.move_to(0, 1)
          lcd.putstr("3Funciones ")
        elif vista == 1:
          Juegos.Juegos()
        elif vista == 2:
         apps.App()
        elif vista == 3:
          Funciones()
      key = None
# exec(open("main.py").read())