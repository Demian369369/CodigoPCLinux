import pygame
import sys
import random
import time
pygame.init()
ANCHO, ALTO = 1000, 1000
FPS = 60
Azul = (0, 0, 255)
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Captura los círculos azules")
reloj = pygame.time.Clock()
def generar_circulo():
    radio = random.randint(20, 50)
    x = random.randint(radio, ANCHO - radio)
    y = random.randint(radio, ALTO - radio)
    return {"x": x, "y": y, "radio": radio, "color": Azul, "visible": False, "tiempo_aparicion": time.time()}
puntos = 0
circulos = []
ultimo_tiempo_circulo = time.time()
tiempo_no_presionar = 0
running = True
while running:
    pantalla.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if time.time() - ultimo_tiempo_circulo > max(4 - puntos/20, 1):
        circulo = generar_circulo()
        circulos.append(circulo)
        ultimo_tiempo_circulo = time.time()
    mouse_x, mouse_y = pygame.mouse.get_pos()
    clicked = pygame.mouse.get_pressed()[0]
    for circulo in circulos[:]:
        if not circulo["visible"] and time.time() - circulo["tiempo_aparicion"] > 5:
            circulo["visible"] = True
        if circulo["visible"]:
            pygame.draw.circle(pantalla, circulo["color"], (circulo["x"], circulo["y"]), circulo["radio"])
        
            circulo["radio"] = max(circulo["radio"] - puntos/50, 5)
            distancia = ((circulo["x"] - mouse_x) ** 2 + (circulo["y"] - mouse_y) ** 2) ** 0.5
            if distancia < circulo["radio"] and circulo["color"] == Azul and clicked:
                puntos += 1
                circulo["visible"] = False
                circulo["tiempo_aparicion"] = time.time()
    fuente = pygame.font.Font(None, 36)
    texto_puntos = fuente.render(f"Puntos: {puntos}", True, (0, 0, 0))
    pantalla.blit(texto_puntos, (10, 10))
    pygame.display.flip()
    reloj.tick(FPS)
pygame.quit()
sys.exit()


