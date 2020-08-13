import pygame


class Renderer:

    def __init__(self, screen, hero, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.screenWidth = 1920
        self.screenHeight = 1080
        self.speed = 10
        self.lineWidth = 4
        self.width = 10
        self.height = 10
        self.gridWide = 30
        self.color = (0, 0, 0)
        self.hero = hero

    # Primitives

    def draw_rect(self, pos, width, height, color):
        print(f"{pos} {color} {(pos[0] - self.x, pos[1] - self.y, width, height)}")
        pygame.draw.rect(self.screen, color, (pos[0] - self.x, pos[1] - self.y, width, height))

    def draw_line(self, pos1, pos2, width, color):
        pygame.draw.line(self.screen, color, pos1, pos2, width)

    def draw_circle(self, center, radius, color):
        pygame.draw.circle(self.screen, color, center, radius)

    def render_hero(self, surface, ):
        self.check_screen_box()
        (x, y) = (self.hero.pos[0] - self.x, self.hero.pos[1] - self.y)
        pygame.draw.rect(surface, (139, 26, 26), (x, y - self.hero.height, self.hero.width, self.hero.height), 5)
        self.hero.height = self.hero.stand_height

    # Complex

    def check_screen_box(self):
        if self.hero.x > 1500 + self.x:
            self.horizontal_move(1, self.hero.speed)
        elif self.hero.x < 420 + self.x:
            self.horizontal_move(-1, self.hero.speed)

        if self.hero.y > 730 + self.y:
            self.vertical_move(1, abs(self.hero.velocity))
        elif self.hero.y < 350 + self.y:
            self.vertical_move(-1, abs(self.hero.velocity))

    def draw_ground_line(self, objlist):
        # for pos in coordinate:
        #     if (self.x < pos[0][0] < (self.x + self.screenWidth) and self.y < pos[0][1] < (self.y + self.screenHight)) or (self.x < pos[1][0] < (self.x + self.screenWidth) and self.y < pos[1][1] < (self.y + self.screenHight)):
        # (pos[1][0] > self.x and pos[1][1] > self.y):
        # pygame.draw.line(self.screen, 0, (pos[0][0] - self.x, pos[0][1] - self.y),
        #                  (pos[1][0] - self.x, pos[1][1] - self.y), self.lineWidth)
        for obj in objlist:
            pos = obj.add_block()
            if self.in_screen([pos[1][0], pos[1][1]], pos[1][2], pos[1][3]):
                posN = [pos[1][0], pos[1][1]]
                self.draw_rect(posN, pos[1][2], pos[1][3], pos[0][1])

    def calculating_pos(self, pos1, pos2):
        return (pos1[0] + self.x, pos1[1] + self.y), (pos2[0] + self.x, pos2[1] + self.y)

    # def return_coordinates(self):
    #     return self.surface_altitudes

    def horizontal_move(self, direction, speed=10):
        self.x += direction * speed

    def vertical_move(self, direction, speed=10):
        self.y += direction * speed
        print(direction * speed)

    def real_pos(self, pos):
        return (pos[0] + self.x, pos[1] + self.y)

    def pos_on_grid(self, pos):
        return (pos[0] + self.x) - ((pos[0] + self.x) % self.gridWide), (pos[1] + self.y) - (
                (pos[1] + self.y) % self.gridWide)

    def in_screen(self, pos, width, hight):
        # if (self.x <= pos[0] or self.x <= (pos[0] + width)) and (
        #         self.y <= pos[1] or self.y <= (pos[1] + hight)) and (
        #         (self.x + self.screenWidth) >= pos[0] or (self.x + self.screenWidth) >= (
        #         pos[0] + width)) and (
        #         (self.y + self.screenHight) >= pos[1] or (self.y + self.screenHight) >= (pos[1] + width)):
        if (self.x <= (pos[0] + width)) and (self.y <= (pos[1] + hight)) and ((self.x + self.screenWidth) >= pos[0]) and ((self.y + self.screenHeight) >= pos[1]):
            return True
        else:
            return False

    pos = property(lambda self: (self.hero.x, self.hero.y))
