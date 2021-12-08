import pygame
pygame.init()

from Font import *
from Color import *

class Button:

    def __init__(self, screen, x, y, width, height, backcolor=Color.AQUA, text='', on_click=None):
        self.__screen = screen
        self.__backcolor = backcolor
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__text = Font.SANS_50.render(text, True, Color.BLACK)
        self.__on_click = on_click

    def draw(self):
        pygame.draw.rect(self.__screen, self.__backcolor, 
        (self.__x, self.__y, self.__width, self.__height))
        self.__screen.blit(self.__text, (self.__x + 10, self.__y - 5))

    def check_clicked(self, x, y):
        if self.__on_click == None:
            return
        if (self.__x <= x <= self.__x + self.__width) and (self.__y <= y <= self.__y + self.__height):
            self.__on_click()