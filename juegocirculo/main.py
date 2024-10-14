import pygame
import sys
import random
import time
pygame.init()
ANCHO, ALTO = 1000, 1000
FPS = 60
Azul = (0, 0, 255)
Morado = (128, 0, 128)
Dorado = (255, 215, 0)
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Captura los círculos azules")
reloj = pygame.time.Clock()
def generar_circulo():
    radio = random.randint(20, 50)
    x = random.randint(radio, ANCHO - radio)
    y = random.randint(radio, ALTO - radio)
    color = Azul if random.random() < 0.8 else Morado
    return {"x": x, "y": y, "radio": radio, "color": color}
def generar_punto_dorado():
    x = random.randint(20, ANCHO - 20)
    y = random.randint(20, ALTO - 20)
    return {"x": x, "y": y, "puntos": 10}
puntos = 0
vidas = 3
circulos = []
punto_dorado = None
ultimo_tiempo_circulo = time.time()
tiempo_no_presionar = 0
tiempo_ultimo_punto_dorado = time.time()
running = True
while running and vidas > 0:
    pantalla.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if time.time() - ultimo_tiempo_circulo > 4:
        circulos.append(generar_circulo())
        ultimo_tiempo_circulo = time.time()
    mouse_x, mouse_y = pygame.mouse.get_pos()
    clicked = pygame.mouse.get_pressed()[0]
    for circulo in circulos:
        pygame.draw.circle(pantalla, circulo["color"], (circulo["x"], circulo["y"]), circulo["radio"])
        circulo["y"] += 2 + int(puntos / 10)
        if circulo["color"] == Azul and circulo["y"] > ALTO:
            puntos -= 1
            circulos.remove(circulo)
    if puntos >= 5 and time.time() - tiempo_ultimo_punto_dorado > 20:
        punto_dorado = generar_punto_dorado()
        tiempo_ultimo_punto_dorado = time.time()
    if punto_dorado:
        pygame.draw.circle(pantalla, Dorado, (punto_dorado["x"], punto_dorado["y"]), 10)
        distancia = ((punto_dorado["x"] - mouse_x) ** 2 + (punto_dorado["y"] - mouse_y) ** 2) ** 0.5
        if distancia < 10 and clicked:
            puntos += 10
            punto_dorado = None
    for circulo in circulos[:]:
        distancia = ((circulo["x"] - mouse_x) ** 2 + (circulo["y"] - mouse_y) ** 2) ** 0.5
        if distancia < circulo["radio"] and circulo["color"] == Azul and clicked:
            puntos += 1
            circulos.remove(circulo)
            tiempo_no_presionar = time.time()
        elif distancia < circulo["radio"] and circulo["color"] == Morado and clicked:
            vidas -= 1
            circulos.remove(circulo)
    fuente = pygame.font.Font(None, 36)
    texto_puntos = fuente.render(f"Puntos: {puntos}", True, (0, 0, 0))
    texto_vidas = fuente.render(f"Vidas: {vidas}", True, (0, 0, 0))
    pantalla.blit(texto_puntos, (10, 10))
    pantalla.blit(texto_vidas, (10, 50))
    pygame.display.flip()
    reloj.tick(FPS)
pygame.quit()
sys.exit()

