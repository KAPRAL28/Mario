import sys

import controls
import pygame

from colonna import Colonna
from mario import Mario

H = 576
W = 1024

pygame.init()
screen = pygame.display.set_mode((W, H))  # экран
ava_mario = pygame.image.load('images/mario_icon.png')  # аватарка игры
background = pygame.image.load('images/map.png')  # задний фон (карта)

mario = Mario(screen)

big_colonna = Colonna(background, pygame.image.load('images/colonna.png').convert_alpha())

pygame.display.set_icon(ava_mario)  # установка аватарки
pygame.display.set_caption('Mario')  # название игры

jump = 19
move = jump + 1
ground = H - 128

FPS = 60
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        """выход из игры"""
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:  # вправо
                mario.mright = True
            elif event.key == pygame.K_a:  # влево
                mario.mleft = True
            elif event.key == pygame.K_SPACE and mario.rect.bottom == ground:
                move = -jump
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                mario.mright = False
            elif event.key == pygame.K_a:
                mario.mleft = False
    if move <= jump:
        if mario.rect.bottom + move < ground:
            mario.rect.bottom += move
            if move < jump:
                move += 1
        else:
            mario.rect.bottom = ground
            move = jump + 1
    if abs(big_colonna.rect.top - mario.rect.bottom) < 12 and mario.rect.colliderect(
            big_colonna.rect):  # проверка стоит ли марио на платформе
        mario.rect.bottom = ground - big_colonna.rect.bottom + big_colonna.rect.top
        move = jump + 1
    else:
        if big_colonna.rect.top == mario.rect.bottom and not big_colonna.rect.left <= mario.centerx <= big_colonna.rect.right:
            mario.rect.bottom = ground
            move = jump + 1
    if abs(mario.rect.right - big_colonna.centerx) <= 6 and abs(big_colonna.rect.top - mario.rect.bottom) >= 10:
        # mario.rect.right = big_colonna.rect.left - 2
        mario.mright = False
    elif abs(mario.rect.left - big_colonna.centerx) <= 6 and abs(big_colonna.rect.top - mario.rect.bottom) >= 10:
        # mario.rect.left = big_colonna.rect.right + 2
        mario.mleft = False
    screen.blit(background, (mario.back, 0))
    mario.update_mario()
    mario.screen.blit(mario.image, mario.rect)
    controls.update_screen(screen, mario)
    big_colonna.screen.blit(big_colonna.image, big_colonna.rect)
    clock.tick(FPS)
    print(background)
    # print(big_colonna.rect.bottom)
    # print(big_colonna.centerx)
