import os
import string
import sys
from collections import defaultdict

import pygame
from pygame.locals import *

from block import Block
from build_blocks import build_blocks
from states import STATES, CLEAR, ON_TABLE, ON
# check for conflicting states

def print_blocks(blocks):
    for b in blocks.values():
        print(b)

def get_blocks(num):
    blocks = defaultdict(Block)

    for name in string.ascii_uppercase[:n]:
        blocks[name] = Block(name)

    return blocks

def get_states(stack, final=False):
    if final:
        which = 'Final'
    else:
        which = 'Initial'

    print(f'Enter {which} States of the blocks: [enter `done` when completed]')
    while True:
        state, *args = input().split()
        if state == 'done':
            break
        if state == 'clear':
            stack.append(CLEAR(*args))
        elif state == 'ontable':
            stack.append(ON_TABLE(*args))
        elif state == 'on':
            stack.append(ON(*args))


def start_game(num):
    pygame.init()

    black = (0, 0, 0)
    csize = width, height = (800, 800)

    build_blocks(num)

    game_blocks = {s: pygame.image.load(f'blocks/{s}.png') for s in string.ascii_uppercase[:num]}

    bg = pygame.image.load('images/table.jpg')
    bg = pygame.transform.scale(bg, csize)

    screen = pygame.display.set_mode(csize)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_q):
                sys.exit()
        screen.fill(black)
        screen.blit(bg, (0, 0))
        pygame.display.flip()

if __name__ == '__main__':
    n = int(input('enter no. of blocks: '))


    blocks = get_blocks(n)

    STATES.blocks = blocks
    stack = []
    get_states(stack)

    for state in stack:
        state.construct()

    gstack = []

    get_states(gstack, final=True)

    gstack = sorted(gstack, key=lambda x: x.priority, reverse=True)

    width, _ = os.get_terminal_size()
    print('-' * width)
    print('FINAL STATES:', gstack)

    print('-' * width)
    print_blocks(blocks)
    print('-' * width)
    while len(gstack) != 0:
        state = gstack.pop()
        if state.is_satisfied:
            print(f'>> {state} satisfied')
            continue
        print(f'<< {state}')
        state.work()
    print('-' * width)

    print_blocks(blocks)

    start_game(n)
