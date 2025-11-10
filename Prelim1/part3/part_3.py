# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_3.py
This is the template file for the part 3 of the Prelim 1.
Ceci est le fichier template pour la partie 3 du Prelim 1.
"""

def part_3(sentence: str):
    """
    Find "ornithorynque" in the sentence

    Parameters:
        sentence str: The sentence that may contain contain the letters of "ornithorynque"

    Returns:
        [int]: The position of the letters found
    """
    mot = "ornithorynque"
    phrase = "ornithorynque est mignon"
    liste_lettre = []
    nb_valeur_liste = 0
    ### You code goes here ###
    ### Votre code va ici ###
    def verification_coordonnees(position_lettre, liste_lettre):
        print("debug: entre fct")
        print("debug: liste" + str(liste_lettre))
        for position_trouve in liste_lettre:
            print("debug: position trouve " + str( position_trouve))
            if position_lettre==position_trouve:
                print("debug: verification " )
                position_lettre=-1
                return position_lettre
                break
        else:
            if position_lettre != -1:
                return position_lettre
            position_lettre=-1
            return position_lettre

    for lettre in mot:
        print("Debug: lettre " + lettre) 
        position_lettre = phrase.find(lettre)
        print("Debug: position_lettre " + str(position_lettre))
        if nb_valeur_liste>0:
            position_lettre=verification_coordonnees(position_lettre, liste_lettre)
        #liste_lettre.append(position_lettre)
        #print("Debug: liste_lettre " + str(liste_lettre))
        #print("Debug: nb_valeur_liste " + str(nb_valeur_liste))
        liste_lettre.append(position_lettre)
        print("debug: liste" + str(liste_lettre))
        nb_valeur_liste +=1
    
    print(liste_lettre)
    return lsite_lettre
