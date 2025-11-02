### This is the test file and you are NOT supposed to modify it (unless you want to add more tests) ###
### Ceci est le fichier de test et vous n'êtes PAS supposé le modifier (sauf si vous voulez ajouter plus de tests) ###

# To run the test run the command pytest in the terminal being in the right folder (go see test instructions if needed)
# Pour rouler les tests avec pytest utilisez le terminal dans le bon folder et exécutez la commande pytest (voir le fichier donnée sur les tests)

from part4.part_4 import part_4


def test_from_problem_description():
    assert part_4(positions = [(0, 0, 0), (5, 6, 4), (9, 9, 2), (6, 2, 3), (3, 8, 4)]) == [3, 1, 4, 2]
    assert part_4(positions = [(0, 0, 0), (4, 13, 6), (2, 6, 4), (3, 1, 7), (7, 5, 10)]) == [2, 3, 4, 1]
    assert part_4(positions = [(16, 17, 5), (4, 4, 9), (11, 16, 14), (8, 4, 9), (11, 18, 8), (17, 2, 15), (10, 18, 7)]) == [4, 6, 2, 3, 5, 1]

def test_supplementaire():
    assert part_4(positions = [(-1, -1, -1), (1, 2, 3), (4, 5, 6)]) == [1, 2]