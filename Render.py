import pygame
from coords import CoordConverter
import viewport


class Renderer:

    def __init__(self, display, hero, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.screenWidth = 1920
        self.screenHeight = 1080
        self.speed = 10
        self.lineWidth = 4
        self.width = 10
        self.height = 10
        self.gridWide = 30
        self.color = (0, 0, 0)
        self.hero = hero

    coords = CoordConverter((1, 1), ((0, 0), (1000, 1000)))

    # def in_viewport(self, line): # pos is in real coordinates(rc)
    #     (pos1, pos2) = line
    #     (xp1, yp1) = pos1
    #     (xp2, yp2) = pos2
    #     (xd, yd) = self.display
    #     if((0 <= xp1 <= xd) and (0 <= yp1 <= yd)) or ((0 <= xp2 <= xd) and (0 <= yp2 <= yd)):
    #         return True
    #     return False


    # def in_screen(self, surface):
    #     for line in surface:
    #         for point in line:


    # TODO
    # def draw(self):

