"""prelim.py
This is the template file for the special Prelim challenge.
Ceci est le fichier template pour défi préliminaire spécial.
"""

import random
import time

from game_visuals import move_penguin
from game_logic import Board, Tile
from game_logic import Penguin

from collections import deque


def solve(penguins: list[tuple[int, int, str]], fish: tuple[int, int, str], board):
    """
    Solve the problem as fast and accurately as possible

    Returns:
        [String]: The list of moves to apply
    """
    moves = []
    ### You code goes here ###
    ### Votre code va ici ###

    # print(penguins)
    # print(fish)
    # print(board.tiles[15][2].content)

    # The penguin that should be moved

    main_penguin: Penguin
    valid_directions = ["U", "R", "D", "L"]

    for p in penguins:
        if p[2].strip() == fish[2]:
            main_penguin = Penguin(p[2], p[0], p[1])

    # print(fish, main_penguin)
    # print(main_penguin)

    # start_time = time.perf_counter()
    # end_time = time.perf_counter()

    print(fish, main_penguin.x, main_penguin.y)

    # for d in valid_directions:
    #     move_penguin(board, main_penguin, d)
    #     print(main_penguin.x, main_penguin.y)

    # BFS
    start = Tile(main_penguin.color.strip(), main_penguin.x, main_penguin.y)
    end = Tile("F", fish[0], fish[1])

    # path = Tile + direction
    queue = deque([(start, "U")])
    visited = set([(start, "U")])

    i = 0
    while i < 10:
        print("q ---->", queue)
        print("v ====> ", visited)

        path = queue.popleft()
        print(path)

        possible_paths = []

        # for d in valid_directions:
        #     possible_paths.append((path[0], d))

        move_penguin(board, main_penguin, path[1])

        for d in valid_directions:
            if d != path[1]:
                neighbour = (Tile(main_penguin.color.strip(), main_penguin.x, main_penguin.y), d)

                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)


        moves.append(main_penguin.color.strip() + path[1])

        if main_penguin.x == fish[0] and main_penguin.y == fish[1]:
            break

        i += 1

    print(moves)

    return moves


def convert(pos_16: int) -> int:
    return pos_16 * 2 + 1


# valid_portals_16x16 = [(0, 0), (5, 0), (6, 0), (11, 0), (12, 0), (15, 0), (4, 1), (7, 2), (2, 3), (12, 3), (0, 4), (5, 4), (9, 4), (15, 4), (0, 5), (15, 5), (3, 6), (1, 7), (7, 7), (8, 7), (11, 7), (7, 8), (8, 8), (13, 8), (4, 9), (9, 10), (1, 11), (12, 11), (15, 11), (0, 12), (6, 12), (15, 12), (0, 13), (14, 13), (2, 14), (10, 14), (5, 15), (11, 15), (15, 15)]

# valid_colors = ['R', 'G', 'B', 'Y']

# walls = [
#         (12,1), (24, 1), (8, 3), (14, 5), (4, 7), (24, 7), (10, 9), (20, 9), (8, 13), (2, 15), (16, 15), (22, 15), (16, 17), (28, 17), (10, 19), (18, 21), (4, 23), (24, 23), (14, 25), (30, 27), (6, 29), (20, 29), (12, 31), (24, 31),
#          # horizontal walls
#         (1, 10), (1, 26), (3, 16), (3, 22), (5, 6), (5, 28), (7, 14), (9, 4), (9, 18), (11, 8), (13, 24), (15, 6), (15, 16), (17, 16), (19, 8), (19, 20), (21, 28), (23, 16), (25, 6), (25, 22), (27, 18), (29, 28), (31, 10), (31, 24)
#         ]

# (fx, fy) = random.choice(valid_portals_16x16)
# f_color = random.choice(valid_colors)
# prx = random.randint(0, 15)
# pry = random.randint(0, 15)
# pyx = random.randint(0, 15)
# pyy = random.randint(0, 15)
# pbx = random.randint(0, 15)
# pby = random.randint(0, 15)
# pgx = random.randint(0, 15)
# pgy = random.randint(0, 15)

# penguins1 = [(convert(prx), convert(pry), ' R '), (convert(pyx), convert(pyy), ' Y '), (convert(pbx), convert(pby), ' B '), (convert(pgx), convert(pgy), ' G ')]
# fish1 = (convert(fx), convert(fy), f_color)
# board_given = Board(16, 16, penguins1, fish1, walls)

# solve(penguins=penguins1, fish=fish1, board=board_given)
