import pygame

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.state = False

    def render(self, screen, left, top, cell_size):
        pygame.draw.rect(screen, (255, 255, 255), (((left + self.x * cell_size), (top + self.y * cell_size)),
                                                   (cell_size, cell_size)), 1)
        if self.state:
            pygame.draw.circle(screen, (0, 255, 0), ((left + self.x * cell_size) + cell_size // 2,
                                                     (top + self.y * cell_size) + cell_size // 2),
                               cell_size // 2 - 1)

