import pygame

class player:
    x = 390
    y = 390

    def __init__(self):
        self.x, self.y = 390, 390
        self.speed = 3
    
    def draw(self, screen):
        player.x = self.x
        player.y = self.y
        rect = pygame.Rect(self.x, self.y, 20, 20)
        pygame.draw.rect(screen, (100,100,0), rect)

    def movement(self, key):
        if key[pygame.K_a]:
            self.x -= self.speed
        if key[pygame.K_d]:
            self.x += self.speed
        if key[pygame.K_w]:
            self.y -= self.speed
        if key[pygame.K_s]:
            self.y += self.speed

    def shooting(self, bullet):
        if pygame.mouse.get_pressed()[0]:
            bullet.color = (255,0,0)
        elif not pygame.mouse.get_pressed()[0]:
            bullet.color = (255,255,255)
