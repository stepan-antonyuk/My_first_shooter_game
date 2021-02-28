class Character:
    def __init__(self):
        self.state = "standing"
        self.location = (0, 0)
        self.speed = 5
        self.sprint = 10
        self.direction = 0
        self.extra = 1

    def move(self):
        self.location = (self.location[0] + self.direction * self.speed * self.extra, self.location[1])
        print(self.location)

    def gravity(self, gravity):
        self.location[1] += gravity
