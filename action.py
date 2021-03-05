from Universe import Universe


class Action:
    def is_done(self):
        return False

    def change_universe(self, universe: Universe):
        pass


class DoneAction(Action):
    def is_done(self):
        return True


class NopAction(Action):
    pass


class DebugAction(Action):
    def __init__(self, message):
        self.message = message

    def change_universe(self, universe):
        print(self.message)


class ChangeModeAction(Action):
    def __init__(self, mode):
        self.mode = mode

    def change_universe(self, universe):
        universe.mode = self.mode


class AddBlockAction(Action):
    def change_universe(self, universe):
        pass


class JumpAction(Action):
    def change_universe(self, universe):
        print("jumping")
        universe.hero.state = "jumping"


class MoveAction(Action):
    def __init__(self, direction):
        self.direction = direction

    def change_universe(self, universe):
        # if universe.hero.state != "running":
        #     universe.hero.state = "moving"
        universe.hero.direction = self.direction
        universe.hero.move()


class RunAction(Action):
    def change_universe(self, universe):
        print("run boy run")
        universe.hero.extra = 2


class StopRunAction(Action):
    def change_universe(self, universe):
        print("Stop, wait a min")
        universe.hero.extra = 1


class StandAction(Action):
    @staticmethod
    def change_universe(universe):
        universe.hero.state = "standing"
        print("standing")


class CrouchAction(Action):
    def change_universe(self, universe):
        universe.hero.state = "crouch"


class MouseDAction(Action):
    # print("standing")
    def change_universe(self, universe):
        universe.pointPressed = universe.mouseCoords
        print(universe.pointPressed)


class MouseUAction(Action):
    # print("standing")
    def change_universe(self, universe: Universe):
        universe.surface_altitudes.append(universe.pointPressed, universe.mouseCoords)
        print(universe.mouseCoords)
