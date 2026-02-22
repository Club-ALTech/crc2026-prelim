# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_4.py
This is the template file for the part 4 of the Prelim 1.
Ceci est le fichier template pour la partie 4 du Prelim 1.
"""

import math

def part_4(positions: [(int, int, int)]):
    """
    Find the closest preys to the platypus

    Parameters:
        positions [(int, int, int)]: The position of the platypus and all the preys

    Returns:
        [int]: The ascending order of the preys' distance to the platypus
    """
    order = []
    ### You code goes here ###
    ### Votre code va ici ###

    origin = positions[0]
    Delta = []
    
    for i in range(1,len(positions)):
        delta = []
        for j in range(3):
            delta.append(positions[i][j] - origin[j])
        D = math.sqrt(math.pow(delta[0],2) + math.pow(delta[1],2) + math.pow(delta[2],2))
        Delta.append(D)

    DeltaCopy = Delta.copy()
    DeltaCopy.sort()
    for k in range(0,len(DeltaCopy)):
        order.append(Delta.index(DeltaCopy[k]) + 1)

    print(order)
    return order

part_4([(16, 17, 5), (4, 4, 9), (11, 16, 14), (8, 4, 9), (11, 18, 8), (17, 2, 15), (10, 18, 7)])