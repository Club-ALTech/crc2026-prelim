### This is the test file and you are NOT supposed to modify it (unless you want to add more tests) ###
### Ceci est le fichier de test et vous n'êtes PAS supposé le modifier (sauf si vous voulez ajouter plus de tests) ###

# To run the test run the command pytest in the terminal being in the right folder (go see test instructions if needed)
# Pour rouler les tests avec pytest utilisez le terminal dans le bon folder et exécutez la commande pytest (voir le fichier donnée sur les tests)

from part1.part_1 import part_1

pattern1 = [ [1, 1, 1],
             [0, 1, 0],
             [0, 1, 0] ]

pattern2 = [ [0, 0, 1],
             [0, 1, 1],
             [0, 1, 0] ]

pattern3 = [ [1, 1],
             [1, 1] ]

pattern4 = [ [1, 0],
             [1, 0],
             [1, 1],
             [0, 1] ]

pattern5 = [ [1, 1],
             [0, 1],
             [1, 1] ]


def test_from_problem_description():
    assert part_1(pattern1) == 14
    assert part_1(pattern2) == 14
    assert part_1(pattern3) == 25
    assert part_1(pattern4) == 13

def test_supplementaire():
    assert part_1(pattern5) == 12
