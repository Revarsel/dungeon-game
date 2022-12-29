import pygame
from player import *
import math

class bullet:
    x = 0
    y = 0
    def __init__(self):
        self.speed = 10
        self.x = player.x
        self.y = player.y
        self.color = (255,255,255)

    def shoot(self, mousepos, screen):
        bullet.x = mousepos[0]
        bullet.y = mousepos[1]
        self.x = player.x
        self.y = player.y
        angle_x = mousepos[0]-self.x
        angle_y = mousepos[1]-self.y
        angle = math.atan2(angle_y,angle_x)
        dy = math.sin(angle) * self.speed
        dx = math.cos(angle) * self.speed
        while True:
            bullet.x += dx
            bullet.y += dy
            if bullet.x >= 800 or bullet.x <= 0 or bullet.y >= 800 or bullet.y <= 0:
                break
        #print(self.color)
        pygame.draw.line(screen, self.color, (self.x+10, self.y+10), (bullet.x, bullet.y))