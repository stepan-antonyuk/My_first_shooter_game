# import pygame
# import math


class World:
    LEFT = -1
    RIGHT = 1

    def __init__(self, surface_altitudes, bounce):
        self.surface_altitudes = surface_altitudes
        self.bounce = bounce

    # def check_duplicates(self,pos1, pos2):
    #     for pos in self.surface_altitudes

    def append_line(self, pos):
        if self.check_for_duplicate(pos):
            self.surface_altitudes.append(pos)

    def append_rect(self, pos, wide, high):
        self.append_line((pos, (pos[0] + wide, pos[1])))
        self.append_line((pos, (pos[0], pos[1] + high)))
        self.append_line(((pos[0] + wide, pos[1] + high), (pos[0] + wide, pos[1])))
        self.append_line(((pos[0] + wide, pos[1] + high), (pos[0], pos[1] + high)))

    def return_coordinate(self):
        return self.surface_altitudes

    def change_surface(self, coordinates):
        self.surface_altitudes = coordinates

    def check_for_duplicate(self, pos):
        for posM in self.surface_altitudes:
            if posM == pos:
                return False
        return True

    # def if_on_line(self, pos):
    #     for i in self.surface_altitudes:
    #         if i[0] == pos or i[1] == pos:
