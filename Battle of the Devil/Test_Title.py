# -*- coding: UTF-8 -*-

import pygame
from pygame.locals import *
import tkinter
import sys
from MainWindow import main_window


def main():
    #global screen
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Battle of the Devil")
    window = main_window(screen)
    window.title()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    pygame.mixer.music.fadeout(2000)
                    window.fade("background/title_a", 40)
                    window.fade("background/black", 20)
                    window.load("")


if __name__ == '__main__':
    main()
