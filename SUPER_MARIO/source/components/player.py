# -*- coding:utf-8 -*-
"""
:author: 单纯同学
:time: 2023-08-21
:software: pycharm
:commentary: 超级马里奥--玩家动作管理
"""
import pygame
from SUPER_MARIO.source.setup import *
from SUPER_MARIO.source.tools import *


class Player(pygame.sprite.Sprite):  # 在level中调用
    def __init__(self, name):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.setup_states()
        self.setup_velocities()
        self.setup_timers()
        self.load_images()

    # 设置状态
    def setup_states(self):
        self.face_right = True
        self.dead = False
        self.big = False

    # 各种速度
    def setup_velocities(self):
        self.x_vel = 0
        self.y_vel = 0

    # 各状态计时器
    def setup_timers(self):
        self.walking_timer = 0
        self.transition_timer = 0

    def load_images(self):
        sheet = GRAPHICS['mario_bros']
        self.right_frames = []
        self.left_frames = []
        self.up_frames = []
        self.down_frames = []

        frame_rects = [
            (178, 32, 12, 16),
            (80, 32, 15, 16),
            (96, 32, 16, 16),
            (112, 32, 16, 16)
        ]

        for frame_rect in frame_rects:
            right_image = get_image(sheet, *frame_rect, (0, 0, 0), PLAYER_MULTI)
            left_image = pygame.transform.flip(right_image, True, False)  # 镜像翻转
            up_image = pygame.transform.rotate(right_image, 90)
            down_image = pygame.transform.rotate(right_image, -90)
            self.right_frames.append(right_image)
            self.left_frames.append(left_image)
            self.up_frames.append(up_image)
            self.down_frames.append(down_image)

        self.frame_index = 0
        self.frames = self.right_frames
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()

    def update(self, keys):
        self.current_time = pygame.time.get_ticks()
        if keys[pygame.K_RIGHT]:
            self.x_vel = 5
            self.y_vel = 0
            self.frames = self.right_frames
        if keys[pygame.K_LEFT]:
            self.x_vel = -5
            self.y_vel = 0
            self.frames = self.left_frames
        if keys[pygame.K_UP]:
            self.x_vel = 0
            self.y_vel = -5
            self.frames = self.up_frames
        if keys[pygame.K_DOWN]:
            self.x_vel = 0
            self.y_vel = 5
            self.frames = self.down_frames
        # 帧动画
        if self.current_time - self.walking_timer > 100:
            self.walking_timer = self.current_time
            self.frame_index += 1
            self.frame_index %= 4
        self.image = self.frames[self.frame_index]
