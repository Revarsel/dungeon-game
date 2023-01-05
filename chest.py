import pygame
import random
from weapon import weapon_list

class chest:
    def __init__(self):
        self.opened = 0
        self.x = random.randint(100,700)
        self.y = random.randint(100,700)
        self.tick = 0
        self.screen = 0
        self.contents = weapon_list[0]  #random.choice(weapon_list)
        self.color = (20,50,100)
        self.rect = pygame.Rect(self.x, self.y, 40, 30)

    def draw(self, screen, move):
        if self.opened != 2:
            self.screen = screen
            self.x -= move[0]
            self.y -= move[1]
            self.rect = pygame.Rect(self.x, self.y, 40, 30)
            pygame.draw.rect(self.screen, self.color, self.rect)

    def collide(self, Player, tick):
        if self.opened == 0:
            self.tick = tick
            if pygame.Rect.colliderect(self.rect, Player.rect):
                self.opened = 1
                return True

    def update(self, tick):
        if self.opened == 1:
            self.color = (100,100,50)
            if tick-self.tick >= 5000:
                self.opened = 2

    class weapon_drop:
        def __init__(self, x, y, contents, screen):
            self.x = x+15
            self.y = y+40
            self.visible = True
            self.contents = contents
            self.screen = screen
            self.rect = pygame.Rect(0,0,10,10)

        def draw(self, move):
            if self.visible == True:
                self.x -= move[0]
                self.y -= move[1]
                self.rect = pygame.Rect(self.x, self.y, 10, 10)
                pygame.draw.rect(self.screen, (20,90,255), self.rect)

        def collide(self, player):
            if pygame.Rect.colliderect(self.rect, player.rect):
                self.visible = False
                return True
