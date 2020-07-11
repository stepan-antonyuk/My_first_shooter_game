# import pygame


class Hero:

    def __init__(self, world, x, y, speed=0, velocity=0, ClimbSpeed=0):
        self.world = world
        self.x = x
        self.y = y
        self.speed = speed
        self.max_speed = speed
        self.max_velocity = velocity
        self.velocity = 0
        self.ClimbSpeed = ClimbSpeed
        self.height = 160
        self.width = 128
        self.sit_height = 80
        self.stand_height = 160
        self.minimal_y = 10**100
        self.minimal_x = 10**100
        self.acceleration = 4
        self.jump_power = -40
        self.Rpos = []

    # def render_hero(self, surface,):
    #     (x, y) = self.pos
    #     pygame.draw.rect(surface, (139,26,26), (x, y - self.height, self.width, self.height), 5)
    #     self.height = self.stand_height

    # def is_roof(self):
    #     if

    def _is_falling(self):
        self.minimal_y = 10**100
        for ((x1, y1), (x2, y2)) in self.world.surface_altitudes:
            if x1 > x2:
                (x1, x2) = (x2, x1)
            if (self.x <= x2) and (x1 <= (self.x + self.width)):
                if y1 == self.y or y2 == self.y:
                    self.velocity = min(self.velocity, 0)
                    return False
                if self.y < y1 < self.y + self.velocity:
                    if self.minimal_y > y1:
                        self.minimal_y = y1
                        self.velocity = y1 - self.y
                elif self.y < y2 < self.y + self.velocity:
                    if self.minimal_y > y2:
                        self.minimal_y = y2
                        self.velocity = y2 - self.y
        return True

    def move(self, direction):
        self.x += self.speed * direction

    def jump(self):
        if not self._is_falling():
            self.velocity = self.jump_power
            self.y += self.velocity

    def stair(self, pos):
        if abs(pos[1] - pos[0]) <= 10:
            self.y -= abs(pos[1] - pos[0]) + 1
            # self.y -= pos[0] - pos[1] - 1

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

    def count_distance_to_wall(self, x1, direction):
        if direction == 1:
            self.speed = x1 - (self.x + self.width) - 1
        else:
            self.speed = self.x - x1 - 1
        # self.move(direction)
        # self.stair((y1, y2))
        # self.speed = self.max_speed
        # return True

    def count_closest(self, direction, x1, pos):
        if direction == 1:
            if self.minimal_x > x1:
                self.minimal_x = x1
                self.count_distance_to_wall(x1, direction)
                self.Rpos = pos
        else:
            if (self.minimal_x * -1) < x1:
                self.minimal_x = x1
                self.count_distance_to_wall(x1, direction)
                self.Rpos = pos

    def move_to_wall(self, direction, pos):
        self.move(direction)
        self.stair(pos)
        self.speed = self.max_speed
        return True

    def is_wall(self, direction):
        self.minimal_x = 10**100
        wall = False
        for ((x1, y1), (x2, y2)) in self.world.surface_altitudes:
            if x1 == x2:
                (y1, y2) = (y2, y1) if y1 > y2 else (y1, y2)
                if direction == -1:
                    if (self.x - self.speed) <= x1 <= self.x:
                        if y1 > y2:
                            (y1, y2) = (y2, y1)
                        if ((self.y - self.height) < y2) and (self.y > y1):
                            self.count_closest(direction, x1, (y1, y2))
                            wall = True
                            # self.speed = self.x - x1 - 1
                            # self.move(direction)
                            # self.stair((y1, y2))
                            # self.speed = self.max_speed
                            # return True
                elif direction == 1:
                    if ((self.x + self.width) + self.speed) >= x1 >= (self.x + self.width):
                        if y1 > y2:
                            (y1, y2) = (y2, y1)
                        if ((self.y - self.height) < y2) and (self.y > y1):
                            self.count_closest(direction, x1, (y1, y2))
                            wall = True
                            # self.speed = x1 - (self.x + self.width) - 1
                            # self.move(direction)
                            # self.stair((y1, y2))
                            # self.speed = self.max_speed
                            # return True
        if wall:
            self.move_to_wall(direction, (self.Rpos))
            return True
        else:
            return False

    # def roof(self):
    #     for ((x1, y1), (x2, y2)) in self.world.surface_altitudes:

    pos = property(lambda self: (self.x, self.y))
