import pygame
from pygame.locals import *
from color import BLACK, WHITE
from helicopter import Helicopter
from message import Logger
from obstacles.pipe import Pipe
from random import randint

class Game:
    def __init__(self):
        self.__screen_width = 800
        self.__screen_height = 600
        self.__display = pygame.display
        self.__surface = self.__display.set_mode((self.__screen_width, self.__screen_height))
        self.__clock = pygame.time.Clock()
        self.__heli = Helicopter("helicopter.png")
        self.__logger = None
        self.__pipe_list = []

    def update(self):
        self.__heli.update()
        for pipe in self.__pipe_list:
            pipe.update()
        if self.__heli.is_colliding(None):
            self.game_over()

    def draw(self):
        self.__heli.draw(self.__surface)
        for pipe in self.__pipe_list:
            pipe.draw(self.__surface)

    def replay_or_quit(self):
        for event in pygame.event.get([KEYDOWN, KEYUP, QUIT]):
            if event.type is QUIT or (event.type is KEYDOWN and event.key is K_ESCAPE):
                pygame.quit()
                quit()
            elif event.type is KEYDOWN:
                return event.key
        if pygame.mouse.get_pressed()[0]:
                return True
        return None

    def game_over(self):
        self.__logger.message("Kaboom!", 1)
        while self.replay_or_quit() is None:
            self.__clock.tick()
        self.run()

    def run(self):
        pygame.init()
        diff_mod = {'EASY': 3, 'NORMAL': 2}
        self.__logger = Logger(self.__display, self.__surface)
        self.__heli.reset()
        pipe = Pipe(self.__screen_width, 0, 75, randint(0, self.__screen_height), 3, self.__heli.get_height() * diff_mod['EASY'])
        self.__pipe_list.append(pipe)
        while True:
            self.__surface.fill(BLACK)
            self.update()
            self.draw()
            self.replay_or_quit()
            self.__display.update()
            self.__clock.tick(60)

Game().run()