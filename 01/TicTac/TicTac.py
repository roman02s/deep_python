"""
TicTacToe modules
"""
import random
import sys


class TicTac:
    """Класс консольной игры в крестики-нолики"""
    def __init__(self,
                 computer_symbol: str = "O",
                 person_symbol: str = "X",
                 empty_symbol: str = "_",
                 dim: int = 3,
                 win_dim: int = 3,
                 ):
        """
        Параметры кофигурации игры, по умолчанию - стандартные правила
        :param computer_symbol: символ, которым ходит компьютер
        :param person_symbol: символ, которым ходит человек
        :param empty_symbol: символ пустой ячейки
        :param dim: размерность доски
        :param win_dim: размер последовательности, необходимой для выигрыша
        """
        self.computer_symbol = computer_symbol
        self.person_symbol = person_symbol
        self.empty_symbol = empty_symbol
        self.dim = dim
        self.win_dim = win_dim
        self.board = [[empty_symbol for _ in range(dim)] for _ in range(dim)]
        self.steps = [(i, j) for i in range(dim) for j in range(dim)]

    def show_board(self):
        """Отображение доски игры в stdout"""
        max_len_symbol = max(len(self.person_symbol), len(self.computer_symbol)) + 1
        print(*range(self.dim + 1))
        for i in range(self.dim):
            print(str(i + 1), end=' ')
            for j in range(self.dim):
                print(f"{self.board[i][j]}".ljust(max_len_symbol), end='')
            print()
        print("")

    def validate_input(self) -> tuple:
        """Проверка пользовательского ввода"""
        print("Ваш ход")
        while True:
            try:
                step = tuple(map(lambda x: x - 1, list(map(int, input().split()))))
                if step in self.steps:
                    return step
                print("Введите координаты пустой ячейки")
            except (IndexError, ValueError) as error:
                print(f"Ошибка ввода: {error}")
            except KeyboardInterrupt:
                print("Вы закончили игру преждевременно!")
                sys.exit(-1)

    def computer_input(self):
        """Ввод данных компьютера"""
        if self.steps:
            self.step_input(random.choice(self.steps), self.computer_symbol)

    def person_input(self):
        """Ввод данных человека"""
        if self.steps:
            self.step_input(self.validate_input(), self.person_symbol)

    def step_input(self, step: tuple, symbol: str):
        """Выполнение хода игры"""
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
                print("Выиграл Person")
                break
            self.computer_input()
            if self.check_winner(self.computer_symbol):
                print("Выиграл Computer")
                break
        self.show_board()

    def check_winner(self, symbol: str) -> bool:
        """Поиск выигрышной комбинации"""
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
