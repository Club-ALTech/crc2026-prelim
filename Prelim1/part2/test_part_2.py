### This is the test file and you are NOT supposed to modify it (unless you want to add more tests) ###
### Ceci est le fichier de test et vous n'êtes PAS supposé le modifier (sauf si vous voulez ajouter plus de tests) ###

# To run the test run the command pytest in the terminal being in the right folder (go see test instructions if needed)
# Pour rouler les tests avec pytest utilisez le terminal dans le bon folder et exécutez la commande pytest (voir le fichier donnée sur les tests)

from part2.part_2 import part_2


def test_from_problem_description():
    assert part_2(w = 10, h = 14, l = 50, a = 4) == 733.04
    assert part_2(w = 13, h = 10, l = 47, a = 3) == 479.88
    assert part_2(w = 16, h = 17, l = 63, a = 7) == 3140.34

def test_supplementaire():
    assert part_2(w = 9, h = 12, l = 40, a = 8) == 904.78