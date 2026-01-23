# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_5.py
This is the template file for the part 5 of the Prelim 3.
Ceci est le fichier template pour la partie 5 du Prelim 3.
"""

from dataclasses import dataclass


@dataclass
class Bee:
    bee_type: str
    pain: int
    region: [int]
    family: int
    nest_type: [int]
    remedies: [int]


def part_5(pain: int, geography: str, family: str, nest: str):
    """
    You will not bee-lieve how much this hurts!

    Parameters:
        pain int: The amount of pain felt
        geography str: The geographical region of the incident
        family str: The taxonomical family of the bee
        nest str: The type of nest of the bee

    Returns:
        list[str]: The remedy(ies) you should use on the bee sting
    """
    remedies=[]
    ### YOUR CODE GOES HERE ###

    pain_levels = [2, 4, 5, 6, 8]
    regions = ["africa", "asia", "europe", "north america", "south america", "oceania"]
    families = ["halictidae", "apidae", "andrenidae", "megachilidae"]
    nest_types = ["ground", "tree", "hole", "dead wood", "bamboo", "artificial nest", "garden", "rock"]
    all_remedies = ["epinephrine", "antihistamine", "ice", "antiseptic cream"]

    bees = [
        Bee("sweat bee", 1, [0, 1, 2], 0, [0, 1], [0]),
        Bee("killer bee", 4, [0, 3, 4], 1, [0, 2], [1, 3]),
        Bee("carpenter bee", 2, [2, 5], 1, [3, 4], [0]),
        Bee("honey bee", 1, [1, 2, 3, 4], 1, [2, 5], [2]),
        Bee("bumblebee", 0, [1, 2, 3, 4], 1, [1, 2, 6], [0, 2]),
        Bee("dark bee", 4, [2, 3], 1, [1], [1, 3]),
        Bee("buckfast bee", 3, [0, 2], 1, [5], [1]),
        Bee("mining bee", 3, [0, 1, 2, 3], 2, [0], [0]),
        Bee("mason bee", 1, [1, 5], 3, [1, 4, 7], [2]),
        Bee("resin bee", 2, [2], 3, [1, 5], [1, 3])
    ]

    for bee in bees:
        if pain_levels[bee.pain] == pain and regions.index(geography) in bee.region and families[bee.family] == family and nest_types.index(nest) in bee.nest_type:
            remedies = [all_remedies[i] for i in bee.remedies]
            break

    return remedies