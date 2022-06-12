# This program opens a simple pygame window
# By default, the aspect ratio is 16/9, the 
# user can change the height  and the width ù
# will be calculated in respect to the aspect
# ratio. By default the window has a white 
# background color. 

import pygame

pygame.init()

ASPECT_RATIO = 16/9
WIN_H = 600
WIN_W = ASPECT_RATIO * WIN_H 
WHITE = (255, 255, 255)

def create_window(width = WIN_W, height = WIN_H):
    window = pygame.display.set_mode((width, height))
    return window

def set_background(window, color = WHITE):
    window.fill(WHITE)

def main_loop():
    while 1:
        pygame.display.update()
        check_events()

def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

if __name__ == "__main__":
    window = create_window()
    set_background(window)
    main_loop()


