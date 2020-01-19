# -*- coding: UTF-8 -*-

from enum import Enum
import pygame
from pygame.locals import *
import sys
import wx
import os
import sqlite3

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
TITLE, MENU, STORY, BATTLE = range(4)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Battle of the Devil")


def window(contents):
    caption = contents[0]
    messages = contents[1].split("/")
    buttons = contents[2].split("/")
    statusBar = contents[3]
    print(caption, messages, buttons, statusBar)


def errorContentsLoad(errorCode):
    conn = sqlite3.connect("data/database.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM error_contents WHERE id = ?", errorCode)
    data = cur.fetchone()
    conn.close()
    errorCodeSentence = "Error Code : " + errorCode.zfill(4)
    return ("エラー", data[1], data[2], errorCodeSentence)


class imageType(Enum):
    CHARACTER = 0
    BACKGROUND = 1


def combinePath(paths):
    path = paths[0]
    for i in paths[1:]:
        path = os.path.join(path, i)
    return path


def loadImage(type, fileName):
    path = combinePath(("data", "images", imageType(type).name.lower(), fileName + ".png"))
    try:
        image = pygame.image.load(path)
    except pygame.error:
        errorContents = errorContentsLoad("1")
        window(errorContents)


loadImage(0, "vartfen")
