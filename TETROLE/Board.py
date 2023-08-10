import pygame
import numpy as np

COL = 10
ROW = 25
SIZE = 35  # 网格大小
SCORE_FIELD = 5  # 分数显示占格大小
COLOR_NONE = "#3c3c3c"

class Board():
    def __init__(self):
        super().__init__()
        self.board = np.zeros((COL, ROW))

    def Load_Game(self, surface):
        for j in range(COL):
            for i in range(ROW):
                if self.board[j][i] == 0:
                    pygame.draw.rect(surface, COLOR_NONE, (j * SIZE, i * SIZE, SIZE - 1, SIZE - 1))

    def Update(self, surface):
        self.Load_Game(surface)

