from machine import Pin, SoftI2C, RTC
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
import time
import menu
def volver_a_vista_0():
    global vista
    lcd.clear
    vista = 0
Mostrar_pantallas = False
Mostrar_pantalla = True
cronometro_en_ejecucion = False
boton_c_presionado = False
tiempo_transcurrido = 0  
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
Mostrar = True
## Iniciar LCD
I2C_ADDR = 0x3f
totalRows = 2
totalColumns = 16
i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)
lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)

def menu1():
   oldKey = None
   menuNivel = 0
   while True:
      key = Keypad4x4Read(col_list, row_list)
      lcd.move_to(0,0)
      if menuNivel == 0:
        lcd.putstr("Menu 1 1")
      elif menuNivel == 1:
        lcd.putstr("Menu 1 2")
      elif menuNivel == 2:
        lcd.putstr("Menu 1 3")
      elif menuNivel == 3:
        lcd.putstr("Menu 1 4")
      if key == None:
        if oldKey == "A":
          if menuNivel > 0:
            menuNivel -= 1
        elif oldKey == "B":
            if menuNivel < 3:
              menuNivel += 1
        elif oldKey == "C":
            break
        elif oldKey == "D":
            volver_a_vista_0()  
            lcd.clear()
        elif oldKey == "*":
            lcd.clear()
        elif oldKey == "#":
            lcd.clear()
      oldKey = key

# Mueve la inicialización de t al principio del programa
t = time.ticks_ms()
vista = 0
menuNivel = 0
oldKey = None
while True:
    lcd.move_to(0,0)
    if menuNivel == 0:
        lcd.putstr("Menu 0 1")
    elif menuNivel == 1:
        lcd.putstr("Menu 0 2")
    elif menuNivel == 2:
        lcd.putstr("Menu 0 3")
    elif menuNivel == 3:
        lcd.putstr("Menu 0 4")
    if time.ticks_diff(time.ticks_ms(), t) > 100:
      t = time.ticks_ms()
      key = Keypad4x4Read(col_list, row_list)
      if key == None:
        if oldKey == "A":
          if menuNivel > 0:
            menuNivel -= 1
        elif oldKey == "B":
            if menuNivel < 3:
              menuNivel += 1
        elif oldKey == "C":
          if menuNivel == 0:
             menu1()
        elif oldKey == "D":
            volver_a_vista_0()  
            lcd.clear()
        elif oldKey == "*":
            lcd.clear()
        elif oldKey == "#":
            lcd.clear()
      oldKey = key
      #exec(open("main.py").read())