# This module creates a window, it draws a ball that moves as soon
# as you try to get near it with the mouse.
#
# Written by: Tony De Corso

import pygame
import math
import random

pygame.init()

ASPECT_RATIO = 16/9
WIN_H = 720
WIN_W = int(ASPECT_RATIO * WIN_H)

RADIUS = 30

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

FPS = 30

class Circle:
    def __init__(self, canvas, radius = RADIUS, color = RED):
        self.canvas = canvas
        self.surface = pygame.Surface((radius, radius)).convert()
        self.radius = radius
        self.color = color
        self.surface.fill(self.color)
        self.center = [int(self.canvas.get_size()[0]/2), 
                       int(self.canvas.get_size()[1]/2)]


    def render(self):
        pygame.draw.circle(self.canvas, self.color, self.center, self.radius)

class App:
    def __init__(self, width = WIN_W, height = WIN_H):
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Can't touch me: demo")
        self.background = pygame.Surface((width, height)).convert()
        self.background.fill(WHITE)
        self.circle = Circle(self.window)
        self.FPS = FPS
        self.clock = pygame.time.Clock()
        self.running = 1

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
        return 1

    def _update(self):
        distance = math.dist(pygame.mouse.get_pos(), self.circle.center)
        if (distance > self.circle.radius*6):
            self.circle.color = GREEN
        else:
            self.circle.color = RED

    def _render(self):
        self.window.blit(self.background, (0, 0))
        self.circle.render()
        pygame.display.update()

    def run(self):
        while self.running:
            self.clock.tick(self.FPS)
            self.running = self._check_events()
            self._update()
            self._render()

        pygame.quit()

if __name__ == "__main__":
    app = App()
    app.run()
