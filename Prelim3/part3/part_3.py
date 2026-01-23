# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_3.py
This is the template file for the part 3 of the Prelim 3.
Ceci est le fichier template pour la partie 3 du Prelim 3.
"""

def pitch_is_valid(previous, current):
    if current[4] == 1:
        return previous[1] < current[1]
    
    return True


def get_group(groupe_id, mesures):
    for mesure in mesures:
        for groupe in mesure:
            if groupe[0] == groupe_id:
                return groupe

    return None


def part_3(mesures: list):
    """
    Bee-thoven

    Parameters:
        mesures list: Les groupes de notes possibles pour
                      chaque mesure ainsi que leurs paramètres

    Returns:
        list[int]: Les ids en ordre des groupes de notes qui forme la séquence valide
    """
    sequence = []
    ### YOUR CODE GOES HERE ###
    ### Votre code va ici ###

    possible_sequences = [[groupe[0]] for groupe in mesures[0]]

    for i in range(1, len(mesures)):
        for j in range(len(mesures[i])):
            for k in range(len(possible_sequences)):
                current = mesures[i][j]
                previous = get_group(possible_sequences[k][-1], mesures)

                if previous[0] // 10 == current[0] // 10:
                    previous = get_group(possible_sequences[k][-2], mesures)

                    if pitch_is_valid(previous, current) and previous[3] != current[3] and previous[3] != current[5]:
                        sq = possible_sequences[k][:-1]
                        sq.append(current[0])
                        possible_sequences.append(sq)
                else:
                    if pitch_is_valid(previous, current) and previous[3] != current[3] and previous[3] != current[5]:
                        possible_sequences[k].append(current[0])

    for sq in possible_sequences:
        duration = 0

        if len(sq) == 4:
            for i in range(len(sq)):
                duration += get_group(sq[i], mesures)[2]

            if duration == 10:
                sequence = sq
            
    return sequence