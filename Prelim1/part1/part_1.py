# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_1.py
This is the template file for the part 1 of the Prelim 1.
Ceci est le fichier template pour la partie 1 du Prelim 1.
"""

# just a small helper to visualize the tail
def print_tail(tail: [str]):
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


    for i in range((size*2)+1):
        if(i >= 0 and i <= size):
          line = "|" + "_." * ((size*2)-1) + "_|"
          tail.append(line)
        else:
            line = " " * (i-size) + "\\" + "_." * (((size*2)) - ((i-size)) - 1) + "_/" + " " * (i-size)
            tail.append(line)

    print_tail(tail)

    return tail

part_1(7)
