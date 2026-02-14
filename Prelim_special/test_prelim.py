from Prelim_special.game_logic import Board
from Prelim_special.game_visuals import run_pygame_animation
from Prelim_special.prelim import solve
import multiprocessing
import time
import random

### These are the 3 variables you can modify!
seed = 0
use_seed = False
nbr_examples = 1

#### DO NOT MODIFY AFTER THIS ######

def call_solve(penguins1, fish1, board_given, moves):
    moves.extend(solve(penguins1, fish1, board_given))

def convert(pos_16: int) -> int:
    return pos_16 * 2 + 1

valid_portals_16x16 = [(0, 0), (5, 0), (6, 0), (11, 0), (12, 0), (15, 0), (4, 1), (7, 2), (2, 3), (12, 3), (0, 4), (5, 4), (9, 4), (15, 4), (0, 5), (15, 5), (3, 6), (1, 7), (7, 7), (8, 7), (11, 7), (7, 8), (8, 8), (13, 8), (4, 9), (9, 10), (1, 11), (12, 11), (15, 11), (0, 12), (6, 12), (15, 12), (0, 13), (14, 13), (2, 14), (10, 14), (5, 15), (11, 15), (15, 15)]

valid_colors = ['R', 'G', 'B', 'Y']

def test():
    # vertical walls
    walls = [
        (12,1), (24, 1), (8, 3), (14, 5), (4, 7), (24, 7), (10, 9), (20, 9), (8, 13), (2, 15), (16, 15), (22, 15), (16, 17), (28, 17), (10, 19), (18, 21), (4, 23), (24, 23), (14, 25), (30, 27), (6, 29), (20, 29), (12, 31), (24, 31),
         # horizontal walls
        (1, 10), (1, 26), (3, 16), (3, 22), (5, 6), (5, 28), (7, 14), (9, 4), (9, 18), (11, 8), (13, 24), (15, 6), (15, 16), (17, 16), (19, 8), (19, 20), (21, 28), (23, 16), (25, 6), (25, 22), (27, 18), (29, 28), (31, 10), (31, 24)
        ]

    if use_seed:
        random.seed(seed)

    for i in range(nbr_examples):
        (fx, fy) = random.choice(valid_portals_16x16)
        f_color = random.choice(valid_colors)
        prx = random.randint(0, 15)
        pry = random.randint(0, 15)
        pyx = random.randint(0, 15)
        pyy = random.randint(0, 15)
        pbx = random.randint(0, 15)
        pby = random.randint(0, 15)
        pgx = random.randint(0, 15)
        pgy = random.randint(0, 15)

        penguins1 = [(convert(prx), convert(pry), 'R'), (convert(pyx), convert(pyy), 'Y'), (convert(pbx), convert(pby), 'B'), (convert(pgx), convert(pgy), 'G')]
        penguins2 = [(convert(prx), convert(pry), 'R'), (convert(pyx), convert(pyy), 'Y'), (convert(pbx), convert(pby), 'B'), (convert(pgx), convert(pgy), 'G')]
        penguins3 = [(convert(prx), convert(pry), 'R'), (convert(pyx), convert(pyy), 'Y'), (convert(pbx), convert(pby), 'B'), (convert(pgx), convert(pgy), 'G')]
        fish1 = (convert(fx), convert(fy), f_color)
        fish2 = (convert(fx), convert(fy), f_color)
        fish3 = (convert(fx), convert(fy), f_color)

        board_given = Board(16, 16, penguins1, fish1, walls)
        board_verification = Board(16, 16, penguins2, fish2, walls)
        board_visuals = Board(16, 16, penguins3, fish3, walls)

        manager = multiprocessing.Manager()
        moves = manager.list()
        p = multiprocessing.Process(target=call_solve, args=(penguins1, fish1, board_given, moves))

        start_time = time.perf_counter()
        p.start()
        p.join(10) ## wait a maximum of 10 seconds for execution
        end_time = time.perf_counter()
        if p.is_alive():
            print("\nTest " + str(i) + " Failed!!\nTime limit of 10 seconds exceeded!")
            p.kill()
            p.join()
            assert False

        valid_answer = board_verification.test_path(moves, (15, 9))
        if valid_answer:
            print("\nAnswer is valid!")
            print(f"Your solution has {len(moves)} moves!")
            print(f"Your solution executed for {end_time-start_time:.6f} seconds")
            run_pygame_animation(board_visuals, moves, f"Test #1 - Success!! {len(moves)} moves in {end_time-start_time:.6f} seconds")
        else:
            print("Invalid answer")
            run_pygame_animation(board_visuals, moves, "Test # " + str(i) + " - Failed!!")
    assert False

        
