import pygame


class Model():

    def __init__(self, screen, world, render):
        self.screen = screen

        self.lineWide = 4
        self.color = (0, 0, 0)
        self.wide = 10
        self.high = 10

    def draw_line(self, pos1, pos2):
        pygame.draw.line(self.screen, 0, pos1, (pos2[0], pos1[1]), self.lineWide)

    def draw_rect(self, pos):
        pygame.draw.rect(self.screen, self.color, (pos[0] - self.x, pos[1] - self.y, self.wide, self.high))
        self.world.append_line((pos, (pos[0] + self.wide, pos[1])))
        self.world.append_line((pos, (pos[0], pos[1] + self.high)))
        self.world.append_line(((pos[0] + self.wide, pos[1] + self.high), (pos[0] + self.wide, pos[1])))
        self.world.append_line(((pos[0] + self.wide, pos[1] + self.high), (pos[0], pos[1] + self.high)))

    # def grid(self):

    # def hero_spawn(self):
