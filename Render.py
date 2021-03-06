import pygame


class Renderer:

    def __init__(self, coords, screen):
        self.coords = coords
        self.screen = screen

    # TODO
    def draw(self, surface):
        for line in surface:
            if(self.coords.in_viewport(line)):
                pos1 = self.coords.from_universe(line[0])
                pos2 = self.coords.from_universe(line[1])
                pygame.draw.line(self.screen, (250,250,250), pos1, pos2)
