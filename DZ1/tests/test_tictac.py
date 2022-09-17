"""
Tests for TicTacToe game
"""
import random
import pytest
from pytest_mock import mocker

from DZ1.TicTac import TicTac


@pytest.fixture
def test_person_input_data():
    def func():
        steps = [(i, j) for i in range(3) for j in range(3)]
        return random.choice(steps)
    return func


@pytest.fixture
def game(test_person_input_data):
    return TicTac.TicTac(test_person_input_data, computer_symbol="O", person_symbol="X",
                         empty_symbol="_", dim=3, win_dim=3)


@pytest.fixture
def game_clear_board(game):
    return [[game.empty_symbol for _ in range(game.dim)] for _ in range(game.dim)]


@pytest.fixture
def game_full_board(game):
    return [
        [game.person_symbol, game.computer_symbol, game.person_symbol],
        [game.computer_symbol, game.computer_symbol, game.person_symbol],
        [game.person_symbol, game.person_symbol, game.computer_symbol],
    ]


def test_show_board(game):
    game.show_board()


def test_validate_input(game):
    assert game.validate_input() in game.steps


def test_computer_input(game):
    game.computer_input()


def test_person_input(game):
    game.validate_input = lambda: tuple((1, 0))
    game.person_input()


def test_step_input_empty(game, game_clear_board):
    step = ()
    game.step_input(step, game.computer_symbol)
    assert game.board == game_clear_board


@pytest.mark.parametrize("step", [
    (i, j) for i in range(3) for j in range(3)
])
def test_step_input(game, step: tuple):
    game.step_input(step, game.computer_symbol)
    assert game.board[step[0]][step[1]] == game.computer_symbol


@pytest.mark.parametrize("step", [
    (random.randint(0, 2), random.randint(0, 2)),
])
def test_step_input_full(game: TicTac, step: tuple):
    game.step_input(step, game.computer_symbol)
    assert game.board[step[0]][step[1]] == game.computer_symbol


@pytest.mark.xfail
def test_check_winner_with_clear_board(game):
    assert game.check_winner(game.computer_symbol)


def test_start_game_empty_steps(game):
    game.steps = []
    game.start_game()


def test_start_game(game):
    steps = [
        (0, 1),
        (0, 2),
    ]

    def _input():
        if steps:
            game.step_input(random.choice(steps), game.computer_symbol)
    game.steps = steps
    game.person_input = _input
    game.computer_input = _input
    game.start_game()


def test_start_game_win_person(game):
    steps_person = [
        (0, 0),
        (0, 1),
        (0, 2)
    ]
    steps_computer = [
        (1, 0),
        (1, 1),
        (1, 2),
    ]

    def _input(steps, symbol):
        def func():
            if steps:
                step = random.choice(steps)
                steps.remove(step)
                game.step_input(step, symbol)
        return func
    game.steps = steps_person + steps_computer
    game.person_input = _input(steps_person, game.person_symbol)
    game.computer_input = _input(steps_computer, game.computer_symbol)
    assert game.steps
    game.start_game()


def test_start_game_win_computer(game):
    steps_person = [
        (2, 0),
        (0, 1),
        (0, 2)
    ]
    steps_computer = [
        (1, 0),
        (1, 1),
        (1, 2),
    ]

    def _input(steps, symbol):
        def func():
            if steps:
                step = random.choice(steps)
                steps.remove(step)
                game.step_input(step, symbol)
        return func
    game.steps = steps_person + steps_computer
    game.person_input = _input(steps_person, game.person_symbol)
    game.computer_input = _input(steps_computer, game.computer_symbol)
    game.start_game()


def test_check_winner_diagonal(game, game_clear_board):
    steps = [
        (0, 0),
        (1, 1),
        (2, 2),
    ]
    for step in steps:
        game.step_input(step, game.computer_symbol)
    result_board = game_clear_board
    assert game.check_winner(game.computer_symbol)


def test_check_winner_reverse_diagonal(game):
    steps = [
        (0, 2),
        (1, 1),
        (2, 0),
    ]
    for step in steps:
        game.step_input(step, game.computer_symbol)
    assert game.check_winner(game.computer_symbol)


@pytest.mark.parametrize("line", [0, 1, 2])
def test_check_winner_line(game, line):
    steps = []
    for i in range(game.win_dim):
        steps.append((line, i))
    for step in steps:
        game.step_input(step, game.computer_symbol)
    assert game.check_winner(game.computer_symbol)


@pytest.mark.parametrize("column", [0, 1, 2])
def test_check_winner_column(game, column):
    steps = []
    for i in range(game.win_dim):
        steps.append((i, column))
    for step in steps:
        game.step_input(step, game.computer_symbol)
    assert game.check_winner(game.computer_symbol)
