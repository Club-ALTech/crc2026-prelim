mot = "ornithorynque"
phrase = "What exactly is that thing called an ornithorynque in french??"
liste_lettre = []
depart = 0
    ### You code goes here ###
    ### Votre code va ici ###

def verification(position, liste) :
    for position_liste in liste :
        if position_liste == position :
            return False
    else :
        return True

for lettre in mot :
    print("debug mot " + lettre)
    position_lettre_mot=phrase.find(lettre, depart)
    print("debug position lettre mot " + str(position_lettre_mot))
    if len(liste_lettre)>0 :
        for i in range(len(phrase)) :
            if not verification(position_lettre_mot, liste_lettre):
                depart += 1
                position_lettre_mot=phrase.find(lettre, depart)
            else :
                break
    liste_lettre.append(position_lettre_mot)
    depart = 0
print (liste_lettre)
    
        
    
        
