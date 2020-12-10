#!/usr/bin/env python

import random
import sys

import pygame
from pygame.locals import *

pygame.init()

size = w, h = (800, 800)

screen = pygame.display.set_mode(size)

bg = pygame.image.load('images/table.jpg')
bg = pygame.transform.scale(bg, (800, 200))

def get_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

block_size = b_w, b_h = (50, 50)

# block = pygame.Rect((20, 550), block_size)
color = get_random_color()
block = pygame.Rect((20, 550), block_size)


while True:
    screen.blit(bg, (0, 600))  # fixed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == KEYDOWN and event.key == K_q:
            sys.exit()
        if event.type == KEYDOWN and event.key == K_UP:
            x = block.x
            y = block.y
            block.move_ip(x, y+1)
    pygame.draw.rect(screen, color, block, 2)
    pygame.display.update()

