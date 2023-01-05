import pygame
import math
import random
from player import *


class enemy:
    class melee:
        x = 0
        y = 0

        def __init__(self):
            self.x, self.y = random.randint(100,700), random.randint(100,700)
            self.speed = 1
            self.health = 100

        def draw(self, screen):
            enemy.x = self.x
            enemy.y = self.y
            rect = pygame.Rect(self.x, self.y, 20, 20)
            pygame.draw.rect(screen, (200,10,10), rect)

        def movement(self,move):
            angle_x = self.x - player.x
            angle_y = self.y - player.y
            angle = math.atan2(angle_y, angle_x)
            dx = self.speed * math.cos(angle)
            dy = self.speed * math.sin(angle)
            self.x -= dx 
            self.y -= dy        
            self.x -= move[0]
            self.y -= move[1]
            
