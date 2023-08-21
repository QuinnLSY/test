# -*- coding:utf-8 -*-
"""
:author: 单纯同学
:time: 2023-08-18
:software: pycharm
:commentary: 超级马里奥--工具及游戏主控
"""
import os

import pygame
import random
import sys
from SUPER_MARIO.source.constants import *
from SUPER_MARIO.source.setup import *


class Game:
    def __init__(self, state_dict, start_state):
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
        self.keys = pygame.key.get_pressed()  # 为下面run中state.update顺利更新，需在前传入键值，否则无法更新
        self.state_dict = state_dict
        self.state = self.state_dict[start_state]

    def update(self):
        if self.state.finished:
            next_state = self.state.next
            self.state.finished = False
            self.state = self.state_dict[next_state]
        self.state.update(self.screen, self.keys)  # state是MainMenu()的对象，定义在main.py

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.keys = pygame.key.get_pressed()
                elif event.type == pygame.KEYUP:
                    self.keys = pygame.key.get_pressed()

            # self.screen.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            # image = get_image(GRAPHICS['mario_bros'], 145, 32, 16, 16, (0, 0, 0), 5)
            # self.screen.blit(image, (300, 300))
            self.update()
            pygame.display.update()
            self.clock.tick(FPS)


# 载入图片
def load_graphics(path, accept=('.jpg', '.png', '.bmp', '.gif')):
    graphics = {}
    for pic in os.listdir(path):
        name, ext = os.path.splitext(pic)  # 拆成 文件名，后缀
        if ext.lower() in accept:
            img = pygame.image.load(os.path.join(path, pic))
            if img.get_alpha():  # 透明背景，加快图像渲染
                img = img.convert_alpha()
            else:
                img = img.convert()
            graphics[name] = img
    return graphics


# 画出图片
def get_image(sheet, x, y, width, height, colorkey, scale):
    image = pygame.Surface((width, height))
    image.blit(sheet, (0, 0), (x, y, width, height))
    image.set_colorkey(colorkey)
    image = pygame.transform.scale(image, (int(width*scale), int(height*scale)))
    return image
