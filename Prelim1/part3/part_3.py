# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_3.py
This is the template file for the part 3 of the Prelim 1.
Ceci est le fichier template pour la partie 3 du Prelim 1.
"""

def string_to_array(phrase: str):
    array = []
    for letter in phrase:
        array.append(letter)
    return array

def find(array: list, letter):
    j = -1
    k = 0
    condition = True
    for i in array:
        j += 1
        if(i == letter):
            condition = False
            k = j
            break
    if(condition == True):
        j = -1
    if(condition == False):
        array[k] = ''
    return j

def part_3(sentence: str):
    """
    Find "ornithorynque" in the sentence

    Parameters:
        sentence str: The sentence that may contain contain the letters of "ornithorynque"

    Returns:
        [int]: The position of the letters found
    """
    word = "ornithorynque"
    #phrase = sentence
    positions = []

    phrase = string_to_array(sentence)

    for letter in word:
        position = find(phrase,letter)
        positions.append(position)
   

    print(positions)
    print(phrase)
    print(sentence)
    ### You code goes here ###
    ### Votre code va ici ###
    
    


    return positions

part_3("What exactly is that thing called an ornithorynque in french??")
