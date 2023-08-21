# -*- coding:utf-8 -*-
"""
:author: 单纯同学
:time: 2023-08-18
:software: pycharm
:commentary: 超级马里奥--主菜单
"""
import random

import pygame

from SUPER_MARIO.source.setup import *
from SUPER_MARIO.source.tools import *
from SUPER_MARIO.source.components.info import *


class MainMenu:
    def __init__(self):
        self.setup_background()  # 底图
        self.setup_player()  # 玩家
        self.setup_cursor()  # 光标
        self.info = Info('main_menu')
        self.finished = False
        self.next = 'load_screen'

    # 背景
    def setup_background(self):
        # 全页背景
        self.background = GRAPHICS['level_1']
        self.background_rect = self.background.get_rect()
        self.background = pygame.transform.scale(self.background, (int(self.background_rect.width * BG_MULTI),
                                                                   int(self.background_rect.height * BG_MULTI)))
        self.viewport = SCREEN.get_rect()
        # 中间的标志牌子
        self.caption = get_image(GRAPHICS['title_screen'], 1, 60, 176, 88, (255, 0, 220), BG_MULTI)

    # 玩家mario，左下角
    def setup_player(self):
        self.player_image = get_image(GRAPHICS['mario_bros'], 178, 32, 12, 16, (0, 0, 0), PLAYER_MULTI)

    # 选择光标，小蘑菇
    def setup_cursor(self):
        self.cursor = pygame.sprite.Sprite()
        self.cursor.image = get_image(GRAPHICS['item_objects'], 24, 160, 8, 8, (0, 0, 0), PLAYER_MULTI)
        rect = self.cursor.image.get_rect()
        rect.x, rect.y = (220, 360)
        self.cursor.rect = rect
        self.cursor.state = '1P'

    # 选择游戏状态，单人or双人
    def update_cursor(self, keys):
        if keys[pygame.K_UP]:
            self.cursor.state = '1P'
            self.cursor.rect.y = 360
        elif keys[pygame.K_DOWN]:
            self.cursor.state = '2P'
            self.cursor.rect.y = 405
        elif keys[pygame.K_RETURN]:  # 确定，进入游戏
            if self.cursor.state == '1P':
                self.finished = True
            elif self.cursor.state == '2P':
                self.finished = True

    def update(self, surface, keys):  # 在tools里调用
        self.update_cursor(keys)

        surface.blit(self.background, self.viewport)
        surface.blit(self.caption, (170, 100))
        surface.blit(self.player_image, (110, 490))
        surface.blit(self.cursor.image, self.cursor.rect)

        self.info.update()  # 金币闪烁
        self.info.draw(surface)
