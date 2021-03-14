from Character import Character
# from world import World


class Universe:
    def __init__(self):
        self.surface_altitudes = [((100,100),(500,100))]
        self.collision_points = []
        self.hero = Character()
        self.mode = "map"
        self.buildMode = "line"
        self.mouseCoords = (0, 0)
        self.pointPressed = (0,0)
        self.pointLeft = (0,0)
        self.gravity = -5

    def update(self):
        pass
        # Character.draw_me()

    def gravity(self):
        Character.gravity(self.gravity)

    # def build(self):
    #     if self.buildMode == "line":
