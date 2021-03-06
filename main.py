import pygame

import settings
from action import DoneAction
from translator import Translator
from universe import Universe

from coords import CoordConverter
from Render import Renderer


# from world import World
# from hero import Hero
# from editor import Editor


clock = pygame.time.Clock()
pygame.init()

# pygame.display.init()  # initialization of display
display = (1000,1000)  # display
screen = pygame.display.set_mode(display)
surface = pygame.Surface(display)

scale = (1,1)
moving = False
dragging = False


# world = World(surface_altitudes=[(0,1080)], blocks=[], bounce=0)
# hero = Hero(world=world, x=960, y=400, speed=15, velocity=15, ClimbSpeed=5)
# render = Renderer(surface, hero, x=0, y=0)
# editor = Editor(screen, world, render, hero)

# GameMode = False
# MapMode = True


universe = Universe()
coords = CoordConverter(scale, ((0,0), display))
render = Renderer(coords, screen)


def main_loop():
    translator = Translator(settings.TRANSLATION_MAP, DoneAction())

    def collect_actions():
        result = translator.translate_pressed(universe.mode)
        for event in pygame.event.get():
            universe.mouseCoord = pygame.mouse.get_pos()
            result += translator.translate_event(universe.mode, event)
        return result

    while True:
        actions = collect_actions()

        if any(action.is_done() for action in actions):
            break

        for action in actions:
            action.change_universe(universe)

        screen.fill((255,255,255))
        render.draw(universe.surface_altitudes)
        pygame.display.flip()

        universe.update()
        # render_universe()
        clock.tick(settings.FPS)


if __name__ == "__main__":
    main_loop()
    pygame.quit()
