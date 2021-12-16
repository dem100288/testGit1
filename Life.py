import Board as br


class Life(br.Board):

    def on_click(self, cell):
        if not self.start:
            x, y = cell
            self.board[x][y].state = not self.board[x][y].state

    def game_cycle(self):
        if self.start:
            pass
