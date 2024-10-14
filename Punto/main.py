import pygame
from pygame.math import Vector2
import os
import random
import time
pygame.init()
ANCHO = 720
ALTO = 480
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
    def check_collision(self, other_point):
        return self.body[0].distance_to(other_point.body[0]) < (self.size + other_point.size) / 2
    def aumentar_tamano(self):
        self.size += 2
    def crear_nuevo_punto(self):
        return Puntos(random.randint(0, ANCHO - 1), random.randint(0, ALTO - 1), 20, (0, 0, 255))
    def mover_aleatoriamente(self):
        random_direction = Vector2(random.choice([-2, 0, 2]), random.choice([-2, 0, 2])) 
        self.direction = random_direction
    def mover_arriba(self):
        self.direction = Vector2(0, -5) 
        self.started = True
    def mover_abajo(self):
        self.direction = Vector2(0, 5)  
        self.started = True
    def mover_izquierda(self):
        self.direction = Vector2(-5, 0) 
        self.started = True
    def mover_derecha(self):
        self.direction = Vector2(5, 0) 
        self.started = True
def generar_punto_verde():
    return Puntos(random.randint(0, ANCHO - 1), random.randint(0, ALTO - 1), 10, (0, 255, 0))
def main():
    punto1 = Puntos(ANCHO / 2, ALTO / 2, 20, (255, 0, 0))
    puntos_azules = [Puntos(random.randint(0, ANCHO - 1), random.randint(0, ALTO - 1), 20, (0, 0, 255)) for _ in range(5)]
    puntos_verdes = []
    puntos_azules_timer = 0
    puntos_verdes_timer = 0
    fps = pygame.time.Clock()
    while True:
        fps.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    punto1.mover_arriba()
                if event.key == pygame.K_DOWN:
                    punto1.mover_abajo()
                if event.key == pygame.K_LEFT:
                    punto1.mover_izquierda()
                if event.key == pygame.K_RIGHT:
                    punto1.mover_derecha()
        punto1.move()
        for punto_azul in puntos_azules:
            punto_azul.move()
            if pygame.time.get_ticks() - puntos_verdes_timer >= 10000:
                punto_azul.mover_aleatoriamente()
            elif not punto1.check_collision(punto_azul):
                WIN.fill((2, 25, 75))
                direccion_al_rojo = punto1.body[0] - punto_azul.body[0]
                direccion_al_rojo.normalize_ip()
                punto_azul.direction = direccion_al_rojo * 2  
            if punto1.check_collision(punto_azul):
                punto1.aumentar_tamano()
                nuevo_punto_azul = punto_azul.crear_nuevo_punto()
                puntos_azules.append(nuevo_punto_azul)
        if pygame.time.get_ticks() - puntos_verdes_timer > 10000 and len(puntos_verdes) < 2:
            if len(puntos_azules) >= 1:
             puntos_verdes.append(generar_punto_verde())
             puntos_verdes_timer = pygame.time.get_ticks()
            else: 
             print("Ganaste")
        for punto_verde in puntos_verdes:
            punto_verde.mover_aleatoriamente()
            if punto1.check_collision(punto_verde):
                WIN.fill((200, 2, 2))
                punto1.aumentar_tamano()
                puntos_verdes.remove(punto_verde)
                puntos_azules_timer = pygame.time.get_ticks()
                puntos_azules = puntos_azules[:len(puntos_azules)//2]
        if pygame.time.get_ticks() - puntos_azules_timer < 5000:
            for punto_azul in puntos_azules:
                punto_azul.mover_aleatoriamente()
        pygame.draw.circle(WIN, punto1.color, (int(punto1.body[0].x), int(punto1.body[0].y)), int(punto1.size))
        for punto_azul in puntos_azules:
            pygame.draw.circle(WIN, punto_azul.color, (int(punto_azul.body[0].x), int(punto_azul.body[0].y)), int(punto_azul.size))
        for punto_verde in puntos_verdes:
            pygame.draw.circle(WIN, punto_verde.color, (int(punto_verde.body[0].x), int(punto_verde.body[0].y)), int(punto_verde.size))
        pygame.display.update()
        if len(puntos_azules) >= 100:
            print("perdiste")
            time.sleep(1)
            pygame.quit()
            quit()
if __name__ == "__main__":
    main()
