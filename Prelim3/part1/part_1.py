# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_1.py
This is the template file for the part 1 of the Prelim 3.
Ceci est le fichier template pour la partie 1 du Prelim 3.
"""

def part_1(start: int, end: int):
    """
    Fizz-Buzz-Bees

    Parameters:
        start int: The first number to be included
        end int: The last number to be included

    Returns:
        list[str]: The numbers or replacement all int string
    """
    sequence=[]
    ### YOUR CODE GOES HERE ###
    
    for i in range(start, end + 1):
        str = ""

        if i % 3 == 0:
            str += "Fizz"
        if i % 5 == 0:
            str += "Buzz"
        if i % 7 == 0:
            str += "Bees"
        if str == "":
            str = f"{i}"

        sequence.append(str)

    return sequence
