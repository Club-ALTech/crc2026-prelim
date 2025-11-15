
# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_2.py
This is the template file for the part 2 of the Prelim 1.
Ceci est le fichier template pour la partie 2 du Prelim 1.
"""

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

    pi = 3.14159
    
    V = (4/3) * pi * w/2 * h/2 * l/2

    production = a * 0.1 if a * 0.1 <= 1.0 else 1.0

    milk = round((V/2) * production,2)

    return milk
