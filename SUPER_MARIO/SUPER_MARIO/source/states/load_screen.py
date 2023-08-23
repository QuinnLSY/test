# -*- coding:utf-8 -*-
"""
:author: 单纯同学
:time: 2023-08-21
:software: pycharm
:commentary: 超级马里奥--载入游戏，正式开始游戏
"""
import pygame
from SUPER_MARIO.source.states.main_menu import *


class LoadScreen:
    def __init__(self):
        self.finished = False
        self.next = 'level'
        self.timer = 0
        self.info = Info('load_screen')

    def update(self, surface, keys):
        self.draw(surface)
        if self.timer == 0:
            self.timer = pygame.time.get_ticks()
        if pygame.time.get_ticks() - self.timer > 2000:
            self.finished = True
            self.timer = 0

    def draw(self, surface):
        surface.fill((0, 0, 0))
        self.info.update()  # 金币闪烁
        self.info.draw(surface)
