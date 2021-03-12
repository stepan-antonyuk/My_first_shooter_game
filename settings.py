import pygame

from action import *


FPS = 600
HOR_SPEED = 12

TRANSLATION_MAP = {
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
        },
        'mouse_pressed': {
        },
        'mouse_not_pressed': {
        }
    },
    'map': {
        'key_pressed': {
            # pygame.K_UP: DebugAction("Pressed UP"),
            pygame.K_UP: PressedArrowV(-1),
            # pygame.K_DOWN: DebugAction("Pressed DOWN"),
            pygame.K_DOWN: PressedArrowV(1),
            # pygame.K_LEFT: DebugAction("Pressed LEFT"),
            pygame.K_LEFT: PressedArrowH(-1),
            # pygame.K_RIGHT: DebugAction("Pressed Right"),
            pygame.K_RIGHT: PressedArrowH(1),

        },
        'key_not_pressed': {
        },
        'key_down': {
            pygame.K_e: ChangeModeAction("game"),
        },
        'key_up': {
        },
        'mouse_pressed': {
            0: DebugAction("Pressed Mouse"),
        },
        'mouse_not_pressed': {
            0: DebugAction("Not Pressed Mouse"),
            1: DebugAction("____________________________"),
        }
    }
}
