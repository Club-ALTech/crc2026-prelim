# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_3.py
This is the template file for the part 3 of the Prelim 4.
Ceci est le fichier template pour la partie 3 du Prelim 4.
"""

from math import floor, gcd


def get_cost(tile_size: int, num_of_unique_designs: int, num_of_tiles: int):
    return (50 + floor(360 / tile_size)) * num_of_unique_designs + 80 * num_of_tiles


def rotate_by_90_degrees(tile):
    tile_rotated = []

    for i in range(len(tile)):
        row = ""

        for j in range(len(tile)):
            row += tile[len(tile)-1-j][i]
        tile_rotated.append(row)

    return tile_rotated


def are_the_same(tile1, tile2):
    if tile1 == tile2:
        return True

    for _ in range(3):
        tile2 = rotate_by_90_degrees(tile2)

        if tile1 == rotate_by_90_degrees(tile2):
            return True

    return False


def get_number_of_unique_designs(mosaic, tile_size):
    tiles = []

    row = 0
    while row < len(mosaic):
        column = 0

        while column < len(mosaic[0]):
            tile = [mosaic[row+i][column:column+tile_size] for i in range(tile_size)]
            column += tile_size

            new_design_found = True
            for t in tiles:
                if are_the_same(t, tile):
                    new_design_found = False
                    break

            if new_design_found:
                tiles.append(tile)

        row += tile_size

    return len(tiles)


def part_3(m: int, n: int, mosaic: list[str]):
    """
    Find the best cost for tiling this mosaic floor

    Parameters:
        m int: the height of the mosaic floor
        n int: the width of the mosaic floor
        mosaic list[str]: the pattern of the full mosaic floor

    Returns:
        int: The minimal cost to tile the full mosaic floor
    """
    min_cost = 0
    ### YOUR CODE GOES HERE ###
    ### Votre code va ici ###

    costs = []
    possible_tile_size = []
    max_possible_size = gcd(m, n)

    for i in range(1, max_possible_size + 1):
        if max_possible_size % i == 0:
            possible_tile_size.append(i)

    for size in possible_tile_size:
        total_of_tiles = (m * n) // size ** 2

        costs.append(get_cost(size, get_number_of_unique_designs(mosaic, size), total_of_tiles))

    min_cost = min(costs)

    return min_cost