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
        universe.hero.state = "jumping"
