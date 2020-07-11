
__block_counter = 0


def next_block_name():
    global __block_counter
    __block_counter += 1
    return "block%s" % __block_counter


class Block:

    def __init__(self, x, y, width=10, hight=10,color=(0, 0, 0)):
        self.name = next_block_name()
        self.x = x
        self.y = y
        self.width = width
        self.hight = hight
        self.color = color

    def add_block(self):
        return [[self.name, self.color],[self.x, self.y, self.width, self.hight]]

    def change_color(self, color):
        self.color = color

    def in_block(self, posM):
        print(self.x, self.y, self.width, self.hight)
        if self.x <= posM[0] <= (self.x + self.width) and self.y <= posM[1] <= (self.y + self.hight):
            return True
        else:
            return False
