# This module creates a window, it draws a ball that moves as soon
# as you try to get near it with the mouse.
#
# Written by: Tony De Corso

import pygame
import math

pygame.init()

ASPECT_RATIO = 16/9
WIN_H = 720
WIN_W = int(ASPECT_RATIO * WIN_H)

RADIUS = 20

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

FPS = 120

class Circle:
    def __init__(self, canvas, radius = RADIUS, color = RED):
        self.canvas = canvas
        self.radius = radius
        self.color = color
        self.center = [int(self.canvas.get_size()[0]/2), 
                       int(self.canvas.get_size()[1]/2)]

    def render(self):
        pygame.draw.circle(self.canvas, self.color, self.center, self.radius)

class App:
    def __init__(self, width = WIN_W, height = WIN_H):
        self.window = pygame.display.set_mode((width, height))
        self.width = width
        self.height = height
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

        diff_x = pygame.mouse.get_pos()[0] - self.circle.center[0]
        diff_y = pygame.mouse.get_pos()[1] - self.circle.center[1]

        angle = math.atan2(diff_y, diff_x)
        
        if (distance < self.circle.radius*10):
            self.circle.center[0] -= math.cos(angle)*(1000/distance)
            self.circle.center[1] -= math.sin(angle)*(1000/distance)

        if (self.circle.center[0] + self.circle.radius > self.width):
            self.circle.center[0] = self.circle.radius * 7

        if (self.circle.center[1] + self.circle.radius > self.height):
            self.circle.center[1] = self.circle.radius * 7
        
        if (self.circle.center[0] < 0):
            self.circle.center[0] = self.width - self.circle.radius*7

        if (self.circle.center[1] < 0):
            self.circle.center[1] = self.height - self.circle.radius*7

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
