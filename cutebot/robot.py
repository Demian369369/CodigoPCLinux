from microbit import *
from cutebot import *
import radio
import music
radio.config(group=7)
ct = CUTEBOT()
radio.on
def mover_carro(direccion):
    if direccion == 'adelante':
        ct.set_motors_speed(53, 50)
    elif direccion == 'atras':
        ct.set_motors_speed(-43, -45)
    elif direccion == 'izquierda':
        ct.set_motors_speed(25, -22)
    elif direccion == 'derecha':
        ct.set_motors_speed(-27, 25)
    else:
        ct.set_motors_speed(0, 0)
def reproducir_musica(cancion):
    if cancion == "1":
        music.play(music.BA_DING, wait=False)
    elif cancion == "2":
        music.play(music.POWER_UP, wait=False)
    elif cancion == "3":
        music.play(music.POWER_DOWN, wait=False)
    elif cancion == "4":
        music.play(music.JUMP_UP, wait=False)
def encender_luces(color):
    color_dict = {
        "verde": 0x00ff00,
        "rojo": 0xff0000,
        "azul": 0x0000ff,
        "amarillo": 0xffff00,
        "morado": 0x7f00ff,
        "cian": 0x00ffff
    }
    if color in color_dict:
        ct.set_car_light(left, 90, 90, 90)
        ct.set_car_light(right, 90, 90, 90)
        sleep(1000)
        ct.set_car_light(left, 0, 0, 0)
        ct.set_car_light(right, 0, 0, 0)
def on_button_pressed_a():
    radio.send("izquierda")
    encender_luces("morado")
    pantalla("3")
    sleep(200)  
    encender_luces("rojo")
    mover_carro("izquierda")
    sleep(500)
    mover_carro("parar")
    encender_luces("rojo")
    pantalla("0")
def on_button_pressed_b():
    radio.send("derecha")
    encender_luces("azul")
    pantalla("4")
    sleep(200)  
    encender_luces("rojo")
    mover_carro("derecha")
    sleep(500)
    mover_carro("parar")
    encender_luces("rojo")
    pantalla("0")
def on_button_pressed_ab():
    radio.send("atras")
    encender_luces("amarillo")
    sleep(200)  
    encender_luces("rojo")
    pantalla("2")
    mover_carro("atras")
    sleep(1000)
    mover_carro("parar")
    encender_luces("rojo")
    pantalla("0")
def on_logo_pressed():
    radio.send("adelante")
    encender_luces("rojo")
    pantalla("1")
    sleep(200)  
    encender_luces("verde")
    mover_carro("adelante")
    sleep(1000)
    mover_carro("parar")
    encender_luces("rojo")
    pantalla("0")

def pantalla(texto4: str):
    if texto4 == "0": #parar
        display.show(Image('09990:'
                           '90099:'
                           '90909:'
                           '99009:'
                           '09990'))
    if texto4 == "1": #arriba
        display.show(Image('00900:'
                           '09990:'
                           '00900:'
                           '00900:'
                           '00900'))
    if texto4 == "2": #abajo
        display.show(Image.SWORD)
        sleep(400)
    if texto4 == "3": #izquierda
        display.show(Image('00000:'
                           '09000:'
                           '99999:'
                           '09000:'
                           '00000'))
    if texto4 == "4": #derecha
        display.show(Image('00000:'
                           '00090:'
                           '99999:'
                           '00090:'
                           '00000'))
    if texto4 == "5":
        display.clear()
while True:
    distance=ct.get_distance()
    if distance <= 10:
        encender_luces("cian")
        mover_carro("izquierda")
        sleep(250)
        mover_carro("parar")
    else: 
        print(distance)
    mensaje = radio.receive()
    if mensaje == "adelante":
        on_logo_pressed()
    elif mensaje == "izquierda":
        on_button_pressed_a()
    elif mensaje == "atras":
        on_button_pressed_ab()
    elif mensaje == "derecha":
        on_button_pressed_b()
message = ""