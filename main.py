import pygame
from effects import *
from player import *
from ray import *
from map import *
from enemy import *
from chest import *

screen = pygame.display.set_mode((800,800))

def main():
    run = True
    Clock = pygame.time.Clock()
    Player = player()
    Ray = ray()
    Map = map()
    Chest = chest()
    ray_effect_list = []
    weapon_drop_list = []
    move_list = [0,0]
    enemy_list = []
    chest_list = []
    while run:
        Clock.tick(60)
        screen.fill((30,30,30))
        current_tick = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # All variables ---------------------------------------------------------------------------------------------------------------------------------- |
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pos()


        # Map functions ---------------------------------------------------------------------------------------------------------------------------------- |
        Map.draw(screen, move_list)


        # Drop functions --------------------------------------------------------------------------------------------------------------------------------- |
        for i in weapon_drop_list:
            i.collide(Player)
            if i.collide(Player):
                Player.update(i)
                weapon_drop_list.remove(i)
            i.draw(move_list)

        
        # Chest functions -------------------------------------------------------------------------------------------------------------------------------- |
        for i in chest_list:
            if i.collide(Player, current_tick) == True:
                if i.opened == 1:
                    weapon_drop_list.append(i.weapon_drop(i.x, i.y, i.contents, screen))
            i.draw(screen, move_list)
            i.update(current_tick)
        
        if len(chest_list) > 1:
            pass
        else:
            chest_list.append(chest())


        # Mouse press functions -------------------------------------------------------------------------------------------------------------------------- |
        if pygame.mouse.get_pressed()[0]:
            if current_tick-Player.tick >= Player.weapon.reload*1000:
                for l in range(0, len(enemy_list)):
                    i = enemy_list[l]
                    if Player.weapon.name >= weapon.ray_gun.name:
                        if Ray.collision(i.x, i.y) == True:
                            i.health -= Player.weapon.damage
                            i.speed = 1
                            if i.health <= 0:
                                enemy_list[l] = 0
                        ray_effect_list.append(ray_effect(screen, Player.x+10, Player.y+10, Ray.endx, Ray.endy))
                    else:
                        pass
                Player.tick = current_tick


        # Ray effects functions -------------------------------------------------------------------------------------------------------------------------- |
        for i in ray_effect_list:
            i.draw(move_list)
            if i.width == 0:
                ray_effect_list.remove(i)


        # Enemy functions -------------------------------------------------------------------------------------------------------------------------------- |
        if len(enemy_list) <= 1:
            enemy_list.append(enemy.melee())

        for i in enemy_list:
            if i == 0:
                enemy_list.remove(i)

        for i in enemy_list:
            if i == 0:
                pass
            else:
                i.movement(move_list)
                i.draw(screen)
                Ray.collision(i.x, i.y)

        
        # Player functions ------------------------------------------------------------------------------------------------------------------------------- |
        if Player.weapon.name == weapon.ray_gun.name:
            Ray.shoot(mouse[0], mouse[1], Player.x, Player.y, screen)
            Ray.color = (41,135,96)
        Player.movement(keys, move_list)
        Player.dash()
        Player.draw(screen)


        # Update display
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()