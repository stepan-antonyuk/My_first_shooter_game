from Character import Character


class Universe:
    def __init__(self):
        self.hero = Character()
        self.mode = "map"
        self.mouseCoords = (0, 0)

    def update(self):
        pass
        # Character.draw_me()
