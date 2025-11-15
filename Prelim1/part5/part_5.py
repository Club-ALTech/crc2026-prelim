# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_5.py
This is the template file for the part 5 of the Prelim 1.
Ceci est le fichier template pour la partie 5 du Prelim 1.
"""

from dataclasses import dataclass
import math 

board = [
        "___.________.___",
        "________________",
        "_______________.",
        "____.__.._____..",
        "____.____.._____",
        "__.____________x",
        "__._____________",
        "__________._____",
        "________________",
        "._____._________",
        "________________",
        "____.___._______",
        "________________",
        "______________._",
        "______._________",
        "___.___.________",
    ]


@dataclass
class vec2D:
    x: int
    y: int

@dataclass
class platypus:
    origin: vec2D
    distance: vec2D
    movement:vec2D
    alive: True
    starvation: int
    food: vec2D

def vec_is_equal(A: vec2D, B:vec2D):
    return bool(A.x == B.x and A.y == B.y)

def distance(A:vec2D, B:vec2D):
    return int(math.fabs(A.x - B.x) + math.fabs(A.y - B.y))

def find_position(object, board: [str]):
    position = vec2D(x=0,y=0)
    for i in range(len(board)):
        position.x = str(board[i]).find(object)
        position.y = i
        if(position.x != -1):
            break
    return position

def get_all_food_position(board: [str]):
    condition = True
    positions = []
    copy = board
    count = -1
    while(condition):
        positions.append(find_position(".",copy))
        count += 1
        if(positions[count].x == -1):
            condition = False
        row = list(copy[positions[count].y])
        row[positions[count].x] = "_"
        copy[positions[count].y] = "".join(row)
    return positions

food_positions = get_all_food_position(board)

INIT = 0
SURVIVAL = 1
DEATH = -1

state = INIT 

player = platypus(find_position('x',board),vec2D(x=0,y=0),vec2D(x=0,y=0),True,0,vec2D(x=0,y=0))

def init_state():
    all_distances = []
    for j in range(len(food_positions)):
        all_distances.append(distance(player.origin,food_positions[j]))
    copy_all_distances = all_distances.copy()
    copy_all_distances.sort()
    index = all_distances.index(copy_all_distances[0])
    player.food = food_positions[index]
    print(index, "index")
    player.movement.x = -player.origin.x + player.food.x
    player.movement.y = -player.origin.y + player.food.y
    player.starvation = 0
    player.distance = copy_all_distances[0]

def survival_state():
    if(player.movement.x > 0):
        player.origin.x += 1
        player.movement.x -= 1
    elif(player.movement.x < 0):
        player.origin.x -= 1
        player.movement.x += 1
    elif(player.movement.y > 0):
        player.origin.y += 1
        player.movement.y -= 1
    elif(player.movement.y < 0):
        player.origin.y -= 1
        player.movement.y += 1
    player.starvation += 1
    if(player.starvation > 3):
        player.alive = False
        return False
    if(vec_is_equal(player.origin,player.food)):
        food_positions.remove(player.food)
        init_state()
        print("eat")

    

def part_5(turns: int, board: [str]):
    """
    Simulate the Game of platypus

    Parameters:
        turns str: The number of turns in the game
        board [str]: The 16x16 grid representing the board of the Game of platypus with x as the platypus and . the food

    Returns:
        str: Is the platypus surviving ("Yes" or "No")
    """
    final_answer = "Yes"
    ### You code goes here ###
    ### Votre code va ici ###

    state = INIT

    for i in range(turns):
        if(state == INIT):
            init_state()
            print(player)
            #print(player.food,"food")
            state = SURVIVAL
        elif(state == SURVIVAL):
            if(survival_state() == False):
                state = DEATH
            print(player,"survival")
        if(state == DEATH):
            final_answer = "No"

    print(final_answer)
    return final_answer

part_5(11,board)
#get_all_food_position(board)
#print(find_position('x',board))