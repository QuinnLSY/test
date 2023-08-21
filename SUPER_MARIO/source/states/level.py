# -*- coding:utf-8 -*-
"""
:author: 单纯同学
:time: 2023-08-21
:software: pycharm
:commentary: 超级马里奥--进入关卡
"""
import pygame
from SUPER_MARIO.source.states.main_menu import *


class Level:
    def __init__(self):
        self.finished = False
        self.next = None
        self.info = Info('level')
        self.setup_background()

    def setup_background(self):
        self.background = GRAPHICS['level_1']
        rect = self.background.get_rect()
        self.background = pygame.transform.scale(self.background, (int(rect.width*BG_MULTI),
                                                                   int(rect.height*BG_MULTI)))
        self.background_rect = self.background.get_rect()

    def update(self, surface, keys):
        self.draw(surface)

    def draw(self, surface):
        surface.blit(self.background, (0, 0))
        self.info.update()  # 金币闪烁
        self.info.draw(surface)
