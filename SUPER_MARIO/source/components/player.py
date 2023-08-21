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

class Player(pygame.sprite.Sprite):
    def __init__(self, name):
        