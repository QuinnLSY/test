# -*- coding:utf-8 -*-
"""
:author: 单纯同学
:time: 2023-08-21
:software: pycharm
:commentary: 超级马里奥--金币管理
"""
import pygame
from SUPER_MARIO.source.setup import *
from SUPER_MARIO.source.tools import *


class FlashingCoin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.frames = []
        self.frame_index = 0
        frame_rects = [(1, 160, 5, 8), (9, 160, 5, 8), (17, 160, 5, 8), (9, 160, 5, 8)]  # 多图切换,抠图位置及大小
        self.load_frames(frame_rects)
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = 280  # 金币在主菜单的位置
        self.rect.y = 54
        self.timer = 0

    def load_frames(self, frame_rects):
        sheet = GRAPHICS['item_objects']
        for frame_rect in frame_rects:
            self.frames.append(get_image(sheet, *frame_rect, (0, 0, 0), BG_MULTI))

    def update(self):
        self.current_time = pygame.time.get_ticks()
        frame_durations = [375, 125, 125, 125]

        if self.timer == 0:
            self.timer = self.current_time
        elif self.current_time - self.timer > frame_durations[self.frame_index]:
            self.frame_index += 1
            self.frame_index %= 4
            self.timer = self.current_time

        self.image = self.frames[self.frame_index]
