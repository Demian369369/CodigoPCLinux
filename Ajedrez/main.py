import pygame
import sys
from colors import Colors
pygame.init()
title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Record", True, Colors.white)
game_over_surface = title_font.render("GAME OVER", True, Colors.white)
score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)
screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Chess")
clock = pygame.time.Clock()
GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(Colors.dark_blue)
    screen.blit(score_surface, score_rect)
    pygame.display.update()
    clock.tick(60)
#python3 main.py
#if event.type == pygame.KEYDOWN: