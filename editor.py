import pygame
import math
from block import Block


class Editor:

    def __init__(self, screen, world, render, hero):
        self.map_mode = MapEditorMode(world, render)
        self.game_mode = GameEditorMode(screen, world, render, hero)
        self.mode = self.map_mode
        self.screen = screen
        self.world = world
        self.render = render
        self.hero = hero
        self.button_pressed = False
        self.time = 0

    def on_pressed(self, pressed):
        if pressed[pygame.K_m]:
            self.mode = self.map_mode
            return False
        elif pressed[pygame.K_p]:
            self.mode = self.game_mode
            return True


class EditorMode:
    def before(self):
        raise NotImplementedError()

    def on_left_pressed(self):
        raise NotImplementedError()

    def on_left_released(self):
        raise NotImplementedError()


class GameEditorMode(EditorMode):

    def __init__(self, screen, world, render, hero):
        self.world = world
        self.screen = screen
        self.render = render
        self.hero = hero

    def before(self):
        self.render.render_hero(self.screen)
        self.hero.gravity()

    def k_left(self):
        if not self.hero.is_wall(-1):
            self.hero.move(-1)

    def k_right(self):
        if not self.hero.is_wall(1):
            self.hero.move(1)

    def k_up(self):
        self.hero.jump()

    def k_down(self):
        self.hero.chang_height(-1)

    def on_left_pressed(self):
        return None

    def on_left_released(self):
        return None


class MapEditorMode(EditorMode):

    def __init__(self, world, render):
        self.world = world
        self.renderer = render
        self.dragging = False
        self.drawing_line = False
        self.on_the_edge = False
        self.grid_on = False
        self.pos1 = 0
        self.pos2 = 0
        self.checkpoint_pos = 0
        self.radius = 10
        self.color = (0, 0, 0)

    def find_endpoint(self, posM):
        def in_circle(pos):
            return self.radius >= math.sqrt(
                (posM[0] + self.renderer.x - pos[0]) ** 2 + (posM[1] + self.renderer.y - pos[1]) ** 2)

        for (pos1, pos2) in self.world.surface_altitudes:
            if in_circle(pos1):
                return pos1[0] - self.renderer.x, pos1[1] - self.renderer.y
            elif in_circle(pos2):
                return pos2[0] - self.renderer.x, pos2[1] - self.renderer.y

        return None

    def check_grid(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_g]:
            self.grid_on = True
        if pressed[pygame.K_m]:
            self.grid_on = False

    def before(self):
        print("map editor")
        mouse_pos = pygame.mouse.get_pos()
        mouse_pos = (mouse_pos[0] + self.renderer.x, mouse_pos[1] + self.renderer.y)
        print(mouse_pos)

    def on_left_pressed(self):

        mouse_pos = self.renderer.pos_on_grid(pygame.mouse.get_pos())

        print(mouse_pos)
        self.world.append_block(Block(mouse_pos[0], mouse_pos[1]))
        self.world.on_block(mouse_pos)

        # self.check_grid()
        #
        # if self.grid_on:
        #     mouse_pos = self.renderer.pos_on_grid(pygame.mouse.get_pos())
        #     self.renderer.draw_rect(mouse_pos)
        #     self.world.append_rect(mouse_pos, self.renderer.width, self.renderer.hight)
        # elif not self.on_the_edge:
        #     if not self.dragging:
        #         self.pos1 = pygame.mouse.get_pos()
        #         self.dragging = True
        #         self.drawing_line = True
        #     else:
        #         self.pos2 = pygame.mouse.get_pos()
        #         self.renderer.draw_line(self.pos1, self._calc_end_pos(), self.renderer.lineWidth, 0)
        # elif not self.dragging:
        #     self.pos1 = self.checkpoint_pos
        #     self.dragging = True
        #     self.drawing_line = True
        # elif self.dragging:
        #     self.pos2 = pygame.mouse.get_pos()
        #     self.renderer.draw_line(self.pos1, self._calc_end_pos(), self.renderer.lineWidth, 0)

    def on_left_released(self):

        mouse_pos = self.renderer.pos_on_grid(pygame.mouse.get_pos())

        self.world.on_block(mouse_pos)

        # print("waiting for command")
        # if self.drawing_line:
        #     self.world.append_line(self.renderer.calculating_pos(self.pos1, self._calc_end_pos()))
        # if not self.dragging:
        #     center = self.find_endpoint(pygame.mouse.get_pos())
        #     if center is not None:
        #         self.renderer.draw_circle(center, self.radius, self.color)
        #         self.on_the_edge = True
        #         self.checkpoint_pos = center
        # else:
        #     self.on_the_edge = False
        # else:
        #     if
        # self.dragging = False
        # self.drawing_line = False

    def k_left(self):
        self.renderer.horizontal_move(-1)

    def k_right(self):
        self.renderer.horizontal_move(1)

    def k_up(self):
        self.renderer.vertical_move(-1)

    def k_down(self):
        self.renderer.vertical_move(1)

    def _calc_end_pos(self):
        if abs(self.pos1[0] - self.pos2[0]) > abs(self.pos1[1] - self.pos2[1]):
            return (self.pos2[0], self.pos1[1])
        else:
            return (self.pos1[0], self.pos2[1])
