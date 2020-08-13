import math


__block_counter = 0


def next_block_name():
    global __block_counter
    __block_counter += 1
    return "block%s" % __block_counter


class Block:

    def __init__(self, x, y, width=30, hight=30,color=(0, 0, 0)):
        self.name = next_block_name()
        self.x = x
        self.y = y
        self.radius = 10
        self.width = width
        self.hight = hight
        self.color = color

    def find_ege(self, posM):
        def in_circle(pos):
            return self.radius >= math.sqrt((posM[0] + self.renderer.x - pos[0]) ** 2 + (posM[1] + self.renderer.y - pos[1]) ** 2)

        for (pos1, pos2) in self.world.surface_altitudes:
            if in_circle(pos1):
                return pos1[0] - self.renderer.x, pos1[1] - self.renderer.y
            elif in_circle(pos2):
                return pos2[0] - self.renderer.x, pos2[1] - self.renderer.y

        return None

    def add_block(self):
        return [[self.name, self.color],[self.x, self.y, self.width, self.hight]]

    def change_color(self, color):
        self.color = color

    def in_block(self, posM):
        if self.x <= posM[0] <= (self.x + self.width) and self.y <= posM[1] <= (self.y + self.hight):
            self.color = (0, 255, 0)
            # return True
        else:
            self.color = (0, 0, 0)
            # return False
