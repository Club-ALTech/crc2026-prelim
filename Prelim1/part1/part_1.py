# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_1.py
This is the template file for the part 1 of the Prelim 1.
Ceci est le fichier template pour la partie 1 du Prelim 1.
"""

# just a small helper to visualize the tail
def print_tail(tail: list[str]):
    for line in tail:
        print(line)

def part_1(size: int):
    """
    Draw the platypus tail

    Parameters:
        size int: Size of the tail

    Returns:
        [String]: The platypus tail drawn
    """
    tail = []
    ### YOUR CODE GOES HERE ###
    # The large part
    for i in range(0, size + 1):
        line = "|" + "_." * (size * 2 - 1) + "_|"
        tail.append(line)

    # The diagonal part
    for i in range(0, size):
        line = " " * (i + 1) + "\\" + "_." * ((size - 1) * 2 - i) + "_/" + " " * (i + 1)
        tail.append(line)
    
    return tail
