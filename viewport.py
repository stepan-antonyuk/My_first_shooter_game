

class Viewport:

    def __init__(self, display, pos):
        self.display = display
        self.pos = pos

    # def in_viewport(self, line): # pos is in real coordinates(rc)
    #     (pos1, pos2) = line
    #     (xp1, yp1) = pos1
    #     (xp2, yp2) = pos2
    #     (xd, yd) = self.display
    #     if((0 <= xp1 <= xd) and (0 <= yp1 <= yd)) or ((0 <= xp2 <= xd) and (0 <= yp2 <= yd)):
    #         return True
    #     return False
