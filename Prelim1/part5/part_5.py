# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_5.py
This is the template file for the part 5 of the Prelim 1.
Ceci est le fichier template pour la partie 5 du Prelim 1.
"""

    
from dataclasses import dataclass
from typing import TypedDict

class Coordinate(TypedDict):
    x: int
    y: int
    
def manhattan_dist(a: Coordinate, b: Coordinate):
    return abs(b["x"]-a["x"]) + abs(b["y"]-a["y"])

def next_move(origin: Coordinate, target: Coordinate) -> Coordinate:
    """
    next atomic movement that gets origin closer to coordinate
    retourne un deplacement (ex: {x: 1, y: 0})
    """
    
    if origin["x"] == target["x"] and origin["y"] == target["y"]:
        return {"x": 0, "y": 0} # déplacement nul
    if origin["x"] < target["x"] :
        return {"x": 1, "y": 0}
    if origin["x"] > target["x"]:
        return {"x": -1, "y": 0}
    if origin["y"] < target["y"] :
        return {"x": 0, "y": 1}
    if origin["y"] > target["y"]:
        return {"x": 0, "y": -1}
    print("probleme")


def print_state(platypus: Coordinate, foods: list[Coordinate], turns_left: int):
    BOARD_SIZE = 16
    
    board = ["_"*16 for _ in range(BOARD_SIZE)]
    board[platypus["x"]][platypus["y"]] = "X"
    for f in foods:
        line_in_board = board[f["x"]] 
        index_in_line = f["y"]
        board[f["x"]] = line_in_board[:index_in_line] +"."+ line_in_board[index_in_line+1:]
    to_print = f"""
    [turns left: {turns_left}] [foods left: {len(foods)}]
    {"".join(board)}
    """
    print(to_print)


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
    remaining_food_count: int
    platypus_position: dict
    food_position: list[dict] = []
    food_position_sorted: list[dict] = [] # liste triée de la nourriture la plus proche à l'ornythorinque à la plus loin
    starvationCounter = 0
    round = 0
    
    
    distance_platypus_food = lambda food_position: manhattan_dist(platypus_position, food_position)


    # Finding platypus initial placement
    for row in range(0, len(board)):
        column = board[row].find("x")
        if (column != -1) :
            platypus_position = {"x": column, "y": row}
            break # mauvaise pratique, à changer
    else:
        import sys
        print("[red] PANIC! pas d'ornithorynque")
        sys.exit()

    print(platypus_position)

    # Finding food initial placement
    for row in range(0, len(board)):
        for column in range(0, len(board)):
            if (board[row][column] == "." ) :
                food_position.append({"x": column, "y": row})
                
    remaining_food_count = len(food_position)

    food_position_sorted = food_position.sort(key=distance_platypus_food)

    print(food_position_sorted)
    # print(food_position)
    print_state(platypus_position, food_position, turns)
    # print(remainingFood)
# 
    # Sorting food position array using a merge sort : time complexity O(nlog(n)) probably
    # print("----> ", merge_sort(food_position, platypusPosition))

    return final_answer



""" def merge_sort(array: list[dict], platypus):
    distancePlatypusFood = lambda platypus, food: abs(platypus["x"] - food["x"]) + abs(platypus["y"] - food["y"])

    if len(array) <= 1:
        return array
    
    middle = len(array) // 2
    leftHalf = array[middle:]
    rightHalf = array[:middle]

    merge_sort(leftHalf, platypus)
    merge_sort(rightHalf, platypus)

    sortedArray = []
    left_index, right_index = 0, 0
    while left_index < len(leftHalf) and right_index < len(rightHalf):
        if distancePlatypusFood(leftHalf[left_index], platypus) <= distancePlatypusFood(rightHalf[right_index], platypus):
            sortedArray.append(leftHalf[left_index])
            left_index += 1
        else:
            sortedArray.append(rightHalf[right_index])
            right_index += 1

    sortedArray.extend(leftHalf[left_index:])
    sortedArray.extend(rightHalf[right_index:])

    return sortedArray """