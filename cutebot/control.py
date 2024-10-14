from microbit import *
from cutebot import *
import radio
import music
radio.on()
radio.config(group=7)
def reproducir_musica(cancion):
    if cancion == "1":
        music.play(music.BA_DING, wait=False)
    elif cancion == "2":
        music.play(music.POWER_UP, wait=False)
    elif cancion == "3":
        music.play(music.POWER_DOWN, wait=False)
    elif cancion == "4":
        music.play(music.JUMP_UP, wait=False)
def on_button_pressed_a():
    radio.send("izquierda")
    pantalla("3")
    sleep(500)  
    pantalla("0")
def on_button_pressed_b():
    radio.send("derecha")
    pantalla("4")
    sleep(500)
    pantalla("0")
def on_button_pressed_ab():
    radio.send("atras")
    pantalla("2")
    sleep(500)
    pantalla("0")
def on_logo_pressed():
    radio.send("adelante")
    pantalla("1")
    sleep(500)
    pantalla("0")
def pantalla(texto4: str):
    if pantalla == "0": #parar
        display.show(Image('09990:'
                           '90099:'
                           '90909:'
                           '99009:'
                           '09990'))
    if pantalla == "1": #arriba
        display.show(Image('00900:'
                           '09990:'
                           '00900:'
                           '00900:'
                           '00900'))
    if pantalla == "2": #abajo
        display.show(Image.SWORD)
        sleep(400)
    if pantalla == "3": #izquierda
        display.show(Image('00000:'
                           '09000:'
                           '99999:'
                           '09000:'
                           '00000'))
    if pantalla == "4": #derecha
        display.show(Image('00000:'
                           '00090:'
                           '99999:'
                           '00090:'
                           '00000'))
    if pantalla == "5":
        display.clear()
while True:
    mensaje = radio.receive()
    if(button_a.get_presses() != 0):
        on_button_pressed_a()
    if mensaje == "adelante":
        on_logo_pressed()
    elif mensaje == "izquierda":
        on_button_pressed_a()
    elif mensaje == "atras":
        on_button_pressed_ab()
    elif mensaje == "derecha":
        on_button_pressed_b()
    