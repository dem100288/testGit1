import pygame
import Cell as cl


class Board:
    # создание поля
    def __init__(self, width, height, cell_size=30):
        self.width = width
        self.height = height
        self.board = []
        for x in range(self.width):
            row = []
            self.board.append(row)
            for y in range(self.height):
                row.append(cl.Cell(x, y))
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = cell_size

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for x in range(self.width):
            for y in range(self.height):
                self.board[x][y].render(screen, self.left, self.top, self.cell_size)

    def get_cell(self, mouse_pos):
        x, y = mouse_pos
        x -= self.left
        y -= self.top
        x0 = x // self.cell_size
        y0 = y // self.cell_size
        if x0 < 0 or x0 >= self.width or y0 < 0 or y0 >= self.height:
            print('None')
            return None
        print(f'({x0}, {y0})')
        return x0, y0

    def on_click(self, cell):
        pass

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)