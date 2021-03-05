import pygame

from action import *
# from world import World
# from hero import Hero
# from editor import Editor
# from render import Renderer

FPS = 600
HOR_SPEED = 12
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode()
surface = pygame.Surface((500, 500))
moving = False
dragging = False

# world = World(surface_altitudes=[(0,1080)], blocks=[], bounce=0)
# hero = Hero(world=world, x=960, y=400, speed=15, velocity=15, ClimbSpeed=5)
# render = Renderer(surface, hero, x=0, y=0)
# editor = Editor(screen, world, render, hero)

# GameMode = False
# MapMode = True

universe = Universe()

translation_map = {
    'game': {
        'key_pressed': {
            pygame.K_UP: JumpAction(),
            pygame.K_DOWN: DebugAction("CROUCH"),
            pygame.K_LEFT: MoveAction(-1),
            pygame.K_RIGHT: MoveAction(1),
            pygame.K_LSHIFT: RunAction(),
            # pygame.KMOD_NONE: StandAction()
        },
        'key_not_pressed': {
            pygame.K_LSHIFT: StopRunAction()
        },
        'key_down': {
            pygame.K_e: ChangeModeAction("map"),
            # pygame.K_LSHIFT: RunAction(),
        },
        'key_up': {
            # pygame.K_LSHIFT: StopRunAction()
        }
    },
    'map': {
        'key_pressed': {
            pygame.K_UP: DebugAction("Pressed UP"),
            pygame.K_DOWN: DebugAction("Pressed DOWN"),
            pygame.K_LEFT: DebugAction("Pressed LEFT"),
            pygame.K_RIGHT: DebugAction("Pressed Right"),
        },
        'key_not_pressed': {
        },
        'key_down': {
            pygame.K_e: ChangeModeAction("game"),
            pygame.MOUSEBUTTONDOWN: MouseDAction()
        },
        'key_up': {
            pygame.MOUSEBUTTONUP: MouseUAction()
        }
    }
}


def translate_event(mode, event):
    if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        return [DoneAction()]

    if event.type == pygame.KEYDOWN:
        action = translation_map.get(mode, {}).get('key_down', {}).get(event.key)
        if action:
            return [action]

    if event.type == pygame.KEYUP:
        action = translation_map.get(mode, {}).get('key_up', {}).get(event.key)
        if action:
            return [action]

    return []


def translate_pressed(mode):
    key_pressed = translation_map.get(mode, {}).get('key_pressed', {})
    key_not_pressed = translation_map.get(mode, {}).get('key_not_pressed', {})

    pressed = pygame.key.get_pressed()
    return (
        [action for key, action in key_pressed.items() if pressed[key]] +
        [action for key, action in key_not_pressed.items() if not pressed[key]]
    )


def main_loop():
    def collect_actions():
        result = translate_pressed(universe.mode)
        for event in pygame.event.get():
            universe.mouseCoord = pygame.mouse.get_pos()
            result += translate_event(universe.mode, event)
        return result

    while True:
        actions = collect_actions()

        if any(action.is_done() for action in actions):
            break

        for action in actions:
            action.change_universe(universe)

        universe.update()
        # render_universe()
        clock.tick(FPS)


if __name__ == "__main__":
    main_loop()
    pygame.quit()
