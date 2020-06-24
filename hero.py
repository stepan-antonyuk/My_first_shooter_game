# import pygame


class Hero:

    def __init__(self, world, x, y, speed=0, velocity=0, ClimbSpeed=0):
        self.world = world
        self.x = x
        self.y = y
        self.speed = speed
        self.max_velocity = velocity
        self.velocity = 0
        self.ClimbSpeed = ClimbSpeed
        self.height = 160
        self.width = 128
        self.sit_height = 80
        self.stand_height = 160
        self.acceleration = 4

    # def render_hero(self, surface,):
    #     (x, y) = self.pos
    #     pygame.draw.rect(surface, (139,26,26), (x, y - self.height, self.width, self.height), 5)
    #     self.height = self.stand_height

    def _is_falling(self):
        for ((x1, y1), (x2, _)) in self.world.surface_altitudes:
            (x1, x2) = (x2, x1) if x1 > x2 else (x1, x2)
            if (self.x <= x2) and (x1 <= (self.x + self.width)):
                if y1 == self.y:
                    self.velocity = min(self.velocity, 0)
                    return False
                if self.y < y1 < self.y + self.velocity:
                    self.velocity = y1 - self.y
                    return True
        return True

    def move(self, direction):
        self.x += self.speed * direction

    def jump(self):
        if not self._is_falling():
            self.velocity = -30
            self.y += self.velocity

    # def check_screen_box(self):
    #     return None

    def chang_height(self, position):
        if position == -1:
            self.height = self.sit_height
        else:
            self.height = self.stand_height

    # def return_hero_pos(self):
    #     return self.x, self.y

    def gravity(self):
        if self._is_falling():
            self.y += self.velocity
            print('noo')
            print(self.x, self.y)
            self.velocity += self.acceleration

    def is_wall(self, direction):
        for ((x1, y1), (x2, y2)) in self.world.surface_altitudes:
            if x1 == x2:
                if direction == -1:
                    if (self.x - 7) <= x1 <= self.x:
                        if y1 > y2:
                            if ((self.y - self.height) < y1) and (self.y > y2):
                                self.speed = self.x - x1 - 1
                                self.move(direction)
                                self.speed = 7
                                return True
                        elif y1 < y2:
                            if ((self.y - self.height) < y2) and (self.y > y1):
                                self.speed = self.x - x1 - 1
                                self.move(direction)
                                self.speed = 7
                                return True
                elif direction == 1:
                    if ((self.x + self.width) + 7) >= x1 >= (self.x + self.width):
                        if y1 > y2:
                            if ((self.y - self.height) < y1) and (self.y > y2):
                                self.speed = x1 - (self.x + self.width) - 1
                                self.move(direction)
                                self.speed = 7
                                return True
                        elif y1 < y2:
                            if ((self.y - self.height) < y2) and (self.y > y1):
                                self.speed = x1 - (self.x + self.width) - 1
                                self.move(direction)
                                self.speed = 7
                                return True
        return False

    pos = property(lambda self: (self.x, self.y))
