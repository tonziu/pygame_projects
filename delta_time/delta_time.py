# This program implements and visualize the delta 
# time concept for objects movement.
#
# Delta time is the amount of time from the last 
# frame to the current frame.
#
# When the update function that regulates the movements 
# of an object takes into account the delta time, the
# movement will be time based instead of frame based.
#
# To test this concept, launch the application and press
# the spacebar to make the rectangle start moving. Then try 
# to change the FPS and you will notice that the total time 
# spent for reaching the corner of the window is fixed. Then try
# to do the same but removing the delta time variable in 
# the update of the rectangle. You will notice that the time
# will change accordingly to the FPS change.
#
# Moreover, the target fps variable makes the application 
# frame independent in case of frame rate drops. These are 
# the basic functionalities for regulating the movements of objects.
#
# Author: Tony De Corso

import pygame
import time

pygame.init()

ASPECT_RATIO = 16 / 9
WIN_H = 360
WIN_W = int(ASPECT_RATIO * WIN_H)

FPS = 60
TARGET_FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Text:
    def __init__(self, canvas, fontstring, color, size, x, y):
        self.font = pygame.font.SysFont(fontstring, size)
        self.canvas = canvas
        self.fontstring = fontstring
        self.size = size
        self.x = x
        self.y = y
        self.color = color
       
    
    def render(self, textstring):
        self.surface = self.font.render(textstring, 1, self.color)
        self.canvas.blit(self.surface, (self.x, self.y))



class Rectangle:
    def __init__(self, canvas, width, height, color):
        self.canvas = canvas
        self.surface = pygame.Surface((width, height)).convert()
        self.surface.fill(color)
        self.width = width
        self.height = height
        self.x = 0
        self.y = WIN_H / 2
        self.velocity = 5
        self.color = color
        self.walking = 0
        
    def render(self):
        self.canvas.blit(self.surface, (self.x, self.y))
         
class App:
    def __init__(self, width = WIN_W, height = WIN_H):
        self.window = pygame.display.set_mode((width, height))
        self.width = width
        self.height = height
        self.background = pygame.Surface((width, height)).convert()
        self.background.fill(WHITE)
        self.FPS = FPS
        self.clock = pygame.time.Clock()
        self.running = 1
        self.rectangle = Rectangle(self.window, 50, 50, BLACK)
        self.timer_text = Text(self.window, 'segoeui', BLACK, 32, 50, 50)
        self.timer = 0

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not self.rectangle.walking:
                        self.rectangle.walking = 1
                        self.rectangle.x = 0
                        self.timer = 0

        return 1

    def _update(self, dt):
        if self.rectangle.walking:
            self.timer += dt
            self.rectangle.x += self.rectangle.velocity * dt * TARGET_FPS
            if (self.rectangle.x >= self.width - self.rectangle.width):
                self.rectangle.x = self.width - self.rectangle.width
                self.rectangle.walking = 0


    def _render(self):
        self.window.blit(self.background, (0, 0))
        self.timer_text.render('Total time: ' + str(round(self.timer, 5)))
        self.rectangle.render()
        pygame.display.update()

    def run(self):
        prev_time = time.time()
        while self.running:
            self.clock.tick(self.FPS)
            now = time.time()
            dt = now - prev_time
            prev_time = now
            self.running = self._check_events()
            self._update(dt)
            self._render()

        pygame.quit()


if __name__ == "__main__":
    app = App()
    app.run()
