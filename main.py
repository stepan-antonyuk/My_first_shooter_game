import pygame

from action import *
from world import World
from hero import Hero
from editor import Editor
from render import Renderer

FPS = 60
HOR_SPEED = 12
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode(flags=pygame.FULLSCREEN)
surface = pygame.Surface((500, 500))
done = False
moving = False
dragging = False

world = World(surface_altitudes=[], blocks=[], bounce=0)
hero = Hero(world=world, x=960, y=400, speed=15, velocity=15, ClimbSpeed=5)
render = Renderer(surface, hero, x=0, y=0)
editor = Editor(screen, world, render, hero)

GameMode = False
MapMode = True

universe = Universe()

translation_map = {
    'game': {
        'key_pressed': {
            pygame.K_UP: JumpAction(),
            pygame.K_DOWN: DebugAction("CROUCH"),
        },
        'key_down': {
            pygame.K_e: ChangeModeAction("map")
        }
    },
    'map': {
        'key_pressed': {
            pygame.K_UP: DebugAction("Pressed UP"),
            pygame.K_DOWN: DebugAction("Pressed DOWN"),
        },
        'key_down': {
            pygame.K_e: ChangeModeAction("game")
        }
    }
}


def translate_event(mode, event):
    pressed = pygame.key.get_pressed()
    if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        return [DoneAction()]

    if event.type == pygame.KEYDOWN:
        action = translation_map.get(mode, {}).get('key_down', {}).get(event.key)
        if action:
            return [action]

    key_pressed = translation_map.get(mode, {}).get('key_pressed', {})
    return [action for key, action in key_pressed.items() if pressed[key]]


while not done:
    for event in pygame.event.get():
        universe.mouseCoord = pygame.mouse.get_pos()
        actions = translate_event(universe.mode, event)

        for action in actions:
            if action.is_done():
                done = True
            else:
                action.change_universe(unKiverse)

    universe.update()
    # render_universe()
    clock.tick(2)

# if False:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True
#         elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
#             done = True
#
#     pressed = pygame.key.get_pressed()
#
#     screen.fill((255, 255, 255))
#
#     dragging = False
#
#     surface.fill((255, 255, 255))
#
#     GameMode = editor.on_pressed(pygame.key.get_pressed())
#     editor.mode.before()
#     # if not moving:
#     if pygame.mouse.get_pressed()[0]:
#         editor.mode.on_left_pressed()
#         dragging = True
#     else:
#         editor.mode.on_left_released()
#
#     if pressed[pygame.K_LEFT]:
#         editor.mode.k_left()
#     elif pressed[pygame.K_RIGHT]:
#         editor.mode.k_right()
#
#     if pressed[pygame.K_UP]:
#         editor.mode.k_up()
#     elif pressed[pygame.K_DOWN]:
#         editor.mode.k_down()
#
#     # moving = False
#     # if not dragging:
#     #     if pressed[pygame.K_LEFT]:
#     #         render.horizontal_move(-1)
#     #         moving = True
#     #     elif pressed[pygame.K_RIGHT]:
#     #         render.horizontal_move(1)
#     #         moving = True
#     #
#     #     if pressed[pygame.K_UP]:
#     #         render.vertical_move(-1)
#     #         moving = True
#     #     elif pressed[pygame.K_DOWN]:
#     #         render.vertical_move(1)
#     #         moving = True
#
#     # if GameMode:
#     #     if pressed[pygame.K_RIGHT]:
#     #         hero.move(world.RIGHT)
#     #     elif pressed[pygame.K_LEFT]:
#     #         hero.move(world.LEFT)
#     #     hero.render_hero(screen)
#
#     render.draw_ground_line(world.return_coordinate())
#     screen.blit(surface, (300, 300))
#
#     pygame.display.flip()
#     clock.tick(FPS)

pygame.quit()
