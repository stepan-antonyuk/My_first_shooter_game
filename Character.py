class Character:
    def __init__(self):
        self.state = "standing"
        self.location = (0, 0)
        self.speed = 5
        self.sprint = 10
        self.direction = 0

    def move(self):

        if self.state == "running":
            extra = 2
        else:
            extra = 1

        self.location = (self.location[0] + self.direction * self.speed * extra, self.location[1])
        print(self.location)
