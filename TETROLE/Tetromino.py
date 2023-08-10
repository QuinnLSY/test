from Tetromino_List import *
import pygame
from Board import *

class Tetromino():
    def __init__(self) -> None:
        super().__init__()
        self.tetromino = L
        self.position = 3
        self.rotation = 0

    def Draw(self, surface, tetromino, color):
        for i in range(len(tetromino[self.rotation][0])):  # 列
            for j in range(len(tetromino[self.rotation])):  # 行
                if tetromino[self.rotation][j][i] == '1':
                    pygame.draw.rect(surface, color, ((i + self.position) * SIZE, j * SIZE, SIZE - 1, SIZE - 1))

    def Left_Index(self, tetromino):
        for i in range(len(tetromino[self.rotation][0])):  # 列
            for j in range(len(tetromino[self.rotation])):  # 行
                if tetromino[self.rotation][j][i] == '1':
                    return i

    def Right_Index(self, tetromino):
        right = 0
        for i in range(len(tetromino[self.rotation][0])):  # 列
            for j in range(len(tetromino[self.rotation])):  # 行
                if tetromino[self.rotation][j][i] == '1':
                    right = i
        return right


