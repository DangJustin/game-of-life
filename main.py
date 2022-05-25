import random
import time

LIVE = '\u0023'
DEAD = '\u0020'
RANDOM = 0.75


def dead_state(width, height):
    """ Returns Board of specified height width filled with 0s """
    board_state = [[0 for _ in range(width)] for _ in range(height)]
    return board_state


def random_state(width, height):
    """ Returns Board of specified height width filled with random number"""
    board_state = dead_state(width, height)
    for j in range(height):
        for i in range(width):
            if random.random() > RANDOM:
                board_state[j][i] = 1
    return board_state


def render(board_state):
    """ Render board with specified symbols for live vs dead cells """
    width = len(board_state[0])
    print('-' * width + 2 * '-')
    for row in board_state:
        print('|', end='')
        for state in row:
            if state == 1:
                print(LIVE, end='')
            else:
                print(DEAD, end='')
        print('|')
    print('-' * width + 2 * '-')


def next_board_state(board_state):
    """ Returns next board state based on the rules of Conway's game of life
    The cell  updates its own liveness according to 4 rules:
    Any live cell with 0 or 1 live neighbors becomes dead, because of underpopulation
    Any live cell with 2 or 3 live neighbors stays alive, because its neighborhood is just right
    Any live cell with more than 3 live neighbors becomes dead, because of overpopulation
    Any dead cell with exactly 3 live neighbors becomes alive, by reproduction
    """
    height = len(board_state)
    width = len(board_state[0])
    new_state = dead_state(width, height)
    for j in range(height):
        for i in range(width):
            live = 0
            surroundings = [[j - 1, i - 1], [j - 1, i], [j - 1, i + 1], [j, i - 1], [j, i + 1],
                            [j + 1, i - 1], [j + 1, i], [j + 1, i + 1]]
            for surrounding in surroundings:
                row = surrounding[0]
                column = surrounding[1]
                if (0 <= row < height) and (0 <= column < width):
                    if board_state[row][column] == 1:
                        live += 1
            if board_state[j][i] == 1:
                if live < 2 or live == 4:
                    new_state[j][i] = 0
                else:
                    new_state[j][i] = 1
            else:
                if live == 3:
                    new_state[j][i] = 1

    return new_state


def run_forever(board_state):
    """ Run game of life forever using current board state """
    next_board = board_state
    while True:
        render(next_board)
        next_board = next_board_state(next_board)
        time.sleep(0.5)


def main():
    height = int(input("Enter a height: "))
    width = int(input("Enter a width: "))
    board = random_state(width, height)
    run_forever(board)


if __name__ == '__main__':
    main()
