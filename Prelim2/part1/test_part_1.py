### This is the test file and you are NOT supposed to modify it (unless you want to add more tests) ###
### Ceci est le fichier de test et vous n'êtes PAS supposé le modifier (sauf si vous voulez ajouter plus de tests) ###

# To run the test run the command pytest in the terminal being in the right folder (go see test instructions if needed)
# Pour rouler les tests avec pytest utilisez le terminal dans le bon folder et exécutez la commande pytest (voir le fichier donnée sur les tests)

from part1.part_1 import part_1


def test_from_problem_description():
    assert part_1(d = 6,
ladders = [(1, 38), (4, 14),(21, 42), (28, 84)],
snakes = [(48, 26), (49, 11), (62, 19), (87, 24)]
) == 7
    assert part_1(d = 8,
ladders = [(7, 50)],
snakes = [(80, 30)]
) == 8

def test_supplementaire():
    assert part_1(d = 10,
ladders = [(4, 9), (41, 99)],
snakes = [(31, 5), (50, 20)]
) == 6
