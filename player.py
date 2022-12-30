import pygame
from effects import *

class player:
    x = 390
    y = 390

    def __init__(self):
        self.x, self.y = 390, 390
        self.speed = 10
    
    def draw(self, screen):
        player.x = self.x
        player.y = self.y
        rect = pygame.Rect(self.x, self.y, 20, 20)
        pygame.draw.rect(screen, (63,209,148), rect)

    def movement(self, key, move_list):
        if key[pygame.K_d]:
            move_list[0] = self.speed
        if key[pygame.K_a]:
            move_list[0] = -self.speed
        if key[pygame.K_w]:
            move_list[1] = -self.speed
        if key[pygame.K_s]:
            move_list[1] = self.speed
        if not key[pygame.K_a] and not key[pygame.K_d]:
            move_list[0] = 0
        if not key[pygame.K_w] and not key[pygame.K_s]:
            move_list[1] = 0

