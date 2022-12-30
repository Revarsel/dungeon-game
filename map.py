import pygame

class map:
    def __init__(self):
        self.originx = 200
        self.originy = 200

    def draw(self, screen, move):
        self.originx -= move[0]
        self.originy -= move[1]
        rect1 = pygame.Rect(self.originx, self.originy, 600, 15)
        rect2 = pygame.Rect(self.originx+600, self.originy, 15, 615)
        rect3 = pygame.Rect(self.originx, self.originy+600, 600, 15)
        rect4 = pygame.Rect(self.originx, self.originy, 15, 615)
        pygame.draw.rect(screen, (150,140,200), rect1)
        pygame.draw.rect(screen, (150,140,200), rect2)
        pygame.draw.rect(screen, (150,140,200), rect3)
        pygame.draw.rect(screen, (150,140,200), rect4)
