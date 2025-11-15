# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_4.py
This is the template file for the part 4 of the Prelim 1.
Ceci est le fichier template pour la partie 4 du Prelim 1.
"""


def get_distance(platypus: tuple, prey: tuple) -> float:
    return (
        (prey[0] - platypus[0]) ** 2
        + (prey[1] - platypus[1]) ** 2
        + (prey[2] - platypus[2]) ** 2
    ) ** 0.5


def part_4(positions: list[(int, int, int)]):
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
    platypus: tuple = positions[0]
    preys: list[tuple] = positions[1:]
    preys_sorted = sorted(preys, key=lambda prey: get_distance(platypus, prey))

    order = [preys.index(prey) + 1 for prey in preys_sorted]

    return order
