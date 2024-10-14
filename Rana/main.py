import pygame
from pygame.math import Vector2
import random
import time
pygame.init()
ANCHO = 600
ALTO = 1000
WIN = pygame.display.set_mode((ANCHO, ALTO))
class Puntos:
    def __init__(self, x, y, size, image_path):
        self.body = [Vector2(x, y)]
        self.direction = Vector2(-5, 0)
        self.size = size
        self.scale_factor = 2.5
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (int(size * self.scale_factor), int(size * self.scale_factor)))
        self.started = False
    def move(self):
        new_head = self.body[0] + self.direction
        if new_head.x < 0:
            new_head.x = ANCHO
        self.body = [new_head] + self.body[:-1]
    def check_collision(self, other_point):
        return self.body[0].distance_to(other_point.body[0]) < (self.size + other_point.size) / 2
def main():
    punto1 = Puntos(ANCHO / 2, ALTO, 20, "rana.png")
    coches_azules = [Puntos(random.randint(ANCHO, ANCHO + 200), random.randint(0, ALTO - 1), 20, "cocherojo.png") for _ in
                     range(6)]
    coches_verdes = [Puntos(random.randint(ANCHO, ANCHO + 200), random.randint(0, ALTO - 1), 20, "bochogris.png") for _ in
                     range(10)]
    fps = pygame.time.Clock()
    while True:
        fps.tick(40)
        moved = False  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    punto1.direction = Vector2(0, -20)
                    moved = True
                elif event.key == pygame.K_DOWN:
                    punto1.direction = Vector2(0, 20)
                    moved = True
                elif event.key == pygame.K_LEFT:
                    punto1.direction = Vector2(-20, 0)
                    moved = True
                elif event.key == pygame.K_RIGHT:
                    punto1.direction = Vector2(20, 0)
                    moved = True
        if not moved:
            punto1.direction = Vector2(0, 0)
        punto1.move()
        for coche_azul in coches_azules:
            coche_azul.move()
        for coche_verde in coches_verdes:
            coche_verde.move()
            if punto1.check_collision(coche_azul) or punto1.check_collision(coche_verde):
                print("Perdiste")
                time.sleep(1)
                pygame.quit()
                quit()
        WIN.fill((255, 255, 255))
        WIN.blit(punto1.image, (
        int(punto1.body[0].x - punto1.size * punto1.scale_factor / 2), int(punto1.body[0].y - punto1.size * punto1.scale_factor / 2)))
        for coche_azul in coches_azules:
            WIN.blit(coche_azul.image, (
            int(coche_azul.body[0].x - coche_azul.size * coche_azul.scale_factor / 2),
            int(coche_azul.body[0].y - coche_azul.size * coche_azul.scale_factor / 2)))
        for coche_verde in coches_verdes:
            WIN.blit(coche_verde.image, (
            int(coche_verde.body[0].x - coche_verde.size * coche_verde.scale_factor / 2),
            int(coche_verde.body[0].y - coche_verde.size * coche_verde.scale_factor / 2)))
        pygame.display.update()
if __name__ == "__main__":
    main()
