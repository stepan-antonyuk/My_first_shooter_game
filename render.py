import pygame


class Renderer:

    def __init__(self, screen, hero, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = 10
        self.lineWidth = 4
        self.width = 10
        self.hight = 10
        self.gridWide = 10
        self.color = (0, 0, 0)
        self.hero = hero

    # Primitives

    def draw_rect(self, pos):
        pygame.draw.rect(self.screen, self.color, (pos[0] - self.x, pos[1] - self.y, self.width, self.hight))

    def draw_line(self, pos1, pos2, width, color):
        pygame.draw.line(self.screen, color, pos1, pos2, width)

    def draw_circle(self, center, radius, color):
        pygame.draw.circle(self.screen, color, center, radius)

    def render_hero(self, surface,):
        self.check_screen_box()
        (x, y) = (self.hero.pos[0] - self.x, self.hero.pos[1] - self.y)
        pygame.draw.rect(surface, (139,26,26), (x, y - self.hero.height, self.hero.width, self.hero.height), 5)
        self.hero.height = self.hero.stand_height

    # Complex

    def check_screen_box(self):
        if self.hero.x > 1500 + self.x:
            self.horizontal_move(1, self.hero.speed)
        elif self.hero.x < 420 + self.x:
            self.horizontal_move(-1, self.hero.speed)

        if self.hero.y > 730 + self.y:
            self.vertical_move(1)
        elif self.hero.y < 350 + self.y:
            self.vertical_move(-1)

    def draw_ground_line(self, coordinate):
        for pos in coordinate:
            if (pos[0][0] > self.x and pos[0][1] > self.y) or (pos[1][0] > self.x and pos[1][1] > self.y):
                pygame.draw.line(self.screen, 0, (pos[0][0] - self.x, pos[0][1] - self.y), (pos[1][0] - self.x, pos[1][1] - self.y), self.lineWidth)

    def calculating_pos(self, pos1, pos2):
        return (pos1[0] + self.x, pos1[1] + self.y), (pos2[0] + self.x, pos2[1] + self.y)

    # def return_coordinates(self):
    #     return self.surface_altitudes

    def horizontal_move(self, direction, speed=10):
        self.x += direction * speed

    def vertical_move(self, direction):
        self.y += direction * self.speed

    def pos_on_grid(self, pos):
        return (pos[0] + self.x) - ((pos[0] + self.x) % self.gridWide),(pos[1] + self.y) - ((pos[1] + self.y) % self.gridWide)

    pos = property(lambda self: (self.hero.x, self.hero.y))
