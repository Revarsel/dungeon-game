import pygame
import math

from weapon import *

class player:
    x = 390
    y = 390

    def __init__(self):
        self.x, self.y = 390, 390
        self.speed = 2
        self.weapon = weapon.hand()
        self.camera_speed = 1
        self.tick = 0
        self.rect = pygame.Rect(self.x, self.y, 20, 20)
    
    def draw(self, screen):
        player.x = self.x
        player.y = self.y
        self.rect = pygame.Rect(self.x, self.y, 20, 20)
        pygame.draw.rect(screen, (63,209,148), self.rect)

    def movement(self, key, move_list):
        if key[pygame.K_w]:
            self.y -= self.speed
        elif key[pygame.K_s]:
            self.y += self.speed

        if key[pygame.K_a]:
            self.x -= self.speed
        elif key[pygame.K_d]:
            self.x += self.speed
        
        distance = math.sqrt(((390-self.x)**2)+(390-self.y)**2)

        angle_x = self.x-390

        angle_y = self.y-390

        angle = math.atan2(angle_y, angle_x)

        force = (1/16)*self.camera_speed*distance

        self.x -= (force * math.cos(angle)*self.camera_speed)
        self.y -= (force * math.sin(angle)*self.camera_speed)

        move_list[0] = (force * math.cos(angle))
        move_list[1] = (force * math.sin(angle))

    def dash(self):
        if pygame.mouse.get_pressed()[2]:
            self.speed = 5
        else:
            self.speed = 2

    def update(self, i):
        self.weapon = i.contents

