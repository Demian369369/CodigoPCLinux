def imprime():
    print("E")

def imprime2():
    print("E")
def do_connect(nombre, password):
    import network
    import ntptime
    import time
    return 1
    # wifi = network.WLAN(network.STA_IF)
    # wifi.disconnect()
    # timeout = 8000

    # if not wifi.isconnected():
    #     print('conectandose a red wifi...')
    #     wifi.active(True)
    #     wifi.connect(nombre, password)

    #     t = time.ticks_ms()
    #     while not wifi.isconnected():
    #         if time.ticks_diff(time.ticks_ms(), t) > timeout:
    #             wifi.disconnect()
    #             print("Error, no se encontro ninguna red")
    #             return False
    #     while not wifi.isconnected():
    #         pass
    # print('datos de red: ', wifi.ifconfig())
    # if wifi.isconnected():
    #     print(time.localtime())
    #     ntptime.settime()
    #     print(time.localtime())