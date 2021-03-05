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
