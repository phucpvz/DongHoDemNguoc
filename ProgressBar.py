import pygame
pygame.init()

from Color import *

class ProgressBar:
    def __init__(self, screen, x, y, width, height, thickness=5, backcolor=Color.AQUA, bordercolor=Color.BLACK):
        self.__screen = screen
        self.__backcolor = backcolor
        self.__bordercolor = bordercolor
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__thickness = thickness

    def draw(self, percent=0):
        pygame.draw.rect(self.__screen, self.__bordercolor, 
        (self.__x - self.__thickness, self.__y - self.__thickness, self.__width + self.__thickness*2, self.__height + self.__thickness*2))
        pygame.draw.rect(self.__screen, self.__backcolor, (self.__x, self.__y, self.__width, self.__height))
        # Vẽ tiến trình
        pygame.draw.rect(self.__screen, Color.RED, (self.__x, self.__y, self.__width * percent, self.__height))
