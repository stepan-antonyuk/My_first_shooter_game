import pygame

from world import World
from hero import Hero
from editor import Editor
from render import Renderer

FPS = 60
HOR_SPEED = 12
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode(flags=pygame.FULLSCREEN)
done = False
moving = False
dragging = False

world = World(surface_altitudes=[], blocks=[], bounce=0)
hero = Hero(world=world, x=960, y=400, speed=15, velocity=15, ClimbSpeed=5)
render = Renderer(screen, hero, x=0, y=0)
editor = Editor(screen, world, render, hero)

GameMode = False
MapMode = True

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True

    pressed = pygame.key.get_pressed()

    screen.fill((255, 255, 255))

    dragging = False

    GameMode = editor.on_pressed(pygame.key.get_pressed())
    editor.mode.before()
    # if not moving:
    if pygame.mouse.get_pressed()[0]:
        editor.mode.on_left_pressed()
        dragging = True
    else:
        editor.mode.on_left_released()

    if pressed[pygame.K_LEFT]:
        editor.mode.k_left()
    elif pressed[pygame.K_RIGHT]:
        editor.mode.k_right()

    if pressed[pygame.K_UP]:
        editor.mode.k_up()
    elif pressed[pygame.K_DOWN]:
        editor.mode.k_down()

    # moving = False
    # if not dragging:
    #     if pressed[pygame.K_LEFT]:
    #         render.horizontal_move(-1)
    #         moving = True
    #     elif pressed[pygame.K_RIGHT]:
    #         render.horizontal_move(1)
    #         moving = True
    #
    #     if pressed[pygame.K_UP]:
    #         render.vertical_move(-1)
    #         moving = True
    #     elif pressed[pygame.K_DOWN]:
    #         render.vertical_move(1)
    #         moving = True

    # if GameMode:
    #     if pressed[pygame.K_RIGHT]:
    #         hero.move(world.RIGHT)
    #     elif pressed[pygame.K_LEFT]:
    #         hero.move(world.LEFT)
    #     hero.render_hero(screen)

    render.draw_ground_line(world.return_coordinate())
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
