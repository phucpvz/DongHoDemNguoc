import pygame
import math
pygame.init()

from Color import *

class Clock:
    def __init__(self, screen, center, min_len=50, sec_len=90):
        self.__screen = screen
        self.__center = center
        self.__min_len = min_len
        self.__sec_len = sec_len

    def draw(self, mins=0, secs=0):
        pygame.draw.circle(self.__screen, Color.BLACK, self.__center, 100)
        pygame.draw.circle(self.__screen, Color.AQUA, self.__center, 98)
        pygame.draw.circle(self.__screen, Color.BLACK, self.__center, 5)

        # Vẽ kim phút
        x_min = self.__center[0] + self.__min_len * math.sin(6*mins*math.pi/180)
        y_min = self.__center[1] - self.__min_len * math.cos(6*mins*math.pi/180)
        pygame.draw.line(self.__screen, Color.BLACK, self.__center, (x_min, y_min))

        # Vẽ kim giây
        x_sec = self.__center[0] + self.__sec_len * math.sin(6*secs*math.pi/180)
        y_sec = self.__center[1] - self.__sec_len * math.cos(6*secs*math.pi/180)
        pygame.draw.line(self.__screen, Color.RED, self.__center, (x_sec, y_sec))
