from Character import Character
# from world import World


class Universe:
    def __init__(self, surface_altitudes):
        self.surface_altitudes = surface_altitudes
        self.hero = Character()
        self.mode = "map"
        self.mouseCoords = (0, 0)
        self.gravity = -5

    def update(self):
        pass
        # Character.draw_me()

    def gravity(self):
        Character.gravity(self.gravity)
