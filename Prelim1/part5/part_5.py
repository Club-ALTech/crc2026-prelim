# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_5.py
This is the template file for the part 5 of the Prelim 1.
Ceci est le fichier template pour la partie 5 du Prelim 1.
"""

import itertools
from dataclasses import astuple, dataclass
from types import SimpleNamespace

import numpy as np


@dataclass
class Coordinate:
    x: int
    y: int


def manhattan_dist(a: Coordinate, b: Coordinate) -> int:
    return abs(b.x - a.x) + abs(b.y - a.y)


def next_move(origin: Coordinate, target: Coordinate) -> Coordinate:
    """
    next atomic movement that gets origin closer to coordinate
    retourne un deplacement (ex: {x: 1, y: 0})
    """
    if target == origin:
        return Coordinate(0, 0)
    if target.y != origin.y:
        return Coordinate(x=0, y=np.sign(target.y - origin.y))
    return Coordinate(x=np.sign(target.x - origin.x), y=0)


def get_nearest_food(platypus: Coordinate, foods: list[Coordinate]) -> Coordinate:
    # Aliments triés selon leur éloignement de l'ornythorinque

    def dist_to_platypus(fp):
        return manhattan_dist(platypus, fp)

    food_sorted = sorted(foods, key=dist_to_platypus)

    """
    Aliments qui s'éloignent de la même distance de l'ornythorinque:
    est utile pour déterminer la nourriture qui sera consommée en premier en respectant la priorité de déplacement
    """
    nearest_foods_around: list[Coordinate] = []
    nearest_food = food_sorted[0]
    for food in food_sorted:
        if dist_to_platypus(food) == dist_to_platypus(nearest_food):
            nearest_foods_around.append(food)

    # Déplacement par priorité: droite > bas > gauche > haut
    moving_priority: list[Coordinate] = map(
        lambda c: Coordinate(**c),
        [{"x": 1, "y": 0}, {"x": 0, "y": 1}, {"x": -1, "y": 0}, {"x": 0, "y": -1}],
    )

    # Triage des aliments proches selon l’ordre de priorité
    order_map = {(move.x, move.y): idx for idx, move in enumerate(moving_priority)}
    nearest_foods_sorted = sorted(
        nearest_foods_around,
        key=lambda food: order_map.get(astuple(next_move(platypus, food))),
    )

    return nearest_foods_sorted[0]


def move_platypus(
    platypus: Coordinate,
    foods: list[Coordinate],
    atomic_move: Coordinate,
    starvation_counter: int,
):
    nearest_food = get_nearest_food(platypus, foods)
    platypus_new_position = Coordinate(
        x=platypus.x + atomic_move.x, y=platypus.y + atomic_move.y
    )

    if platypus_new_position == nearest_food:
        starvation_counter = 0

        for food in foods:
            if food.x == platypus_new_position.x and food.y == platypus_new_position.y:
                foods.pop(foods.index(food))
                break
    else:
        starvation_counter += 1

    return SimpleNamespace(
        **{
            "platypus": platypus_new_position,
            "foods": foods,
            "starvation_counter": starvation_counter,
        }
    )


def part_5(turns: int, board: list[str]):
    """
    Simulate the Game of platypus

    Parameters:
        turns str: The number of turns in the game
        board [str]: The 16x16 grid representing the board of the Game of platypus with x as the platypus and . the food

    Returns:
        str: Is the platypus surviving ("Yes" or "No")
    """
    final_answer = "No"
    ### You code goes here ###
    ### Votre code va ici ###
    food_position: list[Coordinate] = []
    platypus_position: Coordinate
    starvation_counter = 0
    round = 0

    # Finding platypus initial placement
    for row in range(0, len(board)):
        column = board[row].find("x")
        if column != -1:
            platypus_position = Coordinate(x=column, y=row)
            break
    else:
        import sys

        sys.exit()

    # Finding foods initial placement
    for row, column in itertools.product(range(len(board)), range(len(board))):
        if board[row][column] == ".":
            food_position.append(Coordinate(x=column, y=row))

    # Let the game BEGIIIN !!!
    while round < turns and starvation_counter < 3:
        move = next_move(
            platypus_position, get_nearest_food(platypus_position, food_position)
        )

        result_after_one_move = move_platypus(
            platypus_position, food_position, move, starvation_counter
        )
        platypus_position = result_after_one_move.platypus
        food_position = result_after_one_move.foods
        starvation_counter = result_after_one_move.starvation_counter

        round += 1

    if starvation_counter < 3:
        final_answer = "Yes"

    return final_answer
