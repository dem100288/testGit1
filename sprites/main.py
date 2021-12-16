import os
import sys
import random
import sprites.util
import sprites.Bomb as bomb_m

import pygame

# Изображение не получится загрузить
# без предварительной инициализации pygame
pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)


bomb_image = sprites.util.load_image("bomb.png")
all_sprites = pygame.sprite.Group()
for i in range(50):
# можно сразу создавать спрайты с указанием группы
    bomb_m.Bomb(all_sprites)

running = True
while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # задаём случайное местоположение бомбочке
    #for bomb in all_sprites.sprites():
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()
