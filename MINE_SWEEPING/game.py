from minesweeping import Game
from board import Board

screenSize = (800, 800)  # 屏幕大小
size = (10, 10)  # 面板规格，即piece数量
prob = 0.1  # 炸弹出现的概率

board = Board(size, prob)  # 新建可视piece承载对象

game = Game(board, screenSize)  # 新建游戏对象

game.run()  # 开始游戏
