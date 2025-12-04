# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_6.py
This is the template file for the part 6 of the Prelim 2.
Ceci est le fichier template pour la partie 6 du Prelim 2.
"""

def part_5(grid: list[str], word: str):
    """
    Find the word on the Boggle grid

    Parameters:
        board [str]: The 4x4 Boggle grid
        word str: The word to find on the grid

    Returns:
        [int]: The position of the letters on the grid
    """
    letter_positions = []
    ### You code goes here ###
    ### Votre code va ici ###

    def convertir_en_position(ligne, colonne):
        return ligne * 4 + colonne

    def trouver_toutes_positions_lettre(lettre):
        positions_trouvees = []
        for ligne in range(4):
            for colonne in range(4):
                if grid[ligne][colonne] == lettre:
                    positions_trouvees.append((ligne, colonne))
        return positions_trouvees

    def obtenir_voisins(ligne, colonne):
        voisins = []
        for autre_ligne in range(4):
            for autre_colonne in range(4):
               
                if autre_ligne == ligne and autre_colonne == colonne:
                    continue
                if abs(autre_ligne - ligne) <= 1 and abs(autre_colonne - colonne) <= 1:
                    voisins.append((autre_ligne, autre_colonne))
        return voisins

    def chercher_depuis_case(ligne, colonne, index_lettre, cases_utilisees, chemin_cases):
        if grid[ligne][colonne] != word[index_lettre] or (ligne, colonne) in cases_utilisees:
            return False

        cases_utilisees.add((ligne, colonne))
        chemin_cases.append((ligne, colonne))

        if index_lettre == len(word) - 1:
            return True

        voisins = obtenir_voisins(ligne, colonne)
        for (v_ligne, v_colonne) in voisins:
            if chercher_depuis_case(v_ligne, v_colonne, index_lettre + 1, cases_utilisees, chemin_cases):
                return True

        cases_utilisees.remove((ligne, colonne))
        chemin_cases.pop()
        return False

    for ligne_depart in range(4):
        for colonne_depart in range(4):
            if grid[ligne_depart][colonne_depart] == word[0]:
                cases_utilisees = set()
                chemin_cases = []

                if chercher_depuis_case(ligne_depart, colonne_depart, 0, cases_utilisees, chemin_cases):
                
                    letter_positions = []
                    for (ligne, colonne) in chemin_cases:
                        letter_positions.append(convertir_en_position(ligne, colonne))
                    return letter_positions
        