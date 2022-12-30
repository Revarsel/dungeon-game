import pygame

class ray_effect:
    def __init__(self, screen, start_x, start_y, end_x, end_y):
        self.width = 12
        self.decrease = 10   # color decrease
        self.screen = screen
        self.sx = start_x
        self.sy = start_y
        self.ex = end_x
        self.ey = end_y
        self.color = [224,117,67]

    def draw(self, move_list):
        self.sx -= move_list[0]
        self.sy -= move_list[1]
        self.ex -= move_list[0]
        self.ey -= move_list[1]
        if self.width >= 0:
            pygame.draw.line(self.screen, self.color, (self.sx, self.sy), (self.ex, self.ey), self.width)
            if self.color[0]-self.decrease <= 0:
                pass
            else:
                self.color[0] -= self.decrease

            if self.color[1]-self.decrease <= 0:
                pass
            else:
                self.color[1] -= self.decrease

            if self.color[2]-self.decrease <= 0:
                pass
            else:
                self.color[2] -= self.decrease
                
            self.width -= 1
    