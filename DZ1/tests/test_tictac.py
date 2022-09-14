import io
import sys

import pytest
from DZ1.TicTac import TicTac


@pytest.fixture
def game():
    return TicTac.TicTac()


@pytest.fixture
def clear_board():
    return [["_" for _ in range(3)] for _ in range(3)]


def test_validate_input_positive(monkeypatch, game):
    step = "1 1\n"
    monkeypatch.setattr('sys.stdin', io.StringIO(step))  # Помещаем содержимое step в stdin
    game.validate_input()
    i, j = list(map(int, step.strip().split()))
    assert game.board[i - 1][j - 1] == "X"


def test_show_board(monkeypatch, game, clear_board):
    game.show_board()
    monkeypatch.setattr('sys.stdout', io.StringIO())
    assert sys.stdout.read() == clear_board

