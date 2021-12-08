import pygame
pygame.init()
from time import sleep

from Color import *
from Button import *
from Clock import *
from ProgressBar import *
from Label import *

class Countdown:

    # Âm thanh
    TICK_SOUND = pygame.mixer.Sound('music/tick.wav')
    TIMEOUT_SOUND = pygame.mixer.Sound('music/timeout.wav')

    def __init__(self):
        self.__pygameclock = pygame.time.Clock()
        self.__screen = pygame.display.set_mode((500, 600))
        pygame.display.set_caption('Đồng hồ đếm ngược')
        programIcon = pygame.image.load('photos/pngwing.com.png')
        pygame.display.set_icon(programIcon)
        self.__running = False
        self.__start = False

        self.__total_secs = 0
        self.__mins = 0
        self.__secs = 0
        self.__total = 0

        self.__buttons = []
        self.__buttons.append(Button(self.__screen, 100, 50, 50, 50, Color.AQUA, '+', self.plus_minute))
        self.__buttons.append(Button(self.__screen, 100, 130, 50, 50, Color.AQUA, '-', self.minus_minute))
        self.__buttons.append(Button(self.__screen, 350, 50, 50, 50, Color.AQUA, '+', self.plus_second))
        self.__buttons.append(Button(self.__screen, 350, 130, 50, 50, Color.AQUA, '-', self.minus_second))
        self.__buttons.append(Button(self.__screen, 50, 200, 170, 50, Color.AQUA, 'Start', self.start))
        self.__buttons.append(Button(self.__screen, 280, 200, 170, 50, Color.AQUA, 'Reset', self.reset))

        self.__clock = Clock(self.__screen, (250, 380))
        self.__progressBar = ProgressBar(self.__screen, 50, 500, 400, 50)
        self.__time = Label(self.__screen, 180, 50, forecolor=Color.RED, text=f'{self.__mins}:{self.__secs}', font=Font.SANS_100)
        self.__lbMinute = Label(self.__screen, 100, 10, forecolor=Color.RED, text='Minute')
        self.__lbSecond = Label(self.__screen, 350, 10, forecolor=Color.RED, text='Second')

    @property
    def total_secs(self):
        return self.__total_secs

    @total_secs.setter
    def total_secs(self, value):
        self.__total_secs = value
        self.__mins = self.__total_secs // 60
        self.__secs = self.__total_secs % 60

    def plus_minute(self):
        self.total_secs += 60
        self.__total = self.total_secs

    def plus_second(self):
        self.total_secs += 1
        self.__total = self.total_secs
    
    def minus_minute(self):
        if self.total_secs >= 60:
            self.total_secs -= 60
        self.__total = self.total_secs

    def minus_second(self):
        if self.total_secs >= 1:
            self.total_secs -= 1
        self.__total = self.total_secs

    def start(self):
        self.__total = self.total_secs
        self.__start = True

    def reset(self):
        self.total_secs = 0

    def run(self):
        self.__running = True
        while self.__running:
            self.__pygameclock.tick(60)
            self.__screen.fill(Color.GRAY)
            mouse_x, mouse_y = pygame.mouse.get_pos()

            self.__lbMinute.draw()
            self.__lbSecond.draw()

            for button in self.__buttons:
                button.draw()
            
            if self.__start:
                if self.total_secs > 0:
                    self.total_secs -= 1
                    sleep(1)
                else:
                    self.__start = False
            self.__time.draw(f'{self.__mins}:{self.__secs}')
            if self.__start:
                if self.total_secs > 0:
                    pygame.mixer.Sound.play(Countdown.TICK_SOUND)
                else:
                    pygame.mixer.Sound.play(Countdown.TIMEOUT_SOUND)

            if self.__total != 0:
                self.__progressBar.draw(self.total_secs/self.__total)
            else:
                self.__progressBar.draw()
            self.__clock.draw(self.__mins, self.__secs)

            # Xử lý sự kiện người dùng
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for button in self.__buttons:
                            button.check_clicked(mouse_x, mouse_y)
            pygame.display.flip()