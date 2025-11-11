# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_2.py
This is the template file for the part 2 of the Prelim 1.
Ceci est le fichier template pour la partie 2 du Prelim 1.
"""

import math

def get_volume(width: int, length: int, height: int) -> float:
    return (4 / 3) * math.pi * width * length * height


def part_2(w: int, h: int, l: int, a: int):
    """
    Finds the amount of milk produced by the platypus

    Parameters:
        w int: The width of the platypus
        h int: The height of the platypus
        l int: The length of the platypus
        a int: The age of the platypus

    Returns:
        float: The amount of milk produced with 2 decimal precision
    """
    milk = 0.0
    ### You code goes here ###
    ### Votre code va ici ###
    
    milk = round(a * 0.1 * get_volume(w / 2, l / 2, h / 2) / 2, 2)

    print(milk)
    
    return milk
