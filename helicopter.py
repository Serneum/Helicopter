import pygame
from pygame.locals import K_SPACE, K_UP

class Helicopter:
    def __init__(self, image):
        self.__image = pygame.image.load("resources/" + image)

        self.__x = 100
        # Start in the center of the y axis
        self.__y = (pygame.display.Info().current_h / 2) - (self.get_height() / 2)
        self.__vel_y = 4

    def draw(self, surface):
        surface.blit(self.__image, (self.__x, self.__y))

    def update(self):
        keys = pygame.key.get_pressed()
        is_key_pressed = keys[K_SPACE] or keys[K_UP] or pygame.mouse.get_pressed()[0]
        self.__setVelY(is_key_pressed)
        self.__move()

    def is_out_of_bounds(self):
        result = False
        if self.__y <= 0 or self.__y > pygame.display.Info().current_h - self.__image.get_rect().size[1]:
            result = True
        return result

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_width(self):
        return self.__image.get_rect().size[0]

    def get_height(self):
        return self.__image.get_rect().size[1]

    def reset(self):
        self.__y = (pygame.display.Info().current_h / 2) - (self.__image.get_rect().size[1] / 2)

    def __move(self):
        self.__y += self.__vel_y

    def __setVelY(self, is_key_pressed):
        if is_key_pressed:
            self.__vel_y = -4
        else:
            self.__vel_y = 4