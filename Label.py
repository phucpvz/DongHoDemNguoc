import pygame
pygame.init()

from Font import *
from Color import *

class Label:

    def __init__(self, screen, x, y, forecolor=Color.BLACK, text='', font=Font.SANS_25):
        self.__screen = screen
        self.__forecolor = forecolor
        self.__x = x
        self.__y = y
        self.__font = font
        self.__text = self.__font.render(text, True, self.__forecolor)

    def draw(self, text=None):
        if text != None:
            self.__text = self.__font.render(text, True, self.__forecolor)
        self.__screen.blit(self.__text, (self.__x, self.__y))