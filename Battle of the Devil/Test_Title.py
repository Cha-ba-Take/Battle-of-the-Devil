# -*- coding: UTF-8 -*-

import pygame
from pygame.locals import *
import tkinter
import sys


def window(caption, text, button):  # window関数で、メッセージを表示するポップアップを作成
    global index

    def callback(i):
        def x():  # callback(i)()という関数を作成
            global index
            index = i + 1
            win.destroy()

        return x

    win = tkinter.Tk()
    win.resizable(False, False)
    win.attributes("-topmost", True)
    win.title(caption)  # ウィンドウのキャプションを指定
    texts = text.split("/")  # "〇〇/△△"という形の引数を、"〇〇"、"△△"という値にし、textsリストに格納
    texts.append("")
    for i in texts:  # iは行数
        lbl = tkinter.Label(win, text=i)
        lbl.pack(anchor="center", pady=2)
    buttons = button.split("/")
    btn = []
    for i in range(len(buttons)):
        btn.append(tkinter.Button(win, text=buttons[i], command=callback(i)))
        btn[i].pack(padx=10, pady=10, side="right")
    win.mainloop()


def load_image(path):
    filename = "data/" + path + ".png"
    print(filename)
    try:
        image = pygame.image.load(filename)
        image = image.convert()
    except pygame.error:
        window("エラー", "ロードに失敗しました。/Error code:0001", "再試行/タイトルに戻る")
        if index == 1:
            load_image(path)
        elif index == 2:
            title()
        else:
            window("エラー", "ロードに失敗しました。/Error code:0001", "再試行/タイトルに戻る")
        image = None
    return image


def bgm(path, loops=0, volume=1.0):
    filename = "data/bgm/" + path + ".ogg"
    pygame.mixer.music.load(filename)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(loops)


def fade(path, time):
    image = load_image(path)
    clock = pygame.time.Clock()
    for i in range(0, 256, 10):
        image.set_alpha(i)
        screen.blit(image, (0, 0))
        clock.tick(time)
        pygame.display.update()


def title():
    bgm("title", loops=-1)
    screen.fill(Color("#FFFFFF"))
    pygame.display.update()
    fade("background/title_a", 20)
    background = load_image("background/title_b")
    # background = load_image("background/title_c")
    screen.blit(background, (0, 0))
    pygame.display.update()


def load():
    screen.fill(Color("#FFFFFF"))
    pygame.display.update()


def main():
    global screen
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Battle of the Devil")
    title()
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
                    fade("background/title_a", 40)
                    fade("background/black", 20)
                    load()


if __name__ == '__main__':
    main()
