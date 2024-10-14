def cronometros():
    import time
    from machine import Pin, SoftI2C, RTC
    from lcd_api import LcdApi
    from i2c_lcd import I2cLcd
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
    t = time.ticks_ms()
    while True:
              def cronometro():
               def diffTiempo(self, ticks):
                 diferencia = time.ticks_diff(time.ticks_ms(), ticks)
                 return diferencia
              t = time.ticks_ms()
              sumar_cronometro = True
              hora_cronometro = 0
              minuto_cronometro = 0
              segundo_cronometro = 0
              if time.ticks_diff(time.ticks_ms(), t) > 1000:
               t = time.ticks_ms()
               key = Keypad4x4Read(col_list, row_list)
              if key == "A":
                sumar_cronometro = not sumar_cronometro
              elif key == 'B':
                if sumar_cronometro:
                    segundo_cronometro += 1
                    segundo_cronometro = segundo_cronometro % 60  
                else:
                    segundo_cronometro -= 1
                    if segundo_cronometro < 0:
                        segundo_cronometro = 59
              elif key == "C":
                if sumar_cronometro:
                    minuto_cronometro += 1
                    minuto_cronometro = minuto_cronometro % 60  
                else:
                    minuto_cronometro -= 1
                    if minuto_cronometro < 0:
                        minuto_cronometro = 59
              elif key == "D":
                if sumar_cronometro:
                    hora_cronometro += 1
                    hora_cronometro = hora_cronometro % 24  
                else:
                    hora_cronometro -= 1
                if hora_cronometro < 0:
                    hora_cronometro = 23
              elif key == "9": 
                    hora_cronometro = 0
                    minuto_cronometro = 0
                    segundo_cronometro = 0
              elif key == '0':
               break
              tiempo_cronometro = f"{hora_cronometro:02d}:{minuto_cronometro:02d}:{segundo_cronometro:02d}"
              lcd.move_to(0, 0)
              lcd.putstr("Cronometro")
              lcd.move_to(0, 1)
              lcd.putstr(tiempo_cronometro)
    cronometro()

        