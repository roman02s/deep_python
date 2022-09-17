"TicTacToe game"
from DZ1.TicTac import TicTac


def person_input_data() -> tuple:
    """
    input: 1 1
    return:tuple(0, 0)
    """
    return tuple(map(lambda x: x - 1, list(map(int, input().split()))))


if __name__ == "__main__":
    game = TicTac.TicTac(person_input_data)
    game.start_game()
