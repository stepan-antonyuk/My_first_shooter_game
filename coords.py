from typing import Tuple


class CoordConverter:

    def __init__(self, scale: Tuple[float, float], viewport: Tuple[Tuple[int, int], Tuple[int, int]]):
        self.scale = scale
        self.viewport = viewport

    def from_universe(self, point: Tuple[int, int]) -> Tuple[int, int]:
        (x_scale, y_scale) = self.scale
        (x, y) = point
        ((xv, yv), (_, _)) = self.viewport

        return (int((x - xv) / x_scale), int((y - yv) / y_scale))

    def to_universe(self, point: Tuple[int, int]) -> Tuple[int, int]:
        (x_scale, y_scale) = self.scale
        (x, y) = point
        ((xv, yv), (_, _)) = self.viewport

        return (int(x * x_scale + xv), int(y * y_scale + yv))

    # def in_viewport(self, line): # pos need to be in real coordinates(rc)
    #
    #     (pos1, pos2) = line
    #     (xp1, yp1) = self.from_universe(pos1)
    #     (xp2, yp2) = self.from_universe(pos2)
    #
    #     ((xv1, yv1), (xv2, yv2)) = self.viewport
    #     xd = xv2 - xv1
    #     yd = yv2 - yv1
    #
    #     if((0 <= xp1 <= xd) and (0 <= yp1 <= yd)) or ((0 <= xp2 <= xd) and (0 <= yp2 <= yd)):
    #         return True
    #     return False
