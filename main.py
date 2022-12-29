import pygame
from player import *
from bullet import *

screen = pygame.display.set_mode((800,800))

def main():
    run = True
    Clock = pygame.time.Clock()
    Player = player()
    Bullet = bullet()
    while run:
        Clock.tick(60)
        screen.fill('black')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        # All variables and all here
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pos()

        # All functions here        
        Player.movement(keys)
        Player.shooting(Bullet)
        Bullet.shoot(mouse, screen)
        Player.draw(screen)

        # Update display
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()