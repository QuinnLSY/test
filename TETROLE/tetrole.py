# -*- coding:utf-8 -*-
"""
:author: 单纯同学
:time: 2023-08-10
:software: pycharm
:commentary: 俄罗斯方块
"""

import pygame
import sys
from Board import *
from Tetromino import *

pygame.init()
screen = pygame.display.set_mode(((COL + SCORE_FIELD) * SIZE, ROW * SIZE))
Game_Board = Board()
My_Tetromino = Tetromino()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and (My_Tetromino.Left_Index(My_Tetromino.tetromino) + My_Tetromino.position) > 0:
                My_Tetromino.position -= 1
            elif event.key == pygame.K_d and (My_Tetromino.Right_Index(My_Tetromino.tetromino) + My_Tetromino.position) < COL - 1:
                My_Tetromino.position += 1

            elif event.key == pygame.K_j:
                if My_Tetromino.tetromino == L and My_Tetromino.rotation == 0 and (My_Tetromino.Left_Index(My_Tetromino.tetromino) + My_Tetromino.position) == 0:
                    My_Tetromino.rotation = My_Tetromino.rotation
                elif My_Tetromino.tetromino == L and My_Tetromino.rotation == 2 and (My_Tetromino.Right_Index(My_Tetromino.tetromino) + My_Tetromino.position) == COL - 1:
                    My_Tetromino.rotation = My_Tetromino.rotation
                else:
                    My_Tetromino.rotation = My_Tetromino.rotation - 1
                if My_Tetromino.rotation < 0:
                    My_Tetromino.rotation = 3
            elif event.key == pygame.K_l:
                if My_Tetromino.tetromino == L and My_Tetromino.rotation == 2 and (My_Tetromino.Left_Index(My_Tetromino.tetromino) + My_Tetromino.position) == 0:
                    My_Tetromino.rotation = My_Tetromino.rotation
                elif My_Tetromino.tetromino == L and My_Tetromino.rotation == 0 and (My_Tetromino.Right_Index(My_Tetromino.tetromino) + My_Tetromino.position) == COL - 1:
                    My_Tetromino.rotation = My_Tetromino.rotation
                else:
                    My_Tetromino.rotation = My_Tetromino.rotation + 1
                if My_Tetromino.rotation > 3:
                    My_Tetromino.rotation = 0

    screen.fill("#ffffff")
    Game_Board.Update(screen)
    My_Tetromino.Draw(screen, My_Tetromino.tetromino, 'red')

    pygame.display.update()
