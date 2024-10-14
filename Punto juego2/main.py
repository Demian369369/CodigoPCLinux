import pygame
from pygame.math import Vector2
import os
import random
import time
pygame.init()
Mouse = False
ANCHO = 800
ALTO = 800
WIN = pygame.display.set_mode((ANCHO, ALTO))
class Puntos:
    def __init__(self, x, y, size, color):
        self.body = [Vector2(x, y)]
        self.direction = Vector2(0, -2)  
        self.size = size
        self.color = color
        self.started = False
    def move(self):
        new_head = self.body[0] + self.direction
        new_head.x = max(0, min(new_head.x, ANCHO - 1))
        new_head.y = max(0, min(new_head.y, ALTO - 1))
        self.body = [new_head] + self.body[:-1]
    def check_collision(self, point):
        return self.body[0].distance_to(point.body[0]) < (self.size + point.size) / 2
    def aumentar_tamano(self):
        self.size += 2
    def crear_nuevo_punto(self):
        return Puntos(random.randint(0, ANCHO - 1), random.randint(0, ALTO - 1), 20, (0, 0, 255))
    def mover_aleatoriamente(self):
        random_direction = Vector2(random.choice([-2, 0, 2]), random.choice([-2, 0, 2])) 
        self.direction = random_direction
def main():
    global Mouse
    puntos_azules = [Puntos(random.randint(0, ANCHO - 1), random.randint(0, ALTO - 1), 20, (0, 0, 255)) for _ in range(5)]
    fps = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                Mouse = True
            if event.type == pygame.MOUSEBUTTONUP:
                Mouse = False
        mouse_position = Vector2(pygame.mouse.get_pos())
        for punto_azul in puntos_azules:
            punto_azul.mover_aleatoriamente()
            if Mouse and punto_azul.check_collision(Puntos(mouse_position.x, mouse_position.y, 1, (0, 0, 0))):
                punto_azul.aumentar_tamano()
        tocando_puntos = any(punto_azul.check_collision(Puntos(mouse_position.x, mouse_position.y, 1, (0, 0, 0))) for punto_azul in puntos_azules)
        if not tocando_puntos:
            WIN.fill((255, 255, 255))
        for punto_azul in puntos_azules:
            pygame.draw.circle(WIN, punto_azul.color, (int(punto_azul.body[0].x), int(punto_azul.body[0].y)), int(punto_azul.size))
        pygame.display.update()
        fps.tick(10)
        if len(puntos_azules) >= 100:
            print("perdiste")
            time.sleep(1)
            pygame.quit()
            quit()
if __name__ == "__main__":
    main()
