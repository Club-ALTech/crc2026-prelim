def part_3(phrase):
    mot = "ornithorynque"
    liste_lettre = []
    depart = 0
    ### You code goes here ###
    ### Votre code va ici ###

    def verification(position, liste):
        for position_liste in liste:
            if position_liste == position:
                return False
        else:
            return True

    for lettre in mot:
        position_lettre_mot = phrase.find(lettre, depart)

        if len(liste_lettre) > 0:
            for _ in range(len(phrase)):
                if not verification(position_lettre_mot, liste_lettre):
                    depart += 1
                    position_lettre_mot = phrase.find(lettre, depart)
                else:
                    break
        liste_lettre.append(position_lettre_mot)
        depart = 0
    return liste_lettre
