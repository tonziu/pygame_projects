# This module creates a window, draws a black grid and creates a walking
# rectangle which walks stepping on the grid.
# 
# Written by: Tony De Corso

import pygame

pygame.init()

NCOLS = 16
NROWS = 9

ASPECT_RATIO = 16/9

WIN_H = int(40*NROWS)
WIN_W = int(ASPECT_RATIO * WIN_H)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

FPS = 10



class Rectangle:
    def __init__(self, canvas,
                 width = int(WIN_W/NCOLS), 
                 height = int(WIN_H/NROWS), 
                 color = RED):

        self.canvas = canvas
        self.surface = pygame.Surface((width, height)).convert()
        self.surface.fill(color)
        self.width = width
        self.height = height
        self.x = 0
        self.y = 0
        self.color = color
        self.col = 0
        self.row = 0

    def render(self):
        self.canvas.blit(self.surface, (self.width*self.col, self.height*self.row)) 

        
class App:
    def __init__(self, width = WIN_W, height = WIN_H):
        self.window = pygame.display.set_mode((width, height))
        self.width = width
        self.height = height
        pygame.display.set_caption("Walking Rectangle: demo")
        self.background = pygame.Surface((width, height)).convert()
        self.background.fill(WHITE)
        self.rectangle = Rectangle(self.window)
        self.running = 1
        self.clock = pygame.time.Clock()
        self.FPS = FPS
        self.ncols = NCOLS
        self.nrows = NROWS

    def _draw_grid(self):
        step_y = int(self.rectangle.height)
        step_x = int(self.rectangle.width)

        for y in range(step_y, self.height, step_y): # horizontal lines
            pygame.draw.line(self.window, BLACK, (0, y), (self.width, y))

        for x in range(step_x, self.width, step_x):  # vertical lines
            pygame.draw.line(self.window, BLACK, (x, 0), (x, self.height))


    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
        return 1

    def update(self):
        if (self.rectangle.col < self.ncols-1):
            self.rectangle.col += 1
        else:
            if (self.rectangle.row < self.nrows-1):
                self.rectangle.col = 0
                self.rectangle.row += 1
            else:
                self.rectangle.col = 0
                self.rectangle.row = 0
        

    def render(self):
        self.window.blit(self.background, (0, 0))
        self._draw_grid()
        self.rectangle.render()
        pygame.display.update()

    def run(self):
        while self.running:
            self.clock.tick(self.FPS)
            self.running = self._check_events()
            self.update()
            self.render()
        pygame.quit()

if __name__ == "__main__":
    app = App()
    app.run()
