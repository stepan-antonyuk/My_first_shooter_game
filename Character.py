

class Character:
    def __init__(self):
        self.state = "standing"
        self.location = (0, 0)
        self.speed = 5
        self.sprint = 10
        self.walk = 5
        self.crouch_speed = 2.5
        self.walk_speed = 5
        self.sprint_speed = 10
        self.run_multiplayer = 2
        self.crouch_multiplayer = 0.5
        self.walk_multiplayer = 1
        self.multiplayer = 1
        self.crouch_on = 0
        self.crouch_off = 1
        self.run_on = 2
        self.run_off = 1
        self.velocity = 0
        self.gravity_acceleration = 0.5
        self.jump_force = 15
        self.crouch = 1
        self.direction = 0
        self.run = 1
        self.hit_box = (100,-200)
        self.stand_hit_box = (100, -200)
        self.crouch_hit_box = (100, -100)

    def move(self):
        self.location = (self.location[0] + self.direction * self.speed * self.run * self.crouch, self.location[1])
        print(self.location)

    # def move(self):
    #     self.location = (self.location[0] + self.direction * self.speed * self.multiplayer, self.location[1])
    #     print(self.location)

    def _is_falling(self, surface_altitudes):
        for ((x1, y1), (x2, _)) in surface_altitudes:
            (x1, x2) = (x2, x1) if x1 > x2 else (x1, x2)
            if (self.location[0] <= x2) and (x1 <= (self.location[0] + self.hit_box[0])):
                if y1 == self.location[1]:
                    self.velocity = min(self.velocity, 0)
                    return False
                if self.location[1] < y1 < self.location[1] + self.velocity:
                    self.velocity = y1 - self.location[1]
                    return True
        return True

    def jump(self, surface_altitudes):
        if not self._is_falling(surface_altitudes):
            self.velocity -= self.jump_force
            self.location = (self.location[0], self.location[1] + self.velocity)

    # def gravity(self, gravity):
    #     self.location[1] += gravity

    def gravity(self, surface_altitudes):
        if self._is_falling(surface_altitudes):
            self.location = (self.location[0], self.location[1] + self.velocity)
            self.velocity += self.gravity_acceleration
