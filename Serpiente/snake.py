import pygame
from pygame.math import Vector2
import random
import os
pygame.init()
vidas = 3
ANCHO = 1000
ALTO = 1000
SNAKE_BODY = pygame.transform.scale(pygame.image.load(os.path.join(r"./images/snakebody.png")), (20, 20))
APPLE = pygame.transform.scale(pygame.image.load(os.path.join(r"./images/manzana.png")), (20, 20))
SNAKE_HEAD = []
for x in range(1, 5):
    SNAKE_HEAD += [pygame.transform.scale(pygame.image.load(os.path.join(r"./images/SnakeHead" + str(x) + ".png")),
                                          (20, 20))]
EAT_SOUND = pygame.mixer.Sound("coin.wav")
WIN = pygame.display.set_mode((ANCHO, ALTO))
SCORE_TEXT = pygame.font.SysFont("Russo One", 15)
class Snake:
    def __init__(self):
        self.body = [Vector2(ANCHO / 2, ALTO / 2), Vector2(ANCHO / 2, ALTO / 2 + 10), Vector2(ANCHO / 2, ALTO / 2 + 20)]
        self.direction = Vector2(0, -20)
        self.add = False
        self.started = False
    def draw(self):
        for bloque in self.body:
            WIN.blit(SNAKE_BODY, (bloque.x, bloque.y))
        if self.direction == Vector2(0, -20):
            WIN.blit(SNAKE_HEAD[0], (self.body[0].x, self.body[0].y))
        if self.direction == Vector2(0, 20):
            WIN.blit(SNAKE_HEAD[2], (self.body[0].x, self.body[0].y))
        if self.direction == Vector2(20, 0):
            WIN.blit(SNAKE_HEAD[1], (self.body[0].x, self.body[0].y))
        if self.direction == Vector2(-20, 0):
            WIN.blit(SNAKE_HEAD[3], (self.body[0].x, self.body[0].y))
    def move(self):
        if self.add:
            body_copy = self.body
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.add = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
    def move_up(self):
        self.direction = Vector2(0, -20)
        self.started = True
    def move_down(self):
        self.direction = Vector2(0, 20)
        self.started = True
    def move_right(self):
        self.direction = Vector2(20, 0)
        self.started = True
    def move_left(self):
        self.direction = Vector2(-20, 0)
        self.started = True
    def die(self):
        global vidas
        if self.body[0].x >= ANCHO + 20 or self.body[0].y >= ALTO + 20 or self.body[0].x <= -20 or self.body[0].y <= -20:
            vidas -= 1
            return True
        for i in self.body[1:]:
            if self.body[0] == i:
                vidas -= 1
                return True
        return False
class Apple:
    def __init__(self):
        self.generate()
    def draw(self):
        WIN.blit(APPLE, (self.pos.x, self.pos.y))
    def generate(self):
        self.x = random.randrange(0, ANCHO / 20)
        self.y = random.randrange(0, ALTO / 20)
        self.pos = Vector2(self.x * 20, self.y * 20)
    def check_collision(self, snake):
        if snake.body[0] == self.pos:
            self.generate()
            snake.add = True
            return True
        for bloque in snake.body[1:]:
            if self.pos == bloque:
                self.generate()
        return False
def main():
    global vidas
    snake = Snake()
    apple = Apple()
    score = 0
    fps = pygame.time.Clock()
    while True:
        fps.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.move_up()
                if event.key == pygame.K_DOWN:
                    snake.move_down()
                if event.key == pygame.K_RIGHT:
                    snake.move_right()
                if event.key == pygame.K_LEFT:
                    snake.move_left()
        WIN.fill((175, 215, 70))
        snake.draw()
        apple.draw()
        if snake.started:
            snake.move()
        if apple.check_collision(snake):
            score += 1
            EAT_SOUND.play()
        if snake.die():
            if vidas > 0:
                snake = Snake()
            else:
                quit()
        text = SCORE_TEXT.render("Score: {} Vidas: {}".format(score, vidas), 1, (255, 255, 255))
        WIN.blit(text, (ANCHO - text.get_width() - 20, 20))
        pygame.display.update()
main()
#python3 snake.py
 