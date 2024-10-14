
def do_connect(nombre, password):
    import network
    import ntptime
    import time
    wifi = network.WLAN(network.STA_IF)
    timeout = 12000

    if not wifi.isconnected():
        print('conectandose a red wifi...')
        wifi.active(True)
        wifi.connect(nombre, password)

        t = time.ticks_ms()
        while not wifi.isconnected():
            if time.ticks_diff(time.ticks_ms(), t) > timeout:
                wifi.disconnect()
                print("Error, no se encontro ninguna red")
                return False
        while not wifi.isconnected():
            pass
    print('datos de red: ', wifi.ifconfig())
    if wifi.isconnected():
        ntptime.settime()
        print(time.localtime())