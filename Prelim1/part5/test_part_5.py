### This is the test file and you are NOT supposed to modify it (unless you want to add more tests) ###
### Ceci est le fichier de test et vous n'êtes PAS supposé le modifier (sauf si vous voulez ajouter plus de tests) ###

# To run the test run the command pytest in the terminal being in the right folder (go see test instructions if needed)
# Pour rouler les tests avec pytest utilisez le terminal dans le bon folder et exécutez la commande pytest (voir le fichier donnée sur les tests)

from part5.part_5 import part_5


def test_from_problem_description():
    assert part_5( turns = 11, 
        board = [
            "___x_.________._",
            "_______.________",
            "_________..___._",
            "_.__._____.____.",
            "_________.__.___",
            ".____________._.",
            "_.__________.___",
            "__.______..__.__",
            "____._______.___",
            ".__.___.________",
            "______._________",
            "____..._____.___",
            "__..___.._______",
            "_______________.",
            "________._._____",
            "____.._______.__",
        ]) == "Yes"
        
    

def test_supplementaire():
    assert part_5( turns = 18,
    board = [
        "___.________.___",
        "________________",
        "_______________.",
        "____.__.._____..",
        "____.____.._____",
        "__.____________x",
        "__._____________",
        "__________._____",
        "________________",
        "._____._________",
        "________________",
        "____.___._______",
        "________________",
        "______________._",
        "______._________",
        "___.___.________",
    ]) == "No"