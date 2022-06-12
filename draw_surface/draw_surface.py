# This module creates a window and draws a red rectangle
# on the screen.
# Written by: Tony De Corso

import pygame

pygame.init()

WIN_H = 720
WIN_W = 16/9 * WIN_H
WHITE = (255, 255, 255)
RED = (255, 0, 0)

def create_window(width = WIN_W, height = WIN_H):
    window = pygame.display.set_mode((width, height))
    return window

def create_background(width = WIN_W, height = WIN_H, color = WHITE):
    background = pygame.Surface((width, height))
    background = background.convert()
    background.fill(color)
    return background

def create_rectangle(width, height, color):
    rectangle = pygame.Surface((width, height)).convert()
    rectangle.fill(color)
    return rectangle

def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return 0
    return 1

def main_loop(FPS):
    running = 1
    clock = pygame.time.Clock()
    while running:
        clock.tick(FPS)
        running = check_events()
    pygame.quit()

def run():
    window = create_window()
    background = create_background()
    rectangle = create_rectangle(50, 50, RED)
    window.blit(background, (0, 0))
    window.blit(rectangle, (50, 50))
    pygame.display.flip()
    main_loop(60)

if __name__ == "__main__":
    run()

