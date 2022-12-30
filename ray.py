import pygame
from player import *
import math

class ray:
    x = 0
    y = 0
    def __init__(self):
        self.speed = 10
        self.x = player.x
        self.y = player.y
        self.endx = ray.x
        self.endy = ray.y
        self.color = (41,135,96)

    def shoot(self, mousepos, screen):
        self.endx = mousepos[0]
        self.endy = mousepos[1]
        self.x = player.x
        self.y = player.y
        angle_x = mousepos[0]-self.x
        angle_y = mousepos[1]-self.y
        angle = math.atan2(angle_y,angle_x)
        dy = math.sin(angle) * self.speed
        dx = math.cos(angle) * self.speed
        while True:
            self.endx += dx
            self.endy += dy
            if self.endx >= 800 or self.endx <= 0 or self.endy >= 800 or self.endy <= 0:
                break
        pygame.draw.line(screen, self.color, (self.x+10, self.y+10), (self.endx, self.endy))