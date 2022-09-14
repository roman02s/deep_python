import random


class TicTac:
    def __init__(self,
                 computer_symbol: str = "O",
                 person_symbol: str = "X",
                 empty_symbol: str = "_",
                 dim: int = 3,
                 win_dim: int = 3,
                 ):
        self.computer_symbol = computer_symbol
        self.person_symbol = person_symbol
        self.empty_symbol = empty_symbol
        self.dim = dim
        self.win_dim = win_dim
        self.board = [[empty_symbol for _ in range(dim)] for _ in range(dim)]
        self.steps = [(i, j) for i in range(dim) for j in range(dim)]

    def show_board(self):
        print(*range(self.dim + 1))
        for i in range(self.dim):
            print(str(i + 1), end=' ')
            for j in range(self.dim):
                print(f"{self.board[i][j]}".ljust(max(len(self.person_symbol), len(self.computer_symbol)) + 1), end='')
            print()
        print("")

    def validate_input(self) -> tuple:
        print("Ваш ход")
        while True:
            try:
                step = tuple(map(lambda x: x - 1, list(map(int, input().split()))))
                if step in self.steps:
                    return step
                else:
                    print("Введите координаты пустой ячейки")
            except (IndexError, ValueError) as er:
                print(f"Ошибка ввода: {er}")
            except KeyboardInterrupt:
                print("Вы закончили игру преждевременно!")
                exit(-1)

    def computer_input(self):
        if self.steps:
            self.step_input(random.choice(self.steps), self.computer_symbol)

    def person_input(self):
        if self.steps:
            self.step_input(self.validate_input(), self.person_symbol)

    def step_input(self, step: tuple, symbol: str):
        if not step:
            return
        if self.steps and step in self.steps:
            self.steps.remove(step)
            if self.board[step[0]][step[1]] == self.empty_symbol:
                self.board[step[0]][step[1]] = symbol

    def start_game(self):
        while self.steps:
            self.show_board()
            self.person_input()
            if self.check_winner(self.person_symbol):
                print(f"Выиграл Person")
                break
            self.computer_input()
            if self.check_winner(self.computer_symbol):
                print(f"Выиграл Computer")
                break
        self.show_board()

    def check_winner(self, symbol: str) -> bool:
        win = [symbol] * self.win_dim
        for i in range(self.dim):
            for k in range(self.dim - self.win_dim + 1):
                if win == self.board[i][k:k + self.win_dim]:
                    return True
        for j in range(self.dim):
            for k in range(self.dim - self.win_dim + 1):
                if win == [self.board[i][j] for i in range(k, k + self.win_dim)]:
                    return True
        for k in range(self.dim - self.win_dim + 1):
            if win == [self.board[i][i] for i in range(k, k + self.win_dim)]:
                return True
        for k in range(self.dim - self.win_dim + 1):
            if win == [self.board[self.dim - i - 1][i] for i in range(k, k + self.win_dim)]:
                return True
        return False
