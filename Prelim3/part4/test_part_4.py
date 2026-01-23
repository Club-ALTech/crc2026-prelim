### This is the test file and you are NOT supposed to modify it (unless you want to add more tests) ###
### Ceci est le fichier de test et vous n'êtes PAS supposé le modifier (sauf si vous voulez ajouter plus de tests) ###

# To run the test run the command pytest in the terminal being in the right folder (go see test instructions if needed)
# Pour rouler les tests avec pytest utilisez le terminal dans le bon folder et exécutez la commande pytest (voir le fichier donnée sur les tests)

from part4.part_4 import part_4

def test_from_problem_description():
    assert part_4(2, [50, 40], [15, 25], [15, 4], [30, 25]) == 2

    assert part_4(3, [60, 30, 25], [20, 25, 24], [30, 40, 40], [45, 50, 47]) == 1
    
def test_supplementaire():
    assert part_4(3, [30, 30, 30], [13, 15, 12], [15, 12, 13], [30, 30, 30]) == 2
