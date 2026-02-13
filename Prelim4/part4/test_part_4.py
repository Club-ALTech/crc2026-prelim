### This is the test file and you are NOT supposed to modify it (unless you want to add more tests) ###
### Ceci est le fichier de test et vous n'êtes PAS supposé le modifier (sauf si vous voulez ajouter plus de tests) ###

# To run the test run the command pytest in the terminal being in the right folder (go see test instructions if needed)
# Pour rouler les tests avec pytest utilisez le terminal dans le bon folder et exécutez la commande pytest (voir le fichier donnée sur les tests)

from part4.part_4 import part_4


def test_from_problem_description():
    assert part_4([(4, 0), (0, 4), (-4, 0), (0, -4)]) == True
    assert part_4([(5, 1), (6, 4), (2, 8), (-1, 6), (-6, 8), (-8, 3)]) == False
    assert part_4([(-3, 5), (0, 0), (10, 0), (-7, 5), (3, 5), (-10, 0), (0, -10), (7, 5)]) == False
    assert part_4([(-6, -15), (3, 3), (-2, 3), (4, 18), (-8, 0), (-4, 0)]) == False

def test_supplementaire():
   assert part_4([(4, 0), (3, 3), (-3, 3), (-4, 0), (-3, -3), (3, -3)]) == True
