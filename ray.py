import pygame
import math
from player import *

class ray:
    x = 0
    y = 0
    def __init__(self):
        self.speed = 20
        self.x = 0
        self.y = 0
        self.endx = 0
        self.endy = 0
        self.color = (41,135,96)

    def collision(self, enemx, enem_y):
        rect1 = pygame.Rect(enemx, enem_y, 20, 20)
        if rect1.clipline((self.x+10, self.y+10), (self.endx, self.endy)):
            self.color = (180,10,20)
            return True

    def shoot(self, end_x, end_y, start_x, start_y, screen):
        self.endx = end_x
        self.endy = end_y
        self.x = start_x
        self.y = start_y
        angle_x = end_x-self.x
        angle_y = end_y-self.y
        angle = math.atan2(angle_y,angle_x)
        dy = math.sin(angle) * self.speed
        dx = math.cos(angle) * self.speed
        while True:
            self.endx += dx
            self.endy += dy
            if self.endx > 800 or self.endx < 0 or self.endy > 800 or self.endy < 0:
                break
        pygame.draw.line(screen, self.color, (self.x+10, self.y+10), (self.endx, self.endy))