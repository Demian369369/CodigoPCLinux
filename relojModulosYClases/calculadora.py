def cal():
    import math
    import time
    from machine import Pin, SoftI2C
    from i2c_lcd import I2cLcd
    I2C_ADDR = 0x3f
    totalRows = 2
    totalColumns = 16
    i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)
    lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)
    key_map = [["D", "#", "0", "*"],
            ["C", "9", "8", "7"],
            ["B", "6", "5", "4"],
            ["A", "3", "2", "1"]]
    row_list = [13, 12, 14, 27]
    col_list = [26, 25, 33, 32]
    for x in range(4):
        row_list[x] = Pin(row_list[x], Pin.OUT)
    for x in range(4):
        col_list[x] = Pin(col_list[x], Pin.IN, Pin.PULL_UP)
    def seleccionar_operacion():
        lcd.putstr("Elije problema: ")
        lcd.clear()
        lcd.putstr("1+ 2- 3* 4/")
        lcd.move_to(0, 1)
        lcd.putstr("5^ 6/^ 7Cos 8Log")
        operacion = None
        while operacion is None:
            key = Keypad4x4Read(col_list, row_list)
            if key in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                operacion = key
        return operacion
    def Keypad4x4Read(cols, rows):
        key = None
        for r in rows:
            r.value(0)
            result = [cols[0].value(), cols[1].value(), cols[2].value(), cols[3].value()]
            if 0 in result:
                key = key_map[rows.index(r)][result.index(0)]
            r.value(1)
        return key
    def ingresar_numero():
        numero_actual = ""
        lcd.clear()
        lcd.move_to(0, 0)
        lcd.putstr("Ingrese número: ")  
        while True:
            seleccionar_operacion()
            key = Keypad4x4Read(col_list, row_list)
            if key.isdigit():
                realizar_operacion()
                numero_actual += key
                lcd.move_to(0, 1)
                lcd.putstr(numero_actual)
            elif key == "#":
                try:
                    numero = float(numero_actual)
                    return numero
                except ValueError:
                    lcd.move_to(0, 1)
                    lcd.putstr("Número inválido")
                    time.sleep(1)
                    numero_actual = ""
                    lcd.move_to(0, 1)
                    lcd.putstr(numero_actual)
    def realizar_operacion(operacion, num1, num2):
        if operacion == '1':
            return num1 + num2
        elif operacion == '2':
            return num1 - num2
        elif operacion == '3':
            return num1 * num2
        elif operacion == '4':
            if num2 != 0:
                return num1 / num2
            else:
                return "División por cero"
        elif operacion == '5':
            return num1 ** num2
        elif operacion == '6':
            return math.sqrt(num1)
        elif operacion == '7':
            return math.cos(num1)
        elif operacion == '8':
            if num1 > 0:
                return math.log(num1)
            else:
                return "Logaritmo de número negativo o cero"
        else:
            return "Operación inválida"
    mostrar_resultado()
    def mostrar_resultado(resultado):
        lcd.clear()
        lcd.move_to(0, 0)
        lcd.putstr("Resultado:")
        lcd.move_to(0, 1)
        lcd.putstr(str(resultado))
        calculadora()
    t = time.ticks_ms()
    def calculadora():
        operacion = seleccionar_operacion()
        if operacion in ['1', '2', '3', '4', '5', '6', '7', '8']:
            num1 = ingresar_numero()
            num2 = ingresar_numero()
            resultado = realizar_operacion(operacion, num1, num2)
            mostrar_resultado(resultado)
        else:
            lcd.clear()
            lcd.move_to(0, 0)
            lcd.putstr("Operación inválida")
            time.sleep(1)
    ingresar_numero()
    #exec(open("calculadora.py").read())
