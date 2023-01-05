import pygame

class map:
    def __init__(self):
        self.originx = 200
        self.originy = 200
        self.length = 800
        self.width = 20
        self.color = (60,60,60)
        self.rect1 = pygame.Rect(self.originx, self.originy, self.length, self.width)
        self.rect2 = pygame.Rect(self.originx+self.length, self.originy, self.width, self.length+self.width)
        self.rect3 = pygame.Rect(self.originx, self.originy+self.length, self.length, self.width)
        self.rect4 = pygame.Rect(self.originx, self.originy, self.width, self.length+self.width)

    def draw(self, screen, move):
        self.originx -= move[0]
        self.originy -= move[1]
        self.rect1 = pygame.Rect(self.originx, self.originy, self.length, self.width)
        self.rect2 = pygame.Rect(self.originx+self.length, self.originy, self.width, self.length+self.width)
        self.rect3 = pygame.Rect(self.originx, self.originy+self.length, self.length, self.width)
        self.rect4 = pygame.Rect(self.originx, self.originy, self.width, self.length+self.width)
        pygame.draw.rect(screen, self.color, self.rect1)
        pygame.draw.rect(screen, self.color, self.rect2)
        pygame.draw.rect(screen, self.color, self.rect3)
        pygame.draw.rect(screen, self.color, self.rect4)
