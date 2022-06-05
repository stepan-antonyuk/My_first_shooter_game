import pygame.mouse

from universe import Universe
from Render import Renderer


class Action:
    def is_done(self):
        return False

    def change_universe(self, universe: Universe, render: Renderer):  #
        pass

    # def change_renderer(self, render: Renderer):
    #     pass


class DoneAction(Action):
    def is_done(self):
        return True


class NopAction(Action):
    pass


class DebugAction(Action):
    def __init__(self, message):
        self.message = message

    def change_universe(self, universe, render):
        print(self.message)


class ChangeModeAction(Action):
    def __init__(self, mode):
        self.mode = mode

    def change_universe(self, universe, render):
        universe.mode = self.mode


class AddBlockAction(Action):
    def change_universe(self, universe, render):
        pass


class JumpAction(Action):
    def change_universe(self, universe, render):
        print("jumping")
        universe.hero.jump(universe.surface_altitudes)
        universe.hero.state = "jumping"


class MoveAction(Action):
    def __init__(self, direction):
        self.direction = direction

    def wall(self, universe):
        pass

    def floor(self, universe):
        pass

    def change_universe(self, universe, render):
        universe.hero.direction = self.direction
        universe.hero.move()


class RunAction(Action):
    def change_universe(self, universe, render):
        print("run")
        universe.hero.state = "running"
        universe.hero.run = universe.hero.run_on


class StopRunAction(Action):
    def change_universe(self, universe, render):
        print("stop running")
        universe.hero.state = "standing"
        universe.hero.run = universe.hero.run_off


class StandAction(Action):
    @staticmethod
    def change_universe(universe):
        universe.hero.state = "standing"
        print("standing")


class CrouchAction(Action):
    def change_universe(self, universe, render):
        print("crouch")
        universe.hero.state = "crouch"
        universe.hero.hit_box = universe.hero.crouch_hit_box
        universe.hero.crouch = universe.hero.crouch_on


class StopCrouchAction(Action):
    def change_universe(self, universe, render):
        print("stop crouching")
        universe.hero.state = "standing"
        universe.hero.hit_box = universe.hero.stand_hit_box
        universe.hero.crouch = universe.hero.crouch_off


class PressedArrowH(Action):
    def __init__(self, direction):
        self.direction = direction

    def change_universe(self, universe, render):
        # print("moving viewport")
        render.move_H(self.direction)


class PressedArrowV(Action):
    def __init__(self, direction):
        self.direction = direction

    def change_universe(self, universe, render):
        # print("moving viewport")
        render.move_V(self.direction)


class LMouseP(Action):
    def change_universe(self, universe, render):
        if(universe.pointPressed == universe.pointZero):
            universe.pointPressed = render.coords.to_universe(pygame.mouse.get_pos())
        # print("Left mouse is pressed")
        # print(universe.mouseCoords)
        # print(universe.pointPressed)


class LMouseNP(Action):
    def change_universe(self, universe, render):
        if (universe.pointPressed != universe.pointZero):
            universe.surface_altitudes.append((universe.pointPressed, render.coords.to_universe(pygame.mouse.get_pos())))
            print("Line appended")
        universe.pointPressed = universe.pointZero
        # print(universe.pointPressed)
        # print("Left mouse is NOT pressed")
        # print(universe.surface_altitudes)
