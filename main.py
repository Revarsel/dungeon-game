import pygame
from player import *
from ray import *
from effects import *

screen = pygame.display.set_mode((800,800))

def main():
    run = True
    Clock = pygame.time.Clock()
    Player = player()
    Ray = ray()
    ray_effect_list = []
    mouse_0 = 0
    move_list = [0,0]
    while run:
        Clock.tick(60)
        screen.fill((30,30,30))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # All variables and all here
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pos()

        # All functions here     
        Player.movement(keys, move_list)
        Ray.shoot(mouse, screen)

        if pygame.mouse.get_pressed()[0]:
            if mouse_0 == 0:
                ray_effect_list.append(ray_effect(screen, Player.x+10, Player.y+10, Ray.endx, Ray.endy))
                mouse_0 = 1
        elif not pygame.mouse.get_pressed()[0]:
            mouse_0 = 0

        for i in ray_effect_list:
            i.draw(move_list)
            if i.width == 0:
                ray_effect_list.remove(i)
        
        Player.draw(screen)

        # Update display
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()